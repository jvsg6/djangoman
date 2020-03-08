wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt update
sudo apt -y install postgresql postgresql-contrib
su - postgres
sudo -u postgres psql


wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt update
sudo apt install pgadmin4 pgadmin4-apache2 -y

sudo apt install python3-pip
pip3 install django

sudo apt-get install binutils libproj-dev gdal-bin
pip3 install python3-django

sudo apt install pkg-config

sudo apt install libsqlite3-dev
sudo apt install libdbus-glib-1-dev


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

sudo apt update
sudo apt-get install libpq-dev
sudo apt-get install libxml2-dev
sudo apt-get install libjson-c-dev



sudo apt install postgresql-12
sudo apt install postgresql-12-postgis-3
sudo apt install postgresql-server-dev-12


sudo ps aux | grep template1
sudo -u postgres createdb 123321123
