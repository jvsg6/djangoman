
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
sudo apt update
sudo apt -y install libpq-dev libxml2-dev libjson-c-dev
sudo apt -y install postgresql-12 postgresql-12-postgis-3 postgresql-server-dev-12 postgresql-contrib
sudo apt install net-tools

#sudo netstat -pant | grep postgres
#/etc/postgresql/9.2/main/postgresql.conf
#listen_addresses = '*'
#sudo service postgresql restart
#psql -U myuser -h 10.0.0.101 mydb

#/etc/postgresql/9.2/main/pg_hba.conf
#host    mydb             myuser         10.0.0.1/32            md5
#sudo service postgresql reload


#psql -U myuser -h 192.168.1.105 mydb
