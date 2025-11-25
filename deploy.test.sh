set -e
set -a
source ./backend/.env.test
set +a

echo "STEP ONE ::: UN-USED CLEAN UP DOCKER"
docker system prune -f

echo "STEP TWO ::: BUILD DOCKER IMAGES"
docker-compose -f docker-compose.test.yml build

echo "STEP THREE ::: START CONTAINERS"
docker-compose -f docker-compose.test.yml up -d

echo "STEP FOUR ::: DATABASE MIGRATION"
docker-compose -f docker-compose.test.yml exec backend python manage.py makemigrations --noinput
docker-compose -f docker-compose.test.yml exec backend python manage.py migrate --noinput

echo "STEP FIVE ::: COLLECT STATIC FILES"
docker-compose -f docker-compose.test.yml exec backend python manage.py collectstatic --noinput

echo "STEP SIX ::: CREATE SUPERUSER"
docker-compose -f docker-compose.test.yml exec backend python -c "
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

echo "STEP SEVEN ::: NGINX CONFIGARATION"
docker-compose -f docker-compose.test.yml exec nginx nginx -t

echo "STEP EIGHT ::: RELOAD NGINX"
docker-compose -f docker-compose.test.yml exec -s reload

echo "TEST PROJECT RUN SUCCESSFULLY"
