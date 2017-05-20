release: python manage.py migrate  --noinput && python manage.py loaddata fixtures/*.json
web: gunicorn habitat.wsgi
