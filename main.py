import telebot
import json
from pymongo import MongoClient


with open('config.json', 'r') as config:
    config = json.load(config)

bot = telebot.TeleBot(config.get('BOT_TOKEN'))
receiver = int(config.get('CHAT_ID'))
client = MongoClient(config.get('MONGO_ADDRESS', default='mongodb://localhost:27017/'))
db = client[config.get("DB_NAME", default='feedback-bot')]
collection = db[config.get("COLLECTION_NAME", default='messages')]


@bot.message_handler(commands=['ping'])
def ping(message):
    ping_message = bot.send_message(receiver, 'ping! проверяем, что бот жив')
    bot.delete_message(receiver, ping_message.message_id, timeout=60)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "привет! чем можем помочь? 👀")


@bot.message_handler(commands=['register'])
def register(message):
    pass


@bot.message_handler(commands=['kvas'])
def kvas(message):
    pass


@bot.message_handler(commands=['cola'])
def cola(message):
    bot.send_message(message.chat.id, "🥤")


@bot.message_handler(func=lambda message: message.chat.id == receiver and message.reply_to_message is not None,
                     content_types=['text', 'audio', 'photo', 'voice', 'video', 'document',
                                    'location', 'contact', 'sticker'])
def handle_admin_reply(message):
    # look up the uid based on the forwarded message ID
    reply = message.reply_to_message

    result = collection.find_one({'message_id': reply.message_id})
    # for old messages and replies inside the admin chat
    if not result:
        return
    # retrieve the user ID from the database based on the unique identifier
    user_id = result['user_id']

    # send the admin's reply back to the user
    if message.text:
        bot.send_message(user_id, message.text)
    if message.audio:
        bot.send_audio(user_id, message.audio.file_id)
    if message.photo:
        for entry in message.photo[3::4]:
            bot.send_photo(user_id, entry.file_id)
    if message.voice:
        bot.send_voice(user_id, message.voice.file_id)
    if message.video:
        bot.send_video(user_id, message.video.file_id)
    if message.document:
        bot.send_document(user_id, message.document.file_id)
    if message.location:
        bot.send_location(user_id, message.location, message.location.longitude, message.location.latitude)
    if message.sticker:
        bot.send_sticker(user_id, message.sticker.file_id)


@bot.message_handler(func=lambda message: message.chat.id != receiver,
                     content_types=['text', 'audio', 'photo', 'voice', 'video', 'document',
                                    'location', 'contact', 'sticker'])
def redirect(message):
    # forward the message to the admin chat
    forwarded_message = bot.forward_message(receiver, message.chat.id, message.message_id)

    # store message metadata and author information in the database
    doc = {
        'user_id': message.from_user.id,
        'chat_id': message.chat.id,
        'message_id': forwarded_message.message_id
    }
    result = collection.insert_one(doc)

# TODO: check whether this works with a telegram supergroup
bot.infinity_polling()
