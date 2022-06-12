web: gunicorn ecommerce.wsgi --log-file -
release: python manage.py migrate
heroku config:set secret_key= 