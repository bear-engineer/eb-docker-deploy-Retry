from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

WSGI_APPLICATION = 'config.wsgi.dev.application'

SECRET_DIR = os.path.join(ROOT_DIR, '.secrets')
STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}