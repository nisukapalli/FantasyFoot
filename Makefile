up:
	docker-compose up --build

down:
	docker-compose down

logs:
	docker-compose logs -f

test-db:
	docker-compose exec web python -m app.test_db

# migrate:
# 	docker-compose exec web alembic upgrade head