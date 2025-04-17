#!/bin/bash

echo "Setting up Python virtual environment"
python3 -m venv env
source env/bin/activate

echo "Installing requirements"
pip install --upgrade pip
pip install -r requirements.txt

echo "Running migrations"
python manage.py makemigrations
python manage.py migrate


export DJANGO_SETTINGS_MODULE=helloagaincrm.settings

echo "Checking for existing Faker data"
DATA_COUNT=$(python -W ignore -c "import django; django.setup(); from crm.models import AppUser; print(AppUser.objects.count())")

if [ "${DATA_COUNT:-0}" -eq "0" ]; then
  echo "No data found. Generating sample data"
  python manage.py generate_data
else
  echo "Data already exists ($DATA_COUNT records). Skipping generation."
fi



echo "Starting development server"
python manage.py runserver
