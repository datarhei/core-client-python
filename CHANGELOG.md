Changelog
---------

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
