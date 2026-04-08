import os
from pathlib import Path


def _is_truthy(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def pytest_ignore_collect(collection_path, config):
    run_integration = _is_truthy(os.getenv("RUN_INTEGRATION_TESTS", "0"))
    run_cluster = _is_truthy(os.getenv("RUN_CLUSTER_TESTS", "0"))
    if run_integration:
        root = Path(str(config.rootpath)).resolve()
        item_path = Path(str(collection_path)).resolve()
        try:
            rel_path = item_path.relative_to(root).as_posix()
        except ValueError:
            rel_path = item_path.as_posix()

        if rel_path.startswith("tests/cluster") and not run_cluster:
            return True
        return False

    root = Path(str(config.rootpath)).resolve()
    item_path = Path(str(collection_path)).resolve()
    try:
        rel_path = item_path.relative_to(root).as_posix()
    except ValueError:
        rel_path = item_path.as_posix()

    if rel_path == "tests" or rel_path.startswith("tests/unit"):
        return False
    if rel_path.startswith("tests"):
        return True
    return False
