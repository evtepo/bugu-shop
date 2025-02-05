#!/usr/bin/env bash

while ! nc -z $DJANGO_DATABASE_HOST $DJANGO_DATABASE_PORT; do
      sleep 0.1
done 

python manage.py makemigrations
python manage.py migrate

gunicorn --bind 0.0.0.0:8000 src.wsgi:application