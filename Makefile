# Fantasy Soccer App - Makefile
.PHONY: help setup build up down logs init-db import-data run test clean

# Default target
help:
	@echo "Fantasy Soccer App - Available commands:"
	@echo "  setup        - Complete setup (build + up + init-db + import-data)"
	@echo "  build        - Build Docker images"
	@echo "  up           - Start containers"
	@echo "  down         - Stop and remove containers"
	@echo "  logs         - View container logs"
	@echo "  init-db      - Initialize database and create admin user (inside container)"
	@echo "  import-data  - Import EPL clubs and players data (inside container)"
	@echo "  run          - Run the development server (if not using Docker CMD)"
	@echo "  test         - Run tests (inside container)"
	@echo "  clean        - Clean Python cache files"

# Complete setup: build images, start containers, init DB, import data
setup: build up init-db import-data
	@echo "Setup complete! Run 'make logs' to view logs or 'make down' to stop containers."

# Build Docker images and start containers in background
default: build

build:
	docker-compose up --build -d

up:
	docker-compose up -d

down:
	docker-compose down -v

logs:
	docker-compose logs -f

init-db:
	docker-compose exec web python3 scripts/init_db.py

import-data:
	docker-compose exec web python3 scripts/import_data.py

# Run development server (if not using Docker CMD)
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	docker-compose exec web pytest

# Clean Python cache
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# migrate:
# 	docker-compose exec web alembic upgrade head