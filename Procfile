web: gunicorn banking.wsgi --log-file -
heroku config:set DISABLE_COLLECTSTATIC=1
release: python manage.py migrate
release: python manage.py makemigrations
