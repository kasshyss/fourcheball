sudo apt-get install python
sudo apt-get install python-pip python-dev build-essential
sudo pip install
sudo pip install bs4
sudo pip install Flask
sudo pip install requests
sudo apt-get install wget
wget --quiet -0 https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install postgresql
sudo apt-get install postgresql-client
sudo adduser meriadoc
sudo -u postgres createuser meriadoc
sudo -u postgres createdb -O meriadoc fourcheball
