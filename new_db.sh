#!/bin/bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate --run-syncd
python3 manage.py createsuperuser
