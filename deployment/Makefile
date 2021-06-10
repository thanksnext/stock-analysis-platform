init:
	pip install pipenv --upgrade
	cd ../finance;\
	pipenv install --dev --pre;\
	pipenv run pre-commit install
start:
	docker-compose up --build -d
	docker image prune -f

stop:
	docker-compose down
	docker volume prune -f

build:
	docker-compose build
	docker image prune -f


ssh-backend:
	docker exec -it stock-backend bash

ssh-database:
	docker exec -it stock-db bash
