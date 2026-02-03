#########################################################
"""
Production settings configuration
"""
#########################################################
from app.settings.base import *

# BASE CONFIGRATION
DEBUG = False
ALLOWED_HOSTS = [
    'eic.com.bd',
    'www.eic.com.bd',
    'eicsec.com',
    'www.eicsec.com',
    'localhost',
    '127.0.0.1',
    '51.79.35.178',
]

SECRET_KEY = 'django-insecure--j7#f^zo#_&rlptdsq0ut#8)cdnocjkb=$7*=(vyc4z%5zizum'

# MIDDLEWARE
MIDDLEWARE.insert(
    MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
    'app.middleware.DomainAndAdminMiddleware'
)

# DATABASE CONFIGRATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT"),
    }
}

# CSRF TRUSTED ORIGINS
CSRF_TRUSTED_ORIGINS = [
    'https://eic.com.bd',
    'https://www.eic.com.bd',
    'https://eicsec.com',
    'https://www.eicsec.com',
    'http://localhost:3000',
]

# CORS ALLOWED ORIGINS
CORS_ALLOWED_ORIGINS = [
    "https://eic.com.bd",
    "https://www.eic.com.bd",
    "https://eicsec.com",
    "https://www.eicsec.com",
    "http://localhost:3000",
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
