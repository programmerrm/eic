#!/bin/bash
set -e
set -a
source ./backend/.env.prod
set +a

echo "STEP 1 ::: CLEAN UP UNUSED DOCKER RESOURCES"
docker system prune -f

echo "STEP 2 ::: START REDIS"
docker-compose -f docker-compose.prod.yml up -d redis

echo "Waiting for Redis to be healthy..."
until [ "$(docker inspect --format='{{.State.Health.Status}}' redis_server)" = "healthy" ]; do
    sleep 2
done
echo "Redis is healthy ✅"

echo "STEP 3 ::: START BACKEND"
docker-compose -f docker-compose.prod.yml up -d backend

echo "Waiting for Backend to be ready..."
until docker-compose -f docker-compose.prod.yml exec backend nc -z localhost 8000; do
    sleep 2
done
echo "Backend is ready ✅"

echo "STEP 4 ::: DATABASE MIGRATION"


echo "STEP 5 ::: COLLECT STATIC FILES"
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput

echo "STEP 6 ::: BUILD FRONTEND"
docker-compose -f docker-compose.prod.yml build frontend

echo "STEP 7 ::: START FRONTEND"
docker-compose -f docker-compose.prod.yml up -d frontend

echo "STEP 8 ::: VALIDATE NGINX CONFIGURATION"
docker-compose -f docker-compose.prod.yml exec nginx nginx -t

echo "STEP 9 ::: RELOAD NGINX"
docker-compose -f docker-compose.prod.yml exec nginx nginx -s reload

echo "PRODUCTION PROJECT RUN SUCCESSFULLY ✅"
