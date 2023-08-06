import os
from flask import Flask, request
import telebot
from telebot.types import *
from telebot import custom_filters

TOKEN = "6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM"
bot = telebot.TeleBot(TOKEN, parse_mode="html")
server = Flask(__name__)

@bot.message_handler(commands =["start"])
def start(message):
	bot.send_message(message.chat.id, "Hello!")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    if update.message:
        bot.process_new_messages([update.message])
        
    return "ok", 200

@server.route("/")
def webhook():
    #bot.remove_webhook()
    #bot.set_webhook(url='https://flask.tolasaa.repl.co/' + TOKEN)
    return "ok", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
