"""
Django settings for kvdomingo project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import pytz
import cloudinary
import dj_database_url
from jinja2 import DebugUndefined, Undefined
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

ASSET_DIR = os.environ.get('CLOUDINARY_ASSETS_LOCATION')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG')))

DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

ALLOWED_HOSTS = [
    'api.kvdomingo.xyz',
    'api.kvdomingo.dev',
]

if DEBUG:
    ALLOWED_HOSTS.extend([
        'localhost',
        '127.0.0.1',
    ])

# Application definition

INSTALLED_APPS = [
    'web.apps.WebConfig',
    'photography.apps.PhotographyConfig',
    'svip.apps.SvipConfig',
    'dev.apps.DevConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_filters',
    'ordered_model',
    'rest_framework',
    'tinymce',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kvdomingo.urls'

CORS_ORIGIN_ALLOW_ALL = DEBUG

CORS_ORIGIN_WHITELIST = [
    'https://kvdomingo.xyz',
    'https://kvdomingo.dev',
]

if DEBUG:
    CORS_ORIGIN_WHITELIST.extend([
        'http://localhost:3000',
        'http://127.0.0.1:3000',
    ])

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [BASE_DIR / 'jinjatemplates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'kvdomingo.jinja2.environment',
            'autoescape': False,
            'undefined': DebugUndefined if DEBUG else Undefined,
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

WSGI_APPLICATION = 'kvdomingo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {'default': dj_database_url.config()}

# Rest API

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

if not DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

LOCAL_TZ = pytz.timezone(TIME_ZONE)

USE_I18N = True

USE_L10N = True

USE_TZ = True

# TinyMCE config

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'silver',
    'plugins': 'link image preview codesample contextmenu table code lists',
    'toolbar': 'formatselect | bold italic underline | alignleft aligncenter alignright alignjustify | bullist numlist | outdent indent table | link image | codesample | preview code',
    'toolbar_mode': 'wrap',
    'contextmenu': 'formats | link image',
    'menubar': False,
    'inline': False,
    'indentation': '20pt',
    'keep_styles': True,
    'statusbar': True,
    'width': 'auto',
    'height': 500,
    'valid_elements': '*[*]',
    'custom_elements': 'Node',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
)

PYTHON_ENV = os.environ.get('PYTHON_ENV')

if PYTHON_ENV != 'development':
    import django_heroku

    django_heroku.settings(locals())
