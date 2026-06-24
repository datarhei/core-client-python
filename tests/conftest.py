import os
from pathlib import Path


def _is_truthy(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "on"}


def _rel_path(collection_path, config) -> str:
    root = Path(str(config.rootpath)).resolve()
    item_path = Path(str(collection_path)).resolve()
    try:
        return item_path.relative_to(root).as_posix()
    except ValueError:
        return item_path.as_posix()


def pytest_ignore_collect(collection_path, config):
    """Gate which test trees pytest collects.

    * Unit tests (``tests/unit``) are always collected.
    * Integration tests (``tests/integration``) require ``RUN_INTEGRATION_TESTS``.
    * Cluster tests (``tests/cluster``) additionally require ``RUN_CLUSTER_TESTS``.
    """
    rel_path = _rel_path(collection_path, config)

    if rel_path.startswith("tests/unit"):
        return False

    if rel_path.startswith("tests/cluster"):
        return not (
            _is_truthy(os.getenv("RUN_INTEGRATION_TESTS", "0"))
            and _is_truthy(os.getenv("RUN_CLUSTER_TESTS", "0"))
        )

    if rel_path.startswith("tests/integration"):
        return not _is_truthy(os.getenv("RUN_INTEGRATION_TESTS", "0"))

    return False
