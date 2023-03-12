sudo apt install -y software-properties-common gnupg apt-transport-https ca-certificates
sudo apt install -y mongodb-org
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update

sudo systemctl start mongod

sudo systemctl status mongod

# Optionally, enable the MongoDB service to start automatically at boot time
sudo systemctl enable mongod