OS := $(shell uname -s)

# Set path separator and commands based on the OS
ifeq ($(OS),Windows_NT)
    SEP := \\
    PY := python
else
    SEP := /
    PY := python3
endif


run_infra:
	docker compose -f "docker-compose.db.yml" down
	docker compose -f "docker-compose.db.yml" up -d
	docker compose -f "docker-compose.etl.yml" down
	docker compose -f "docker-compose.etl.yml" up

run_db:
	docker compose -f "docker-compose.db.yml" down
	docker compose -f "docker-compose.db.yml" up -d

run_etl:
	docker compose -f "docker-compose.etl.yml" down
	docker compose -f "docker-compose.etl.yml" up -d

clean_infra:
	docker compose -f "docker-compose.db.yml" down
	docker compose -f "docker-compose.etl.yml" down

reload_reqs:
	poetry export -f requirements.txt --output .$(SEP).devcontainer$(SEP)requirements.txt --without-hashes

test_py_setup:
	poetry run python src$(SEP)00_setup_db.py

test_py_ingest:
	poetry run python src$(SEP)01_ingest.py

test_py_transform:
	poetry run python src$(SEP)02_transform.py