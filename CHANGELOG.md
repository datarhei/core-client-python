Changelog
---------

## 2.14.0

Fixes three reasons the event streams could deliver nothing usable. All three were
found by running the streams against a live cluster and verified in the Core source.

-   Fix the event streams sending **no request body** when `filters` is omitted. The endpoints reject a bodyless request with `400` ("request doesn't contain any content", `ShouldBindJSONValidation`), so `client.v3_cluster_events_log_stream()` raised `CoreAPIError: 400` instead of streaming. `filters=None` now serializes to the empty filter set `{"filters": []}`, which is how Core expresses "deliver everything"
-   Fix the log-event streams returning only empty events on a cluster, by requesting NDJSON (`accept: application/x-json-stream`) instead of letting Core default to SSE. Core's SSE branch calls `LogEvent.Unmarshal(e)` and ignores its return value; in a cluster the proxy delivers `*api.LogEventRaw`, for which Unmarshal bails out without touching the struct, so the zero value gets serialized and the stream consists of `{"ts":0,"level":"","event":"", ...}` with an empty SSE event name. Its NDJSON branch decodes the payload correctly
-   Add `accept=` to all six streaming methods, with the constants `NDJSON` and `SSE` in `core_client.base.api._stream`, so the SSE framing (where `event_type` is the component rather than `"message"`) stays reachable
-   Mod framed mode (`frame=True`) drops the NDJSON keepalive lines Core writes every 5 seconds, matching how the SSE framing hides them as `:keepalive` comments; `frame=False` still yields them
-   Docs: `LogEventFilter.event` is **not** a regex. Core never compiles it; it is an exact, lowercased component-name lookup, so a name that does not exist silently drops every event, and a filter without `event` matches nothing. The 2.11.1 note claiming all filter values are regexes was wrong for this one field

**Breaking changes:**
- The log-event streams (`v3_events_stream`, `v3_events_log_stream`, `v3_cluster_events_stream`, `v3_cluster_events_log_stream`) now yield `("message", data_str)` instead of `(component, data_str)`, because they request NDJSON. The component is in the payload as `event`; pass `accept=SSE` to restore the previous framing. The process streams are unaffected - their endpoints always served NDJSON

## 2.13.0

Synced against the current Core OpenAPI doc (96 paths / 125 definitions vs. 85 / 112 before);
every finding was verified against the Core source, since the doc has two known errors of its own.

-   Add cluster process endpoints `v3_cluster_process_get_config`, `v3_cluster_process_get_state` and `v3_cluster_process_get_report` (`GET /api/v3/cluster/process/{id}/{config,state,report}`). The report endpoint returns a `ProcessReport`; Core's OpenAPI annotation claims `api.ProcessState`, but its handler returns `process.Report`
-   Add `v3_rtmp_get_channels` (`GET /api/v3/rtmp/channels`) with the models `RtmpChannel`/`RtmpConnection` — the detailed channel listing; `GET /api/v3/rtmp` returns names only
-   Add `v3_srt_get_channels` (`GET /api/v3/srt/channels`) with the models `SrtChannel`/`SrtChannelConnection` (Core marks the endpoint EXPERIMENTAL)
-   Add `v3_rtmp_put_disconnect` (`PUT /api/v3/rtmp/disconnect`, query `path`, `*` for all) and `v3_srt_put_disconnect` (`PUT /api/v3/srt/disconnect`)
-   Add `AsyncClient.v3_events_process_stream` for `POST /api/v3/events/process` (the node-local counterpart of `v3_cluster_events_process_stream`) and `AsyncClient.v3_events_log_stream` for `POST /api/v3/events/log` (Core alias of `/api/v3/events`)
-   Add `ProcessEvent` with `ProcessProgress`, `ProcessProgressInput`, `ProcessProgressOutput` and `ProcessProgressInputAvstream`, so the process event streams can be consumed typed via `model=ProcessEvent`
-   Fix `Srt.log` and `SrtConnection.log`: Core sends `map[string][]api.SRTLog`, they were typed `dict[str, str]` and raised a `ValidationError` as soon as the log was non-empty. Both are now `dict[str, list[SrtLog]]` with the new `SrtLog` model
-   Add `ProcessStateProgressIO.iomap` (new in the Core API)
-   Add 10 missing fields to `ProcessStateProgressIOAvstream` (`channels`, `codec`, `height`, `layout`, `level`, `pix_fmt`, `profile`, `sample_fmt`, `sampling_hz`, `width`) and `ProcessStateProgressMappingMap.id`
-   Mod `AboutResources.gpu` and `ClusterNodeResources.gpu` are typed as `list[AboutResourcesGpu]` / `list[ClusterNodeResourcesGpu]` instead of a bare `list`

