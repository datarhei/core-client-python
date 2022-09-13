ARG PYTHON_VERSION=3.7

FROM python:${PYTHON_VERSION}-alpine

COPY . /client
WORKDIR /client

RUN pip install -r requirements-dev.txt

ENV CORE_URL=""

CMD ["pytest", "tests/1_pre.py", "tests/2_protected.py", "tests/3_main.py", "tests/4_errors.py", "tests/5_post.py"]
