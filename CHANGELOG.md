Changelog
---------

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
