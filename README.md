# datarhei Core PyClient
For rapid development of Python applications around the [datarhei Core](https://github.com/datarhei/core).
Requires Python 3.7+ and datarhei Core v16.10+.

---

-   [Features](#features)
-   [Install](#install)
-   [Usage](#usage)
-   [API definitions](#api-definitions)
    -   [General](#general)
    -   [Cluster (experimental)](#cluster)
    -   [Config](#config)
    -   [Filesystem](#filesystem)
    -   [Log](#log)
    -   [Metadata](#metadata)
    -   [Metrics](#metrics)
    -   [Process](#process)
    -   [Process Playout (commercial extention)](#process-playout-commercial-extention)
    -   [RTMP](#rtmp)
    -   [Session](#session)
    -   [Skills](#skills)
    -   [SRT](#srt)
    -   [Widget](#widget)
    -   [Misc](#misc)
-   [Examples](#examples)
    -   [GET token data](#get-token-data)
    -   [GET processes](#get-processes)
    -   [GET/POST/PUT/DELETE process](#post-process)
-   [API models](#api-models)
-   [Error handling](#error-handling)
-   [Developing & testing](#developing--testing)
-   [Changelog](#changelog)
-   [Contributing](#contributing)
-   [Licence](#licence)

## Features
-   Async & sync support
-   Request & response validation
-   Retries and timeout settings per request
-   Automatic `JWT` renewal
-   [pydantic Models](https://pydantic-docs.helpmanual.io/)
-   [HTTPX](https://www.python-httpx.org/)

## Install

### Latest
```sh
pip install https://github.com/datarhei/core-client-python/archive/refs/heads/main.tar.gz
```

### Specific version
```sh
pip install https://github.com/datarhei/core-client-python/archive/refs/tags/{release_tag}.tar.gz
```
*`{release_tag}` like `1.0.0`*

## Usage

#### Init arguments

-   `base_url: str`
-   **optional: basic auth jwt**
    `username: str = None, password: str = None`
-   **optional: token injection**
    `access_token: str = None, refresh_token: str = None`
-   **optional: httpx global settings**
    `retries: int = 3, timeout: float = 10.0`

#### Sync

```python
from core_client import Client

client = Client(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")
client.login()

about = client.about_get()
print(about)
```

#### Async

```python
import asyncio
from core_client import AsyncClient

client = AsyncClient(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")
client.login()

async def main():
    about = await client.about_get()
    print(about)

asyncio.run(main())
```

## API definitions

### General

-   `GET` /api

    ```python
    about()
    ```

### Cluster

***Do not use in production!***
*This is an upcoming feature. More here: [Core v16.10#cluster](https://github.com/datarhei/core/tree/cluster))*


-   `GET` /api/v3/cluster

    ```python
    v3_cluster_get_list()
    ```

-   `POST` /api/v3/cluster/node/
    ```python
    v3_cluster_post_node(node: ClusterNodeAuth)
    ```
    *Model: [ClusterNodeAuth](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/cluster_node_auth.py)*

-   `GET` /api/v3/cluster/node/{id}
    ```python
    v3_cluster_get_node(id: str)
    ```

-   `PUT` /api/v3/cluster/node/{id}
    ```python
    v3_cluster_put_node(id: str, node: ClusterNodeAuth)
    ```
    *Model: [ClusterNodeAuth](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/cluster_node_auth.py)*


-   `DELETE` /api/v3/cluster/node/{id}
    ```python
    v3_cluster_delete_node(id: str)
    ```

-   `GET` /api/v3/cluster/node/{id}/proxy
    ```python
    v3_cluster_get_node_proxy(id: str)
    ```

### Config

-   `GET` /api/v3/config

    ```python
    v3_config_get()
    ```

-   `PUT` /api/v3/config
    ```python
    v3_config_put(config: Config)
    ```
    *Model: [Config](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/config.py)*

-   `GET` /api/v3/config/reload
    ```python
    v3_config_reload()
    ```

### Filesystem

-   `GET` /api/v3/fs

    ```python
    v3_fs_get_list()
    ```

-   `GET` /api/v3/fs/{name}
    ```python
    v3_fs_get_file_list(name=str, glob: str = "", sort: str = "", order: str = "")
    ```

-   `GET` /api/v3/fs/{name}/{path}
    ```python
    v3_fs_get_file(name: str, path: str)
    ```

-   `PUT` /api/v3/fs/{name}/{path}
    ```python
    v3_fs_put_file(name: str, path: str, data: bytes)
    ```

-   `DELETE` /api/v3/fs/{name}/{path}
    ```python
    v3_fs_delete_file(name: str, path: str)
    ```

### Log

-   `GET` /api/v3/log

    ```python
    v3_log_get(format: str = "console")
    ```

### Metadata

-   `GET` /api/v3/metadata/{key}

    ```python
    v3_metadata_get(key: str)
    ```

-   `PUT` /api/v3/metadata/{key}
    ```python
    v3_metadata_put(key: str, data: Metadata)
    ```
    *Model: [Metadata](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/metadata.py)*

### Metrics

-   `GET` /api/v3/metrics

    ```python
    v3_metrics_get()
    ```

-   `POST` /api/v3/metrics

    ```python
    v3_metrics_post(config: Metrics)
    ```
    *Model: [Metrics](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/metrics.py)*

### Process

-   `GET` /api/v3/process

    ```python
    v3_process_get_list(filter: str = "", reference: str = "", id: str = "", idpattern: str = "", refpattern: str = "")
    ```

-   `POST` /api/v3/process
    ```python
    v3_process_post(config: ProcessConfig)
    ```
    *Model: [ProcessConfig](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/process_config.py)*

-   `GET` /api/v3/process/{id}
    ```python
    v3_process_get(id: str, filter: str = "")
    ```

-   `PUT` /api/v3/process/{id}
    ```python
    v3_process_put(id: str, config: ProcessConfig)
    ```
    *Model: [ProcessConfig](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/process_config.py)*

-   `DELETE` /api/v3/process/{id}
    ```python
    v3_process_delete(id: str)
    ```

-   `PUT` /api/v3/process/{id}/command
    ```python
    v3_process_put_command(id: str, command: ProcessCommand)
    ```
    *Model: [ProcessCommand](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/process_command.py)*

-   `GET` /api/v3/process/{id}/config
    ```python
    v3_process_get_config(id: str)
    ```

-   `GET` /api/v3/process/{id}/metadata/{key}
    ```python
    v3_process_get_metadata(id: str, key: str)
    ```

-   `PUT` /api/v3/process/{id}/metadata/{key}
    ```python
    v3_process_put_metadata(id: str, key: str, data: Metadata)
    ```
    *Model: [Metadata](https://github.com/datarhei/core-client-python/blob/main/core_client/base/models/v3/metadata.py)*

-   `GET` /api/v3/process/{id}/probe
    ```python
    v3_process_get_probe(id: str)
    ```

-   `GET` /api/v3/process/{id}/report
    ```python
    v3_process_get_report(id: str)
    ```

-   `GET` /api/v3/process/{id}/state
    ```python
    v3_process_get_state(id: str)
    ```

### Process Playout (commercial extention)

-   `GET` /api/v3/process/{id}/playout/{input_id}/errorframe/encode

    ```python
    v3_process_get_playout_input_errorframe_encode(id: str, input_id: str)
    ```

-   `POST` /api/v3/process/{id}/playout/{input_id}/errorframe/{input_name}
    ```python
    v3_process_post_playout_input_errorframe_name(id: str, input_id: str, input_name: str)
    ```

-   `GET` /api/v3/process/{id}/playout/{input_id}/keyframe/{input_name}
    ```python
    v3_process_get_playout_input_keyframe(id: str, input_id: str, input_name: str)
    ```

-   `GET` /api/v3/process/{id}/playout/{input_id}/reopen
    ```python
    v3_process_get_playout_input_reopen(id: str, input_id: str)
    ```

-   `GET` /api/v3/process/{id}/playout/{input_id}/status
    ```python
    v3_process_get_playout_input_status(id: str, input_id: str)
    ```

-   `PUT` /api/v3/process/{id}/playout/{input_id}/stream
    ```python
    v3_process_put_playout_input_stream(id: str, input_id: str)
    ```

### RTMP

-   `GET` /api/v3/rtmp

    ```python
    v3_rtmp_get()
    ```

### Session

-   `GET` /api/v3/session

    ```python
    v3_session_get(collectors: str)
    ```

-   `GET` /api/v3/session/active
    ```python
    v3_session_get_active(collectors: str)
    ```

### Skills

-   `GET` /api/v3/skills

    ```python
    v3_skills_get()
    ```

-   `GET` /api/v3/skills/reload
    ```python
    v3_skills_reload()
    ```

### SRT

-   `GET` /api/v3/srt

    ```python
    v3_srt_get()
    ```

### Widget

-   `GET` /api/v3/widget/process/{id}

    ```python
    v3_widget_get_process(id: str)
    ```

### Misc

- `GET` /ping

  ```python
  ping()
  ```

Additional options per request:
- `retries: int = default of class`
- `timeout: float = default of class`

## Examples

### GET token data

```python
from core_client import Client

client = Client(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")

token = client.login()
print(token)
```

### GET processes

```python
from core_client import Client

client = Client(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")
client.login()

process_list = client.v3_process_get_list()
for process in processes:
    print(process.id)
```

### POST process

```python
from core_client import Client

client = Client(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")
client.login()

process_example = {
    "id": "my_proc",
    "reference": "my_ref",
    "input": [
        {
            "address": "testsrc=size=1280x720:rate=25",
            "id": "input_0",
            "options": ["-f", "lavfi", "-re"],
        }
    ],
    "options": ["-loglevel", "info"],
    "output": [
        {
            "address": "-",
            "id": "output_0",
            "options": ["-codec:v", "libx264", "-r", "25", "-f", "null"]
        }
    ]
}

post_process = client.v3_process_post(config=process_example)
print(post_process)
```

### GET process

```python
from core_client import Client

client = Client(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")
client.login()

get_process = client.v3_process_get(id="my_proc")
print(get_process)
```

### PUT process

```python
from core_client import Client

client = Client(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")
client.login()

process_example = {
    "id": "my_proc",
    "reference": "my_ref",
    "input": [
        {
            "address": "testsrc=size=1280x720:rate=25",
            "id": "input_0",
            "options": ["-f", "lavfi", "-re"],
        }
    ],
    "options": ["-loglevel", "debug"],
    "output": [
        {
            "address": "-",
            "id": "output_0",
            "options": ["-codec:v", "libx264", "-r", "25", "-f", "null"]
        }
    ]
}

put_process = client.v3_process_put(id="testproc", config=process_example)
print(put_process)
```

### DELETE process

```python
from core_client import Client

client = Client(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")
client.login()

delete_process = client.v3_process_delete(id="testproc")
print(delete_process)
```

## API models

Models are located here:
-   `core_client/base/models/`
-   `core_client/base/models/v3`

```python
from core_client import Client
from core_client.base.models.v3 import ProcessConfig, ProcessConfigIO

client = Client(base_url="http://127.0.0.1:8080", username="admin", password="datarhei")
client.login()

put_process = client.v3_process_put(id="my_proc", config=ProcessConfig(
    id="my_proc",
    reference="my_ref",
    input=[
        ProcessConfigIO(
            address="testsrc2=rate=25:size=1280x720",
            id="input_0",
            options=["-re", "-f", "lavfi"]
        )
    ],
    options=["-loglevel", "error"],
    output=[
        ProcessConfigIO(
            address="-",
            id="output_0",
            options=["-codec:v", "libx264", "-r", "25", "-f", "null"]
        )
    ]
))
print(put_process)
```

### Pydantic model exports:
-   `model.dict()` exports model to dict
-   `model.json()` exports model to json

### Pydantic parse object as model:
-   `parse_obj_as(ModelName, obj)`
-   `ModelName.parse_obj(obj)`
-   `ModelName(**obj)`

More details and options in the [pydantic docs](https://pydantic-docs.helpmanual.io/usage/models/#model-properties).

## Error handling
`raise_for_status()` is unused, but the exceptions are still available:

```python
try:
    process = client.v3_process_get_list()
except httpx.HTTPError as exc:
    print(f"Error while requesting {exc.request.url!r}.")
```

More in the [HTTPX docs](https://www.python-httpx.org/exceptions/).

## Developing & testing

### Clone

```sh
$ git clone datarhei/core-client-python
$ cd core-client-python && \
    pip install -r requirements-dev.txt
```

### Testing

#### Start a [Core](https://github.com/datarhei/core) backend:
```sh
$ docker run -d --name core -p 8080:8080 datarhei/core:latest
```

#### Local
```sh
$ CORE_URL=http://127.0.0.1:8080 \
    pytest tests/*.py
```
*Use `coverage html` to create an html report.*

#### Docker
```sh
$ docker build --build-arg PYTHON_VERSION=3.7 \
    -f tests/Dockerfile -t core_test .

$ docker run -it --rm \
    -e CORE_URL=http://192.168.1.1:8080 core_test
```
*Notice: 127.0.0.1 is the container itself.*

### Code checks

```sh
$ pre-commit run --all-files
```
*Requires `pip install pre-commit`.*

## Changelog

[Changelog](https://github.com/datarhei/core-client-python/blob/main/CHANGELOG.md)

## Contributing

Found a mistake or misconduct? Create a [issue](https://github.com/datarhei/core-client-python/issues) or send a pull-request.
Suggestions for improvement are welcome.

## Licence

[MIT](https://github.com/datarhei/core-client-python/blob/main/LICENSE)
