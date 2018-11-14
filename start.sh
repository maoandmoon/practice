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

sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'difficultpassword';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

# Некоторые приложения ( Misago в том числе )
# могут устанавливать расширения для PostgreSQL.

ALTER ROLE myprojectuser superuser;
\q


