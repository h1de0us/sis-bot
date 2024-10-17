# set environment variables
CURRENT_DIR=$(pwd)
CURRENT_USER=$(whoami)

sudo apt install -y software-properties-common gnupg apt-transport-https ca-certificates
sudo apt install -y mongodb-org
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.4.list
sudo apt update

sudo systemctl start mongod
sudo systemctl status mongod

# optionally, enable the MongoDB service to start automatically at boot time
sudo systemctl enable mongod

# Create config.json file
echo "Creating a config..."
cat << EOF > $CURRENT_DIR/config.json
{
    "BOT_TOKEN": "your_bot_token_here",
    "CHAT_ID": "your_admin_chat_id_here",
    "MONGO_ADDRESS": "mongodb://localhost:27017",
    "DB_NAME": "feedback-bot",
    "COLLECTION_NAME": "messages"
}
EOF
echo "config.json has been created. Please edit it with your actual values."

# Create bot.service file with filled variables
echo "Creating bot.service file"
cat << EOF | sudo tee ../bot.service
[Unit]
Description=My Bot Service
After=network.target

[Service]
Type=simple
User=$CURRENT_USER
WorkingDirectory=$CURRENT_DIR
ExecStart=/usr/bin/python3 $CURRENT_DIR/main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

echo "Bot service has been set up. Now you may change the service description and copy the service into your /etc/systemd/system."