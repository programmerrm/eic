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


# ================= BACKEND =================
server {
    listen 80;
    server_name eicsec.com www.eicsec.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name eicsec.com www.eicsec.com;

    client_max_body_size 200M;
    large_client_header_buffers 4 32k;

    ssl_certificate /etc/letsencrypt/live/eicsec.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/eicsec.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;

    # ================= SECURITY HEADERS =================
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;

    # ================= MEDIA / STATIC =================
    location /static/ {
        alias /backend/staticfiles/;
    }

    location /media/ {
        alias /backend/media/;
        add_header Access-Control-Allow-Origin https://eic.com.bd;
        add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
        add_header Access-Control-Allow-Headers "Authorization,Content-Type";
    }

    location / {
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;

        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 300;
        proxy_send_timeout 300;
        proxy_read_timeout 300;
        send_timeout 300;
    }
}

# ================= FRONTEND =================
server {
    listen 80;
    server_name eic.com.bd www.eic.com.bd;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;

    server_name eic.com.bd www.eic.com.bd;

    large_client_header_buffers 4 32k;

    ssl_certificate /etc/letsencrypt/live/eic.com.bd/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/eic.com.bd/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    ssl_session_cache shared:SSL:10m;

    # ================= SECURITY HEADERS =================
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "no-referrer-when-downgrade" always;
    add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;

    #  ========== CSP - only frontend + backend domains allowed ========
    add_header Content-Security-Policy "
        default-src 'self';
        script-src 'self' 'unsafe-inline';
        style-src 'self' 'unsafe-inline';
        img-src 'self' https://eicsec.com https://eic.com.bd data:;
        font-src 'self';
        connect-src 'self' https://eicsec.com https://eic.com.bd;
        frame-ancestors 'self';
    " always;

    # ================= END SECURITY HEADERS =================
    location / {
        proxy_buffer_size 128k;
        proxy_buffers 4 256k;
        proxy_busy_buffers_size 256k;

        proxy_pass http://frontend:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;

        proxy_connect_timeout 300;
        proxy_send_timeout 300;
        proxy_read_timeout 300;
        send_timeout 300;
    }
}
