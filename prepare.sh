#!/bin/bash
BOOTSTRAP=bootstrap-4.4.1-dist
wget https://github.com/twbs/bootstrap/releases/download/v4.4.1/$BOOTSTRAP.zip
unzip $BOOTSTRAP.zip -d ./adm/
mv ./adm/$BOOTSTRAP/ ./adm/static
rm $BOOTSTRAP.zip
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate --run-syncd
python3 manage.py createsuperuser