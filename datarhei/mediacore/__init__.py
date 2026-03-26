"""Public import namespace for the datarhei MediaCore Python client."""

from __future__ import annotations

import sys

import core_client.base as _base
import core_client.base.api as _base_api
import core_client.base.models as _base_models
import core_client.base.models.v3 as _base_models_v3
import core_client.models as _models
from core_client import AsyncClient as AsyncMediaCoreClient
from core_client import Client as MediaCoreClient

# Friendly names for the new package path.
Client = MediaCoreClient
AsyncClient = AsyncMediaCoreClient

# Expose legacy submodules on the new import path.
base = _base
models = _models
sys.modules[f"{__name__}.base"] = _base
sys.modules[f"{__name__}.base.api"] = _base_api
sys.modules[f"{__name__}.base.models"] = _base_models
sys.modules[f"{__name__}.base.models.v3"] = _base_models_v3
sys.modules[f"{__name__}.models"] = _models

__all__ = [
    "MediaCoreClient",
    "AsyncMediaCoreClient",
    "Client",
    "AsyncClient",
    "base",
    "models",
]
