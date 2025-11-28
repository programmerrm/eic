# set -e
# set -a
# source ./backend/.env.prod
# set +a

# echo "STEP ONE ::: UN-USED CLEAN UP DOCKER"
# docker system prune -f

# echo "STEP TWO ::: BUILD DOCKER IMAGES"
# docker-compose -f docker-compose.prod.yml build

# echo "STEP THREE ::: START CONTAINERS"
# docker-compose -f docker-compose.prod.yml up -d

# echo "STEP FOUR ::: DATABASE MIGRATION"
# docker-compose -f docker-compose.prod.yml exec backend python manage.py makemigrations --noinput
# docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate --noinput

# echo "STEP FIVE ::: COLLECT STATIC FILES"
# docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput

# echo "STEP SIX ::: CREATE SUPERUSER"
# docker-compose -f docker-compose.prod.yml exec backend python -c "
#     from django.contrib.auth import get_user_model
#     from django.db.utils import IntegrityError
#     User = get_user_model()
#     email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'info@eic.com.bd')
#     username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
#     password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'strongpassword')
#     try:
#         if not User.objects.filter(username=username).exists():
#             User.objects.create_superuser(
#                 email=email,
#                 username=username,
#                 password=password
#             )
#             print('SUPERUSER CREATED SUCCESSFULLY!')
#         else:
#             print('SUPERUSER ALREADY EXISTS.')
#     except IntegrityError:
#         print('ERROR CREATING SUPERUSER.')
# "

# echo "STEP SEVEN ::: NGINX CONFIGARATION"
# docker-compose -f docker-compose.prod.yml exec nginx nginx -t

# echo "STEP EIGHT ::: RELOAD NGINX"
# docker-compose -f docker-compose.prod.yml exec -s reload

# echo "PRODUCTION PROJECT RUN SUCCESSFULLY"


#!/bin/bash
set -e   # Exit immediately if a command exits with a non-zero status
set -a   # Export all variables
source ./backend/.env.prod
set +a

echo "STEP 1 ::: CLEANUP UNUSED DOCKER RESOURCES"
docker system prune -f

echo "STEP 2 ::: BUILD DOCKER IMAGES"
docker-compose -f docker-compose.prod.yml build

echo "STEP 3 ::: START CONTAINERS"
docker-compose -f docker-compose.prod.yml up -d

echo "STEP 4 ::: DATABASE MIGRATIONS"
docker-compose -f docker-compose.prod.yml exec backend python manage.py makemigrations --noinput
docker-compose -f docker-compose.prod.yml exec backend python manage.py migrate --noinput

echo "STEP 5 ::: COLLECT STATIC FILES"
docker-compose -f docker-compose.prod.yml exec backend python manage.py collectstatic --noinput

echo "STEP 6 ::: CREATE SUPERUSER"
docker-compose -f docker-compose.prod.yml exec backend python -c "
import os
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'info@eic.com.bd')
username = os.getenv('SUPERUSER_USERNAME', 'eicadmin')
password = os.getenv('SUPERUSER_PASSWORD', 'strongpassword123')

try:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(email=email, username=username, password=password)
        print('SUPERUSER CREATED SUCCESSFULLY!')
    else:
        print('SUPERUSER ALREADY EXISTS.')
except IntegrityError:
    print('ERROR CREATING SUPERUSER.')
"

echo "STEP 7 ::: NGINX CONFIGURATION CHECK"
docker-compose -f docker-compose.prod.yml exec nginx nginx -t

echo "STEP 8 ::: RELOAD NGINX"
docker-compose -f docker-compose.prod.yml exec nginx nginx -s reload

echo "✅ PRODUCTION DEPLOY COMPLETED SUCCESSFULLY!"
