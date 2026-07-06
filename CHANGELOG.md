Changelog
---------

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
