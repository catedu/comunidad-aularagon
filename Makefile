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

up:
	docker-compose -f docker-compose.local.yml up -d
	docker run --rm -p 6379:6379 --name another-redis -d redis
	python manage.py runserver

redis_worker:
	celery -A project_conf worker -l INFO

redis_beat:
	celery -A project_conf beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler