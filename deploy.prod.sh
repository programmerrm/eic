#!/bin/bash
set -e
set -a
source ./backend/.env.prod
set +a

echo "STEP 1 ::: CLEAN UP UNUSED DOCKER RESOURCES"
docker system prune -f

# ---------------- REDIS ----------------
echo "STEP 2 ::: START REDIS"
docker-compose -f docker-compose.prod.yml up -d redis

echo "Waiting for Redis to be healthy..."
until [ "$(docker inspect --format='{{.State.Health.Status}}' redis_server)" = "healthy" ]; do
    sleep 2
done
echo "Redis is healthy ✅"

# ---------------- BACKEND ----------------
echo "STEP 3 ::: START BACKEND"
docker-compose -f docker-compose.prod.yml up -d backend
echo "Waiting for Backend to be ready..."
until docker-compose -f docker-compose.prod.yml exec -T backend nc -z localhost 8000; do
    sleep 2
done
echo "Backend is ready ✅"

# ---------------- NGINX RESTART AFTER BACKEND 
echo "STEP 4 ::: RESTART NGINX after Backend is ready"
docker-compose -f docker-compose.prod.yml up -d nginx
docker-compose -f docker-compose.prod.yml exec nginx nginx -t
docker-compose -f docker-compose.prod.yml exec nginx nginx -s reload
echo "Nginx restarted ✅"

# ---------------- DATABASE MIGRATION ----------------
echo "STEP 5 ::: DATABASE MIGRATION"
docker-compose -f docker-compose.prod.yml exec -T backend python manage.py makemigrations --noinput
docker-compose -f docker-compose.prod.yml exec -T backend python manage.py migrate --noinput
echo "Backend database ready ✅"

# ---------------- COLLECT STATIC ----------------
echo "STEP 6 ::: COLLECT STATIC FILES"
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput

# ---------------- FRONTEND ----------------
echo "STEP 7 ::: BUILD FRONTEND"
docker-compose -f docker-compose.prod.yml build frontend
echo "STEP 8 ::: START FRONTEND"
docker-compose -f docker-compose.prod.yml up -d frontend

# ---------------- NGINX RELOAD AFTER FRONTEND
echo "STEP 9 ::: RELOAD NGINX after Frontend is ready"
docker-compose -f docker-compose.prod.yml exec nginx nginx -t
docker-compose -f docker-compose.prod.yml exec nginx nginx -s reload

echo "PRODUCTION PROJECT RUN SUCCESSFULLY ✅"
