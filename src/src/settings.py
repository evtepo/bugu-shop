import os
from pathlib import Path

from environ import Env
from split_settings.tools import include


BASE_DIR = Path(__file__).resolve().parent.parent

env = Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = ["*"]

ROOT_URLCONF = "src.urls"

WSGI_APPLICATION = "src.wsgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "article.User"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Article API",
    "DESCRIPTION": "API for managing articles",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": True,
}

include(
    "components/*.py",
)
