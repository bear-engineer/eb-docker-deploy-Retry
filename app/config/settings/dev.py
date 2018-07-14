from .base import *
# 개발용 Setting
secret = json.load(open(os.path.join(SECRET_DIR, 'secrets.json')))

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

# django-storages
INSTALLED_APPS += [
    'storages',
]

WSGI_APPLICATION = 'config.wsgi.dev.application'

STATIC_ROOT = os.path.join(ROOT_DIR, '.static')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR,
]
DEFAULT_FILE_STORAGE = 'config.storage.S3DefaultStorage'
STATICFILES_STORAGE = 'config.storage.S3StaticStorage'

AWS_ACCESS_KEY_ID = secret['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = secret['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secret['AWS_STORAGE_BUCKET_NAME_DEV']
AWS_DEFAULT_ACL = secret['AWS_DEFAULT_ACL']
AWS_S3_REGION_NAME = secret['AWS_S3_REGION_NAME']
AWS_S3_SIGNATURE_VERSION = secret['AWS_S3_SIGNATURE_VERSION']

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


DATABASES = secret['DATABASE_DEV']