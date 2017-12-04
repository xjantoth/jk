FROM python:3

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y; apt-get install nginx supervisor -y && \
    mkdir -p /etc/supervisord /var/log/supervisord /code && \ 
    rm /etc/nginx/sites-enabled/default && \
    sed -i '1idaemon off;' /etc/nginx/nginx.conf 


WORKDIR /code
COPY jk_app.conf /etc/nginx/sites-enabled/jk_app.conf
COPY . /code/
COPY supervisord.conf /etc


RUN  pip install -r reqirements.txt && \
     python /code/jk/manage.py migrate && \ 
     python /code/jk/manage.py collectstatic --noinput && \
     python /code/jk/manage.py migrate && \
     chmod +x /code/start_gunicorn.sh

ENTRYPOINT ["/code/start_gunicorn.sh"]

CMD ["supervisord", "-c", "/etc/supervisord.conf"]

