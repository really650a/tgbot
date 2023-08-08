"""from flask import Flask, request
from telebot import TeleBot 
from telebot.types import *

TOKEN = "5769907387:AAF0tVVa2RNQjFpOeYmRAIWBhzIBa1jFp4E"
bot = TeleBot(TOKEN, parse_mode="html")
app = Flask(__name__)

@bot.message_handler(commands =["start"])
def start(message):
	return bot.send_message(message.chat.id, "Hello!")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    if update.message:
        bot.process_new_messages([update.message])
        
    return "Hello World!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://tgbot-gamma-seven.vercel.app/' + TOKEN)
    return "Hello World!", 200
"""
from flask import Flask, request
from telebot import TeleBot 
from telebot.types import *

TOKEN = "5769907387:AAF0tVVa2RNQjFpOeYmRAIWBhzIBa1jFp4E"
bot = TeleBot(TOKEN, parse_mode="html")
app = Flask(__name__)

last_update_id = None

@bot.message_handler(commands=["start"])
def start(message):
    return bot.send_message(message.chat.id, "Hello!")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    global last_update_id

    update = Update.de_json(request.stream.read().decode('utf-8'))

    if update.message and (last_update_id is None or update.update_id > last_update_id):
        last_update_id = update.update_id
        bot.process_new_messages([update.message])

    return "Hello World!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your-webhook-url.com/' + TOKEN)
    return "Hello World!", 200

if __name__ == "__main__":
    app.run()

