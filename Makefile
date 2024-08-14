run_processes:
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

reload_reqs:
	poetry export -f requirements.txt --output ./.devcontainer/requirements.txt --without-hashes