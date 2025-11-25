#########################################################
"""
Development settings configuration
"""
#########################################################
from app.settings.base import *

# BASE CONFIGRATION
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*']
SECRET_KEY = env('SECRET_KEY')

# DATABASE CONFIGRATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CSRF TRUSTED ORIGINS
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:3000',
    'http://localhost:3001',
    'http://127.0.0.1:8000',
]

# CORS ALLOWED ORIGINS
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:3000',
    'http://localhost:3001',
    'http://127.0.0.1:8000',
]
