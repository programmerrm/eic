############################ DEV RASEL GITHUB BRANCH ##############################
============ THIS BRANCHING MY LATEST ALL UPDATED CODE AND DATA SHEREING ==========

# ======= START WORKING DATE 10/24/2025 7:05 PM ==================

# 1.TASK --->>> BACKEND PROJECT SETUP

DOCKER COMMOND
Start containers
docker-compose -f docker-compose.dev.yml up -d

1. Make migrations
docker-compose -f docker-compose.dev.yml exec backend python manage.py makemigrations configuration

2. Apply migrations
docker-compose -f docker-compose.dev.yml exec backend python manage.py migrate

3. Create superuser
docker-compose -f docker-compose.dev.yml exec backend python manage.py createsuperuser

RUN COMMOND
docker-compose -f docker-compose.dev.yml up --build docker-compose -f docker-compose.dev.yml down docker-compose -f docker-compose.prod.yml up --build docker-compose -f docker-compose.prod.yml down

docker-compose -f docker-compose.prod.yml restart nginx
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput
docker-compose -f docker-compose.prod.yml exec backend python manage.py shell -c "from django.conf import settings; print('BASE_DIR=', settings.BASE_DIR); print('STATIC_ROOT=', settings.STATIC_ROOT)"


cd /var/apps/eic

sudo find backend/staticfiles -type d -exec chmod 755 {} \;
sudo find backend/staticfiles -type f -exec chmod 644 {} \;
sudo find backend/media -type d -exec chmod 755 {} \;
sudo find backend/media -type f -exec chmod 644 {} \;