## 2.12.0

-   Add `AsyncClient.v3_cluster_events_log_stream` for `POST /api/v3/cluster/events/log` (endpoint was missing; Core routes it to the same `cluster.LogEvents` handler as `/api/v3/cluster/events`, so it is an alias with identical SSE format and `LogEventFilter` semantics)
-   Add `hls` to `SessionCollectorActiveSession` (optional): per-session HLS stats reported by newer Core versions, with the new models `SessionCollectorActiveSessionHls`, `SessionCollectorActiveSessionHlsVariant`, `SessionCollectorActiveSessionHlsSegments` and `SessionCollectorActiveSessionHlsBandwidth`

## 2.11.2

-   Add official support for Python 3.14 (classifier); verified: import + full unit suite pass on 3.11–3.14
-   Mod test uses a 32+ byte JWT key to avoid PyJWT's `InsecureKeyLengthWarning`

## 2.11.1

-   Docs: `ProcessEventFilter` fields verified against the Core source (`pid`, `domain`, `type`, `core_id`); document that filter values are case-insensitive, unanchored regex, AND-combined across fields
-   Docs: README streaming section documents the regex filter semantics
-   Docs: drop the "experimental" / "do not use in production" labels from the cluster sections

## 2.11.0

-   Add async event streaming: `AsyncClient.v3_events_stream`, `v3_cluster_events_stream`, `v3_cluster_events_process_stream` — endless async generators over the SSE/NDJSON event endpoints (no read timeout, event-by-event, abort-safe). Raw `(event_type, data_str)` delivery by default; opt-in `model=` for typed events, `frame=False` for raw lines
-   Add `v3_cluster_events_process_stream` for `POST /api/v3/cluster/events/process` (endpoint was missing)
-   Add streaming helper `core_client/base/api/_stream.py`; streams use HTTP/1.1 (the Core cluster terminates HTTP/2 stream connections)
-   Add `ProcessEventFilter` model; `EventFilters.filters` is now a `list[LogEventFilter | ProcessEventFilter]` (filter process streams by `type`, `domain`, ...)
-   Add public `Client.refresh()` / `AsyncClient.arefresh()` for proactive token refresh
-   Add one-shot `401` auto-retry to the sync and async request proxies (streaming exempt)
-   Fix event filter serialization to use `model_dump(exclude_none=True)` (no more `null` filter fields); raw `dict` filters still accepted
-   Mod `LogEventFilter`/`ProcessEventFilter` use `extra="forbid"` for unambiguous union resolution

## 2.10.1

-   Fix `v3_cluster_node_put_state` parsing its `200` response as `ClusterNodeState`; the endpoint returns a string, so it now returns that string
-   Fix `v3_iam_delete_user` parsing its `200` response as `IamUser`; the endpoint returns a string, so it now returns that string
-   Add `PlayoutStatus` model (with `PlayoutStatusIO`, `PlayoutStatusSwap`) and use it for `v3_process_get_playout_input_status`, which previously returned an untyped dict

## 2.10.0

-   Fix 10 `*List` models that were modeled as `class X(BaseModel): RootModel: Y` (same bug as `ClusterReallocation`); they are now `RootModel[list[Y]]`: `IamUserPolicyList`, `IamUserList`, `ProcessList`, `FilesystemFileList`, `FilesystemList`, `RtmpList`, `ClusterNodeList`, `ClusterDbLockList`, `ConfigStorageS3List`, `ReportProcessList`
-   Fix `Srt.socketid` type from `str` to `int` (matches OpenAPI `api.SRTChannel`)
-   Fix `ProcessStateProgressIOTee.fifo_recovery_attempts_total` type from `int` to `float` (matches OpenAPI `api.ProgressIOTee`; fractional values no longer raise a validation error)
-   Fix `SessionToken` field `extras` → `extra` (the Core API expects `extra`; the old key was silently ignored)
-   Add missing fields found by a field-completeness audit against the OpenAPI schemas: `Config.update_check`/`compress`, `About.resources`, `ProcessState.pid`/`limit_mode`, `ProcessStateProgressIO.level`/`profile`/`sample_fmt`, `ProcessStateProgressMappingGraph.id`/`dst_id`, `FilesystemFile.core_id`, `FilesystemOperation.bandwidth_limit_kbit`, `ReportProcess.domain`, `ProcessReportHistory.resources`, `ClusterNodeCore.version`, `ClusterNodeResources` (`cpu_core`, `error`, `gpu`, `memory_core_bytes`, `memory_total_bytes`)
-   Add models `ConfigCompress` and `AboutResources`

