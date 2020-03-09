wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
sudo apt-add-repository "deb https://download.sublimetext.com/ apt/stable/"
sudo apt -y install sublime-text
sudo apt -y install git
git clone https://github.com/jvsg6/djangoGIS.git



wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt update

sudo apt -y install libpq-dev
sudo apt -y install libxml2-dev
sudo apt -y install libjson-c-dev

sudo apt -y install postgresql-12
sudo apt -y install postgresql-12-postgis-3
sudo apt -y install postgresql-server-dev-12
sudo apt -y install postgresql-contrib



su - postgres
sudo -u postgres psql
ALTER USER postgres PASSWORD '123'; #set password 123 for user postgres
#login as postgres
psql -U postgres -h localhost
CREATE USER myuser with PASSWORD '1234';
ALTER ROLE myuser SUPERUSER;
CREATE DATABASE mydb;
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;




wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt update
sudo apt -y install pgadmin4 pgadmin4-apache2
sudo apt -y install binutils libproj-dev gdal-bin
sudo apt -y install python3-pip
sudo apt -y install pkg-config
sudo apt -y install libsqlite3-dev
sudo apt -y install libdbus-glib-1-dev





sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt -y update
sudo apt -y install gdal-bin
sudo apt -y install libgdal-dev
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal




pip3 install virtualenv
mkdir dp
cd dp
/home/ilichev/.local/bin/virtualenv dpenv
source dpenv/bin/activate
cd dpenv/
pip3 freeze
pip3 install django
#pip3 install python3-django
pip3 install psycopg2
pip3 install GDAL==2.4.2
pip install six
pip install django-leaflet



cd ..
django-admin.py startproject dpgis
cd dpgis/
subl .
python3 manage.py startapp reporter



DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD' : '1234',
        'HOST' : 'localhost',
        'PORT' : '5432',

    }
}
#    'django.contrib.gis',


wget https://download.osgeo.org/proj/proj-6.3.1.tar.gz
tar xzf proj-6.3.1.tar.gz
cd proj-6.3.1/
./configure --prefix=/home/ilichev/libs/build
make
make install
cd ..




wget https://download.osgeo.org/geos/geos-3.8.0.tar.bz2
tar xjf geos-3.8.0.tar.bz2
./configure --prefix=/home/ilichev/libs/build
make
make install
cd ..




wget https://download.osgeo.org/gdal/3.0.2/gdal-3.0.2.tar.gz
tar xzf gdal-3.0.2.tar.gz
cd gdal-3.0.2/
export LD_LIBRARY_PATH=/home/ilichev/libs/build/lib:$LD_LIBRARY_PATH
export PATH=/home/ilichev/libs/build/bin:$PATH
export CPPFLAGS=-I/home/ilichev/libs/build/include 
export LDFLAGS=-L/home/ilichev/libs/build/lib
./configure --prefix=/home/ilichev/libs/build
make
make install
cd ..




sudo ps aux | grep template1
sudo -u postgres createdb 123321123
