from flask import Flask, request
from telebot import TeleBot 
from telebot.types import *

TOKEN = "6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM"
bot = TeleBot(TOKEN, parse_mode="html")
app = Flask(__name__)

@bot.message_handler(commands =["start"])
def start(message):
	bot.send_message(message.chat.id, "Hello!")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    update = Update.de_json(request.stream.read().decode('utf-8'))
    if update.message:
        bot.process_new_messages([update.message])
        
    return "Hello World!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://tgbot-iota-tan.vercel.app/' + TOKEN)
    return "Hello World!", 200

app.run()
