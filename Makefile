.PHONY: help watch up down migrate makemigrations shell test logs

help:
	@echo "Available commands:"
	@echo "  make watch          - Watch all services"
	@echo "  make up             - Start all services"
	@echo "  make down           - Stop all services"
	@echo "  make migrate        - Run database migrations"
	@echo "  make makemigrations - Create new database migrations"
	@echo "  make shell          - Open Django shell"
	@echo "  make test           - Run tests"
	@echo "  make logs           - Show logs"

watch:
	docker compose watch

up:
	docker compose up -d

down:
	docker compose down

migrate:
	docker compose exec server python manage.py migrate

makemigrations:
	docker compose exec server python manage.py makemigrations

shell:
	docker compose exec server python manage.py shell

test:
	docker compose exec server pytest

logs:
	docker compose logs -f server