**Breaking changes:**
- `ReportProcessList` (the only one of the above exported from `core_client.base.models.v3`) changes from a `BaseModel` to a `RootModel[list[ReportProcess]]`
- `Srt.socketid` is now `int` instead of `str`
- `SessionToken.extras` is renamed to `SessionToken.extra`

## 2.9.2

-   Fix `ClusterReallocation` model: it was modeled with a single `RootModel: ClusterReallocationNode` field, so `v3_cluster_put_reallocation` serialized the body as `{"RootModel": {…}}`. It is now a `RootModel[list[ClusterReallocationNode]]` and sends the documented array `[{target_node_id, process_ids}]`
-   Fix `v3_cluster_put_reallocation` parsing its response as `ClusterReallocation`; the endpoint returns a string, so it now returns that string

**Breaking changes:**
- `ClusterReallocation` is now `RootModel[list[ClusterReallocationNode]]`; `v3_cluster_put_reallocation` sends a top-level array `[{target_node_id, process_ids}]` instead of `{"RootModel": {…}}`, and returns a string instead of a `ClusterReallocation` (both prior behaviors were broken)

## 2.9.1

-   Fix `v3_fs_get_file_exists` returning the (always empty) `HEAD` body; it now returns the response headers (`dict`) with the file metadata, or an `Error` if the file does not exist

**Breaking changes:**
- `v3_fs_get_file_exists` now returns a `dict` of response headers on success instead of `bytes` (the previous `bytes` return was always empty because `HEAD` responses have no body)

## 2.9.0

-   Fix `v3_cluster_put_reallocation` and `v3_process_put_playout_input_stream` using `GET` instead of `PUT`
-   Add `v3_fs_delete_file_list` for `DELETE /api/v3/fs/{storage}` (delete multiple files by glob)
-   Add `v3_process_post_validate` (`POST /api/v3/process/validate`) and `v3_process_put_report` (`PUT /api/v3/process/{id}/report`)
-   Add cluster endpoints `v3_cluster_get_snapshot`, `v3_cluster_put_transfer`, `v3_cluster_post_events`, `v3_cluster_db_get_kv`, `v3_cluster_db_get_reallocate_map`, `v3_cluster_db_get_node_list`, `v3_cluster_db_get_process`
-   Add event endpoints `v3_events_post`, `v3_events_post_media` and the GraphQL query endpoint `graph_query`
-   Add models `EventFilters`, `LogEventFilter`, `LogEvent`, `MediaEvent`, `GraphQuery`, `GraphResponse`, `ClusterKVSValue`, `ClusterStoreNode`

## 2.8.0

-   Add `v3_process_post_probe` for `POST /api/v3/process/probe` (probe a process config directly; requires Core v16.20.0+)
-   Add optional `coreid` query parameter to `v3_cluster_process_post_probe`
-   Fix `ProcessProbeStream` field types `fps`, `bitrate_kbps`, `duration_sec` from `int` to `float` (matches the Core API; fractional values no longer raise a validation error)

## 2.7.0

