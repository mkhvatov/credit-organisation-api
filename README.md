# API for Unicom24

Web API for credit organizations and partners with different access rights.

## How to use

1. Create a virtual environment: ```virtualenv -p python3 env```
2. Activate the virtual environment: ```source env/bin/activate```
3. Install the requirements: ```pip install -r requirements.txt```
4. Create initial DB migrations: ```python manage.py migrate```
5. Load data to DB: ```python manage.py loaddata credit/fixtures/db.json```
6. Run server: ```python manage.py runserver```
7. Login: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
8. Open API documentation: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Alternative installation by Docker:

1. ```docker-compose build```
2. ```docker-compose up```

## API login information

There are several role types in system:

1. superuser (admin)
2. partner
3. credit organization

Authorization by admin panel (sessions), login / password:

```#!bash

1. superuser: super_user / A123qwerty
2. partner: partner / B123qwerty
3. credit organization: credit_organization / C123qwerty

```
