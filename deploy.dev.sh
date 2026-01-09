set -e
set -a
source ./backend/.env.dev
set +a

echo "STEP ONE ::: BUILD DOCKER IMAGES"
docker compose -f docker-compose.dev.yml build

echo "STEP TWO ::: START CONTAINERS"
docker compose -f docker-compose.dev.yml up -d

echo "STEP THREE ::: DATABASE MIGRATION"
docker compose -f docker-compose.dev.yml exec backend python manage.py makemigrations --noinput
docker compose -f docker-compose.dev.yml exec backend python manage.py migrate --noinput

echo "STEP FOUR ::: COLLECT STATIC FILES"
docker compose -f docker-compose.dev.yml exec backend python manage.py collectstatic --noinput

echo "STEP SIX ::: UN-USED CLEAN UP DOCKER"
docker system prune -f

echo "DEVELOPMENT PROJECT RUN SUCCESSFULLY"
