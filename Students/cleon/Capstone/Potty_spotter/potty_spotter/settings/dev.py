from .base import *

SECRET_KEY = env("DJANGO_SECRET_KEY")


DEBUG = True

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = ["127.0.0.1"]



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": "localhost",
        "PORT": "5432",
        "AUTOCOMMIT": True,
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
