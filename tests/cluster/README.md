### Cluster testing

#### Start a [Core](https://github.com/datarhei/core) backend:
```sh
$ docker run -d --name core_1 -p 8080:8080 datarhei/core:latest
$ docker run -d --name core_2 -p 8081:8080 datarhei/core:latest
```

#### Local
```sh
$ CORE_URL_1=http://127.0.0.1:8080 \
    CORE_URL_2=http://127.0.0.1:8081 \
    pytest tests/cluster/*.py
```
