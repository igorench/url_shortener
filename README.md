Development server
Set environment variables
cp .env.example .env

Build docker
docker-compose build

Run python migrations
docker-compose run server python manage.py migrate

Run docker
docker-compose up

Create superuser
docker-compose run server python manage.py createsuperuser
