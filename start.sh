#!/bin/bash
gnome-terminal --command="celery -A mysite worker -B -l INFO"
python3 manage.py runserver
