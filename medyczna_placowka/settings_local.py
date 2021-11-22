from medyczna_placowka.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME', default='DEFAULTDBNAME'),
        'USER': config('DB_USER', default='DEFAULTUSERNAME'),
        'PASSWORD': config('DB_PASSWORD', default='DEFAULTPASSWORD'),
        'HOST': config('DB_HOST', default='DEFAULTHOST'),
        'PORT': config('DB_PORT', default='1111'),
    }
}
