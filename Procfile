web: gunicorn CVapp1.wsgi --log-file -
python manage.py runserver 0.0.0.0:$PORT collectstatic --noinput
manage.py migrate
