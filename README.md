## Feedback Bot
This is a Telegram bot that forwards messages from users to an admin chat, where the admins can reply to the messages. The bot then forwards the replies back to the original users.

### Installation
To use this bot, you will need to have a Telegram account and a VPS running a Linux distribution. You will also need to install MongoDB on your VPS.

To install all the python packages, you can run the following command:
```commandline
pip install -r requirements.txt
```

To install MongoDB and its dependencies, you can run the mongo-setup.sh script:

```commandline
./mongo-setup.sh
```
This will download and install MongoDB on your VPS.

### Running the Bot
To run the bot, you will need to create a Telegram bot and obtain an API token. You can do this by following the instructions in the Telegram documentation.

Once you have obtained an API token, you can create a file named config.json and add the following params:
* API token 
* CHAT_ID (id of the admin chat)
* MONGO_ADDRESS (the url needed to connect to MongoDB)

Also, there is a script named bot.service, which is needed to run the bot continuously on your VPS. This example assumes 
that your bot script is written in Python 3 and located in /path/to/your/bot/script.py. You should adjust the User and 
WorkingDirectory settings to match your VPS setup.
Then, you can install the bot.service script as a systemd service:

```commandline
sudo cp bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl start bot
```
This will start the bot as a systemd service, which will run continuously on your VPS.

### License
This code is licensed under the MIT License. See the LICENSE file for details.