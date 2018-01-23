from .base import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME', 'leadshop'),
        'USER': os.getenv('DATABASE_USER', 'johnkagga'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', ''),
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

SITE_DOMAIN = "localhost:8000"
