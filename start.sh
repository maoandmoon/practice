#!/bin/sh

virtualenv venv --python=python3
. venv/bin/activate
npm install
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py makemigrations salon
python manage.py migrate
python manage.py loaddata salon.json
python manage.py createsuperuser

