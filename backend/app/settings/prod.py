#########################################################
"""
Production settings configuration
"""
#########################################################
from app.settings.base import *

# BASE CONFIGRATION
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['eic.com.bd', 'eicsec.com']
SECRET_KEY = env('SECRET_KEY')

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
]
