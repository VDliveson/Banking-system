web: gunicorn banking.wsgi --log-file -
release: python manage.py migrate
release: python manage.py makemigrations
//None