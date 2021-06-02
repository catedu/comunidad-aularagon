migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver
	
shell:	
	python manage.py shell_plus

dcup_local:
	docker-compose -f docker-compose.local.yml up

dcup_local_build:
	docker-compose -f docker-compose.local.yml up --build

dcup_all:
	docker-compose up