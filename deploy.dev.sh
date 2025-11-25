set -e
set -a
source ./backend/.env.dev
set +a

echo "STEP ONE ::: BUILD DOCKER IMAGES"
docker-compose -f docker-compose.dev.yml build

echo "STEP TWO ::: START CONTAINERS"
docker-compose -f docker-compose.dev.yml up -d

echo "STEP THREE ::: DATABASE MIGRATION"
docker-compose -f docker-compose.dev.yml exec backend python manage.py makemigrations --noinput
docker-compose -f docker-compose.dev.yml exec backend python manage.py migrate --noinput

echo "STEP FOUR ::: COLLECT STATIC FILES"
docker-compose -f docker-compose.dev.yml exec backend python manage.py collectstatic --noinput

echo "STEP FIVE ::: CREATE SUPERUSER"
docker-compose -f docker-compose.dev.yml exec backend python -c "
import os
from django.conf import settings

# Set DJANGO_SETTINGS_MODULE to your settings if not already set
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()
username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'strongpassword')

try:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            password=password
        )
        print('SUPERUSER CREATED SUCCESSFULLY!')
    else:
        print('SUPERUSER ALREADY EXISTS.')
except IntegrityError:
    print('ERROR CREATING SUPERUSER.')
"

echo "STEP SIX ::: UN-USED CLEAN UP DOCKER"
docker system prune -f

echo "DEVELOPMENT PROJECT RUN SUCCESSFULLY"
