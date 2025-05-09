#!/bin/bash
echo "Checking if port 5173 is already in use..."
PID=$(lsof -ti:5173)
if [ -n "$PID" ]; then
  echo "Port 5173 in use. Killing process $PID..."
  kill -9 $PID
  sleep 1
else
  echo "Port 5173 is free."
fi

echo "Checking if port 8000 is already in use..."
PID=$(lsof -ti:8000)

if [ -n "$PID" ]; then
  echo "Port 8000 in use. Killing process $PID..."
  kill -9 $PID
  sleep 1
else
  echo "Port 8000 is free."
fi

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

if [ "$CI" != "true" ]; then
  echo "Starting development server"
  python manage.py runserver &
fi

echo "Switching to frontend dashboard"
cd django_performance_dashboard || exit 1

echo "Trying to load nvm if available"
export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
  . "$NVM_DIR/nvm.sh"
  echo "nvm loaded"
  nvm use 22 || echo "Node v22 not found via nvm, continuing with system node"
else
  echo "nvm not found, using system node"
fi

echo "Installing frontend dependencies"
npm install

if [ "$CI" != "true" ]; then
  echo "Starting Vite development server in background"
  nohup npm run dev -- --host 0.0.0.0 --port 5173 > vite.log 2>&1 &
fi
