up:
	docker-compose up

build:
	docker-compose up --build

down:
	docker-compose down

logs:
	docker-compose logs -f

# migrate:
# 	docker-compose exec web alembic upgrade head