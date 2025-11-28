#!/bin/bash
set -e
set -a
source ./backend/.env.prod
set +a

echo "STEP ONE ::: CLEAN UP UNUSED DOCKER RESOURCES"
docker system prune -f

echo "STEP TWO ::: BUILD DOCKER IMAGES"
docker-compose -f docker-compose.prod.yml build

echo "STEP THREE ::: START CONTAINERS"
docker-compose -f docker-compose.prod.yml up -d

echo "STEP FOUR ::: DATABASE MIGRATION"
docker-compose -f docker-compose.prod.yml exec backend python manage.py makemigrations --noinput
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate --noinput

echo "STEP FIVE ::: COLLECT STATIC FILES"
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput

echo "STEP SIX ::: CREATE DJANGO SUPERUSER IF NOT EXISTS"
docker-compose -f docker-compose.prod.yml exec nginx nginx -t

echo "STEP EIGHT ::: RELOAD NGINX"
docker-compose -f docker-compose.prod.yml exec nginx nginx -s reload

echo "PRODUCTION PROJECT RUN SUCCESSFULLY"
