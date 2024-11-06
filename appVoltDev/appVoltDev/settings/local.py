from .base import *
from .secret import SECRET

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": SECRET.get("DB_NAME"),
        "USER": SECRET.get("DB_USER"),
        "PASSWORD": SECRET.get("DB_PASS"), 
        "HOST": SECRET.get("DB_HOST"),
        "PORT": SECRET.get("DB_PORT"),
        "OPTIONS": {
            "sql_mode": "STRICT_TRANS_TABLES",
        },
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static/"]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media_local/"
