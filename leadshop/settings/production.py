from .base import *
import dj_database_url
import os

DEBUG = False

ALLOWED_HOSTS += [
    'leadshop.herokuapp.com'
]

SECRET_KEY = os.getenv('SECRET_KEY', '604s%iu%y$_356fb2#kmsc@yk+g0#hd4ztbnoc!k0y^$_y9n+n')

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
