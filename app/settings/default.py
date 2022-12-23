"""
Django settings
"""


import jinja2
from pathlib import Path

from django_jinja.builtins import DEFAULT_EXTENSIONS
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__)
BASE_ROOT = BASE_DIR.parent.parent

env = environ.Env(DEBUG=(bool, False),)

env_file = str(BASE_ROOT.parent / '.env')
env.read_env(env_file)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', default=True)

ALLOWED_HOSTS: list = []
FILE_CHARSET = 'utf-8'


# Application definition

PROJECT_APPS = [
    'apps.user',
    'apps.gallery',
]


INSTALLED_APPS = PROJECT_APPS + [
    
    'django_jinja',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',


    'ckeditor',
    'ckeditor_uploader',
]


SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'NAME': 'jinja2',
        'APP_DIRS': True,
        'DIRS': [BASE_ROOT.parent / 'markup' / 'templates'],
        'OPTIONS': {
            'environment': 'shared.env.jinja2.environment',
            'match_extension': '.jinja',
            'newstyle_gettext': True,
            'auto_reload': True,
            'undefined': jinja2.Undefined,
            'debug': True,

            'filters': {},

            'globals': {},

            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],

            'extensions': DEFAULT_EXTENSIONS,

            "bytecode_cache": {
                "name": "default",
                "backend": "django_jinja.cache.BytecodeCache",
                "enabled": True,
            },
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db('DJANGO_DB_URL')
}
DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=0)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = 'ru'
LANGUAGES = (
    ('ru', 'Russian'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_ROOT / 'static'
STATICFILES_DIRS = [
    BASE_ROOT.parent / 'markup' / 'static'
]
MEDIA_URL = '/uploads/'
MEDIA_ROOT = BASE_ROOT.parent / 'uploads'

LOCALE_PATHS = (
    BASE_ROOT / 'locale',
)


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'



CACHES = {
    'default': env.cache_url('DJANGO_CACHE_URL', 'dummycache://127.0.0.1')
}

EMAIL_CONFIG = env.email_url('DJANGO_EMAIL_URL', 'consolemail://127.0.0.1')
vars().update(EMAIL_CONFIG)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'user.CustomUser'


