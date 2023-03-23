Changelog
---------

## 1.2.0 (open)

Breaking changes:
`v3_process_get_report` is now `v3_process_get_report_list`

-   Add `v3_fs_delete_file_list` to delete multiple files
-   Add `v3_fs_put` for storage operations (copy, move)
-   Add `v3_process_get_report` to get reports by timestamp
-   Mod `` with new params (created_at, exited_at)
-   Mod `v3_fs_get_file_list` with new params (size_min, size_max, lastmod_start, lastmod_end)
-   Mod renames `name` to `storage` on any `fs` definition
-   Mod `process_config` model (scheduler, runtime_duration_seconds)
-   Mod `v3_process_get_report` is now `v3_report_get_process_list`
-   Fix `v3_process_put_command` model

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
