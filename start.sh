#!/bin/sh

virtualenv venv --python=python3
source venv/bin/activate
venv/bin/python -m pip install -r requirements.txt
npm install
python manage.py makemigrations
python manage.py makemigrations salon
python manage.py migrate
python manage.py loaddata salon.json
python manage.py createsuperuser

