# Integration tests

These tests run against a live datarhei Core (`CORE_URL`) and are collected only
when `RUN_INTEGRATION_TESTS=1`. The session-level `manage_auth` fixture enables
JWT auth for the run and restores the original (disabled) state afterwards, so
every module is self-contained and can be run on its own.

Run them via the project Makefile (starts a fresh Core in Docker and tears it
down again):

```sh
make test-integration
```

## Endpoints intentionally not covered here

A standalone (single-node, open-source) Core does not expose the following
endpoints, so they cannot be exercised by an integration test against it. They
return `404`/`405` and would only yield meaningless "asserts an Error" tests:

| Endpoint group | Client methods | Reason |
|---|---|---|
| IAM user/policy management | `v3_iam_get_user_list`, `v3_iam_post_user`, `v3_iam_get_user`, `v3_iam_put_user`, `v3_iam_put_user_policy`, `v3_iam_put_user_policy_list`, `v3_iam_delete_user` | Cluster/enterprise feature → `404` |
| Session token | `v3_session_put_token` | Cluster/enterprise feature → `404` |
| Filesystem PATCH (symlink) | `v3_fs_patch_file` | Not supported on `mem`/`disk` storage → `405` |
| Process playout | `v3_process_get_playout_input_errorframe_encode`, `v3_process_get_playout_input_keyframe`, `v3_process_get_playout_input_reopen`, `v3_process_get_playout_input_status`, `v3_process_post_playout_input_errorframe_name`, `v3_process_put_playout_input_stream` | Commercial extension |
| Cluster | `v3_cluster_*` | Covered separately under `tests/cluster` (needs `RUN_CLUSTER_TESTS=1`) |

If coverage for these is needed in the future, the way to get it without the
corresponding backend is unit tests with a mocked `httpx` (see `tests/unit`),
asserting request construction and response parsing.
