"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
SETTINGS_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(SETTINGS_DIR)


# Application definition

ROOT_URLCONF = "backend.urls"

INSTALLED_APPS = [
    "jet",  # < Must come before contrib.admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",  # < Per Whitenoise, to disable built in
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "drf_yasg",
    "backend.records",
    "backend.core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # Insert Whitenoise Middleware at top but below Security Middleware
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Insert Whitenoise Middleware at top but below Security Middleware
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "backend.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# RestFramework
# https://www.django-rest-framework.org/
REST_FRAMEWORK = {
    # adds ?filter= to viewsets
    # "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    # pass request.version by getting namespace on url route
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning"
}

# Django Yasg + Redoc Settings
# https://drf-yasg.readthedocs.io/en/stable/settings.html
REDOC_SETTINGS = {"SPEC_URL": "/openapi.yaml"}

# Django Jet
JET_DEFAULT_THEME = "default"
JET_SIDE_MENU_COMPACT = True
JET_SIDE_MENU_ITEMS = [
    {"app_label": "auth", "items": [{"name": "group"}, {"name": "user"}]},
    {"app_label": "authtoken", "items": [{"name": "token"}]},
    {"app_label": "records", "items": [{"name": "record"}]},
    {
        "label": "Links",
        "items": [
            {"label": "Docs", "url": "/redoc", "url_blank": True},
            {"label": "Api V1", "url": "/api/v1", "url_blank": True},
        ],
    },
]

# Static Files
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# http://whitenoise.evans.io/en/stable/django.html?highlight=django

# static url
STATIC_URL = "/static/"
# destication of collectstatic
STATIC_ROOT = "staticfiles"
# Where to search for static files
# STATICFILES_DIRS = []
