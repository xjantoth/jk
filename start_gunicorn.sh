#!/bin/bash

cd /code/jk

# Prepare log files and start outputting logs to stdout
touch ./gunicorn.log
touch ./gunicorn-access.log
tail -n 0 -f ./gunicorn*.log &


python /code/jk/manage.py migrate 
python /code/jk/manage.py collectstatic --noinput
python /code/jk/manage.py makemigrations accounts
python /code/jk/manage.py migrate
#export DJANGO_SETTINGS_MODULE=projectx.settings

exec gunicorn jk.wsgi \
    --bind 0.0.0.0:8010 \
    --workers 3 \
    --log-level=info \
    --log-file=./gunicorn.log \
    --access-logfile=./gunicorn-access.log &

exec "$@"

