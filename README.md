## Feedback Bot
This is a Telegram bot that forwards messages from users to an admin chat, where the admins can reply to the messages. The bot then forwards the replies back to the original users.

### Installation
To use this bot, you will need to have a Telegram account and a VPS running a Linux distribution. You will also need to install MongoDB on your VPS.

To install all the python packages, you can run the following command:
```commandline
pip install -r requirements.txt
```

To install MongoDB, setup the bot service and create a template for the config, you can run the setup.sh script:

```commandline
chmod +x setup.sh
./setup.sh
```
This will download and install MongoDB on your VPS.

### Running the Bot
To run the bot, you will need to create a Telegram bot and obtain an API token. You can do this by following the instructions in the Telegram documentation.

After acquiring the token you should fill in the blanks in the generated config file:
* BOT_TOKEN (token from the BotFather) 
* CHAT_ID (id of the admin chat)
* MONGO_ADDRESS (the url needed to connect to MongoDB)
* DB_NAME (the name of the mongo database, default is 'feedback-bot')
* COLLECTION_NAME (the name of the mongo collection, default is 'messages')

Then, you can install the bot.service script as a systemd service:

```commandline
sudo cp bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start bot
```
This will start the bot as a systemd service, which will run continuously on your VPS.

### License
This code is licensed under the MIT License. See the LICENSE file for details.