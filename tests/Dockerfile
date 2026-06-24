ARG PYTHON_VERSION=3.11

FROM python:${PYTHON_VERSION}-alpine

COPY . /client
WORKDIR /client

RUN pip install -r requirements-dev.txt

ENV CORE_URL=""
ENV RUN_INTEGRATION_TESTS="1"

CMD ["pytest", "tests/unit", "tests/integration"]