-   Add cluster endpoints `v3_cluster_get_healthy`, `v3_cluster_get_deployments`, `v3_cluster_process_get_metadata`, `v3_cluster_db_get_process_map`, `v3_cluster_fs_get_file_list` (with `ClusterDeployments`/`ClusterDeploymentsProcess` models)
-   Fix `v3_cluster_process_get_probe` using `POST` instead of `GET`
-   Add opt-in `raise_on_error` that turns an `Error` response into a `CoreAPIError` exception
-   Mod reuses a pooled `httpx` client per instance instead of one per request, and adds `close()`/`aclose()` and context-manager support
-   Mod enables HTTP/2 consistently on the sync and async paths
-   Add a lock around the token refresh path (thread-safety) and an async login/refresh path (`alogin`) for `AsyncClient`
-   Mod README: note on `domain` vs. `domainpattern`, and fix the "GET processes" example
-   Mod `setup.py` with `long_description`, `license` and `project_urls` for PyPI
-   Fix `v3_fs_get_file_exists` crashing on a missing file (empty `HEAD` body now returns an `Error` instead of raising `JSONDecodeError`)
-   Add `Makefile` targets for dockerized testing (`test`, `test-integration`, `test-all`, `core-up`, `core-down`, `core-logs`) that start a fresh Core and tear it down again
-   Mod restructures integration tests into `tests/integration/` with shared fixtures: decoupled and individually runnable, session-managed JWT auth lifecycle, polling instead of fixed sleeps
-   Add integration coverage for previously untested non-cluster endpoints (`v3_fs_get_file_exists`, `v3_metrics`, `v3_process_get_report`)
-   Add `tests/integration/README.md` documenting endpoints not testable against a standalone Core (IAM, `session_token`, `fs` PATCH, playout)
-   Fix outdated test `Dockerfile` command and `RUN_INTEGRATION_TESTS` handling

## 2.6.0

-   Add `log_event_rate` to process config limits
-   Add `public_domains` to the cluster node model
-   Add `lines` to process report history
-   Add GPU fields to process state resources (usage, encoder, decoder, memory)
-   Add `map` details to process state progress mapping
-   Mod raises the lint line-length and reformats the client and API modules (black/pre-commit hook bump)
-   Mod reworks the integration tests (auth, login and config flow, conftest)

## 2.5.0

-   Mod modernizes type hints across all models to PEP 604 (`Optional[X]`/`List`/`Dict` → `X | None`, `list[...]`, `dict[...]`)

## 2.4.0

-   Add `v3_fs_get_file_exists` to check whether a file exists (`HEAD`)
-   Add cluster node filesystem endpoints (`v3_cluster_node_fs_get_file`, `v3_cluster_node_fs_get_file_list`, `v3_cluster_node_fs_head_file`, `v3_cluster_node_fs_put_file`)
-   Add cluster process probe endpoints (`v3_cluster_process_get_probe`, `v3_cluster_process_post_probe`)
-   Mod renames `v3_fs_delete_file_list` to `v3_cluster_node_fs_delete_file`

Breaking changes:
- `v3_fs_delete_file_list` is now `v3_cluster_node_fs_delete_file`

## 2.3.0

Ccompatibility: Core v16.20.0 (or older)

-   Add `iam`, `session_token` and `cluster` interfaces
-   Add `framerate`, `keyframe`, `extradata_size_bytes` to process progress
-   Add `max_minimal_history` to core config
-   Add `log_pattern` to process config and `matches` to process report
-   Add `v3_fs_delete_file_list` to delete multiple files
-   Add `v3_fs_put` for storage operations (copy, move)
-   Add `v3_process_get_report` to get reports by timestamp
-   Mod adds `domain` as `process` param
-   Mod extends `config` models
-   Mod `v3_process_get_report` with new params (created_at, exited_at)
-   Mod `v3_fs_get_file_list` with new params (size_min, size_max, lastmod_start, lastmod_end)
-   Mod renames `name` to `storage` on any `fs` definition
-   Mod `process_config` model (scheduler, runtime_duration_seconds)
-   Mod `v3_process_get_report` is now `v3_report_get_process_list`
-   Fix `v3_process_put_command` model
-   Drop Python `3.7`-`3.10` support, require Python `3.11+` (tested up to `3.13`)
-   Add Ruff lint integration and replace Flake8 in pre-commit

Breaking changes:
- `v3_process_get_report` is now `v3_process_get_report_list`
- `name` to `storage` on any `fs` definition
- new `cluster` interfaces

## 1.1.1

-   Add `v3_process_put_command` tests
-   Fix `v3_process_put_command` (id="", command="{command}")

## 1.1.0

-   Add `metrics_get` endpoint
-   Add definition `ConfigApiAuthAuth0Tenant`
-   Mod extends login tests
-   Mod allows v10.12.0 SRT api (sent_unique__bytes > sent_unique_bytes, recv_loss__bytes > recv_loss_bytes)
-   Mod allows `auth0_token` (login)
-   Mod `about` is now deprecated. Please use `about_get`
-   Mod `metrics` is now deprecated. Please use `metrics_post`
-   Add `memory_limit_mbytes` to config.debug
-   Fix `access_token` and `refresh_token` parameters (login)
-   Fix SRT testing (requires core v10.10+)

## 1.0.0

-   Initial release
