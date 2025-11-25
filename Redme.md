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