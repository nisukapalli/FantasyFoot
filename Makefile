.PHONY: install run test clean init-db import-data help

# Default target
help:
	@echo "Fantasy Soccer App - Available commands:"
	@echo "  install      - Install Python dependencies"
	@echo "  run          - Run the development server"
	@echo "  test         - Run tests"
	@echo "  clean        - Clean Python cache files"
	@echo "  init-db      - Initialize database and create admin user"
	@echo "  import-data  - Import EPL clubs and players data"
	@echo "  setup        - Complete setup (install + init-db + import-data)"

# Install dependencies
install:
	pip install -r requirements.txt

# Run development server
run:
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Run tests
test:
	pytest

# Clean Python cache
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Initialize database
init-db:
	python3 scripts/init_db.py

# Import EPL data
import-data:
	python3 scripts/import_data.py

# Complete setup
setup: install init-db import-data
	@echo "Setup complete! Run 'make run' to start the server."

up:
	docker-compose up -d

build:
	docker-compose up --build -d

down:
	docker-compose down -v

logs:
	docker-compose logs -f

# migrate:
# 	docker-compose exec web alembic upgrade head