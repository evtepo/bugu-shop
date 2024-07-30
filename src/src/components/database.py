DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DJANGO_DATABASE_NAME", default="article"),
        "USER": env("DJANGO_DATABASE_USER", default="postgres"),
        "PASSWORD": env("DJANGO_DATABASE_PASSWORD", default="postgres"),
        "HOST": env("DJANGO_DATABASE_HOST", default="localhost"),
        "PORT": env.int("DJANGO_DATABASE_PORT", default=5432),
    }
}
