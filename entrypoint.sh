#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate
python manage.py loaddata --format json credit/fixtures/db.json

# Start server
echo "Starting server"
python manage.py runserver 127.0.0.1:8000