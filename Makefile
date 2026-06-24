.PHONY: default help clean-pyc clean-dist clean test test-unit test-integration test-all \
	core-up core-down core-logs dist release lint

# --- configuration (override on the command line, e.g. `make test-integration CORE_PORT=8080`) ---
PYTEST         ?= pytest
CORE_IMAGE     ?= datarhei/core:latest
CORE_CONTAINER ?= core-client-test
CORE_PORT      ?= 8088
CORE_URL       ?= http://127.0.0.1:$(CORE_PORT)

default: test

help:
	@echo "Targets:"
	@echo "  test              Run unit tests (no backend required)"
	@echo "  test-integration  Start a fresh Core via Docker, run integration tests, tear it down"
	@echo "  test-all          Run unit tests, then the dockerized integration tests"
	@echo "  core-up           Start a fresh Core container ($(CORE_CONTAINER)) on port $(CORE_PORT)"
	@echo "  core-down         Stop and remove the Core container"
	@echo "  core-logs         Follow the Core container logs"
	@echo "  lint              Run ruff and pre-commit"
	@echo "  clean             Remove build/cache artifacts"
	@echo ""
	@echo "Config (current): CORE_IMAGE=$(CORE_IMAGE) CORE_CONTAINER=$(CORE_CONTAINER) CORE_URL=$(CORE_URL)"

clean-pyc:
	@find . -iname '*.py[co]' -delete
	@find . -iname '__pycache__' -delete
	@find . -iname '.coverage' -delete
	@rm -rf htmlcov/

clean-dist:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info

clean: clean-pyc clean-dist

# --- tests ------------------------------------------------------------------
test: test-unit

test-unit:
	$(PYTEST) -vvv --cov=core_client tests/unit

# Starts a fresh Core, runs the integration suite against it, and always tears
# the container down afterwards (even if the tests fail or startup hangs).
test-integration:
	@set -e; \
	trap '$(MAKE) --no-print-directory core-down' EXIT; \
	$(MAKE) --no-print-directory core-up; \
	RUN_INTEGRATION_TESTS=1 CORE_URL=$(CORE_URL) $(PYTEST) -vvv tests/integration

test-all: test-unit test-integration

# --- dockerized Core lifecycle ---------------------------------------------
core-up:
	@docker rm -f $(CORE_CONTAINER) >/dev/null 2>&1 || true
	@echo ">> starting $(CORE_IMAGE) as '$(CORE_CONTAINER)' on port $(CORE_PORT)"
	@docker run -d --name $(CORE_CONTAINER) -p $(CORE_PORT):8080 $(CORE_IMAGE) >/dev/null
	@echo ">> waiting for Core to become ready at $(CORE_URL)/ping"
	@for i in $$(seq 1 60); do \
		if curl -fsS $(CORE_URL)/ping >/dev/null 2>&1; then \
			echo ">> Core is ready"; \
			exit 0; \
		fi; \
		sleep 1; \
	done; \
	echo ">> Core did not become ready in time" >&2; \
	docker logs $(CORE_CONTAINER) >&2 || true; \
	exit 1

core-down:
	@echo ">> removing '$(CORE_CONTAINER)'"
	@docker rm -f $(CORE_CONTAINER) >/dev/null 2>&1 || true

core-logs:
	@docker logs -f $(CORE_CONTAINER)

# --- packaging --------------------------------------------------------------
dist: clean
	python setup.py sdist
	python setup.py bdist_wheel

release: dist
	git tag `python setup.py -q version`
	git push origin `python setup.py -q version`
	twine upload dist/*

lint:
	ruff check .
	SKIP=no-commit-to-branch pre-commit run -a -v
