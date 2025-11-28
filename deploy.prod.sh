#!/bin/bash
set -e
set -a
source ./backend/.env.prod
set +a

echo "STEP ONE ::: CLEAN UP UNUSED DOCKER RESOURCES"
# Optional, সাবধানে ব্যবহার করো
# docker system prune -f

echo "STEP TWO ::: BUILD DOCKER IMAGES"
docker-compose -f docker-compose.prod.yml build

echo "STEP THREE ::: START CONTAINERS"
docker-compose -f docker-compose.prod.yml up -d

echo "STEP FOUR ::: DATABASE MIGRATION"
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate --noinput

echo "STEP FIVE ::: COLLECT STATIC FILES"
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput

echo "STEP SIX ::: CREATE DJANGO SUPERUSER IF NOT EXISTS"
docker-compose -f docker-compose.prod.yml exec -T backend python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()

email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'info@eic.com.bd')
username = os.getenv('SUPERUSER_USERNAME', 'eicadmin')
password = os.getenv('SUPERUSER_PASSWORD', 'StrongPass123!')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(email=email, username=username, password=password)
    print('SUPERUSER CREATED SUCCESSFULLY!')
else:
    print('SUPERUSER ALREADY EXISTS.')
"

echo "STEP SEVEN ::: NGINX CONFIGURATION TEST"
docker-compose -f docker-compose.prod.yml exec nginx nginx -t

echo "STEP EIGHT ::: RELOAD NGINX"
docker-compose -f docker-compose.prod.yml exec nginx nginx -s reload

echo "PRODUCTION PROJECT DEPLOYED SUCCESSFULLY"
