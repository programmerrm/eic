#########################################################
"""
Production settings configuration
"""
#########################################################
from app.settings.base import *

# BASE CONFIGRATION
DEBUG = False
ALLOWED_HOSTS = ['eic.com.bd', 'www.eic.com.bd', 'eicsec.com', 'www.eicsec.com']
SECRET_KEY = 'django-insecure--j7#f^zo#_&rlptdsq0ut#8)cdnocjkb=$7*=(vyc4z%5zizum'

# DATABASE CONFIGRATION
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# CSRF TRUSTED ORIGINS
CSRF_TRUSTED_ORIGINS = [
    'https://eic.com.bd',
    'https://www.eic.com.bd',
    'https://eicsec.com',
    'https://www.eicsec.com',
]

# PROD FILE
