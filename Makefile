dev:
	docker-compose up

migrate:
	docker-compose exec app poetry run python migrations/

seed-db:
	docker-compose exec app poetry run python seed/
