release: python src/manage.py migrate
web: PYTHONPATH=src gunicorn app.wsgi
worker: PYTHONPATH=src python src/manage.py rundramatiq
