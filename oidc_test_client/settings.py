# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x57-da@(6*rhi%jo_*_sb+38r^d47jq!71yfs=o3n9#2kb1o4m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'mozilla_django_oidc',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oidc_test_client',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oidc_test_client.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'oidc_test_client.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Add 'mozilla_django_oidc' authentication backend

AUTHENTICATION_BACKENDS = (
    'oidc_test_client.auth.OIDCKolibriAuthenticationBackend',
)
OIDC_URL = os.environ.get("API_URL", "http://127.0.0.1:5002/oauth")

OIDC_RP_CLIENT_ID = os.environ.get("CLIENT_ID", "test.app")
OIDC_RP_CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "66af68363c605c05d4ad58c32a0591dd")
OIDC_RP_SIGN_ALGO = "RS256"
# OIDC_AUTHENTICATION_CALLBACK_URL = "kolibri:openidconnect:oidc_authentication_callback",
OIDC_OP_AUTHORIZATION_ENDPOINT = "{}/authorize".format(OIDC_URL)
OIDC_OP_JWKS_ENDPOINT = "{}/jwks".format(OIDC_URL)
OIDC_OP_TOKEN_ENDPOINT = "{}/token".format(OIDC_URL)
OIDC_OP_USER_ENDPOINT = "{}/userinfo".format(OIDC_URL)
OIDC_VERIFY_SSL = False
OIDC_TOKEN_USE_BASIC_AUTH = True
OIDC_RP_SCOPES = "openid profile"
LOGOUT_REDIRECT_URL = "/"
LOGIN_REDIRECT_URL = "/"

