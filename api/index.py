from flask import Flask, request
from telebot import TeleBot, types
import json

TOKEN = "5769907387:AAF0tVVa2RNQjFpOeYmRAIWBhzIBa1jFp4E"
bot = TeleBot(TOKEN, parse_mode="html")
app = Flask(__name__)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello!")

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    data = request.stream.read().decode('utf-8')
    update = types.Update.de_json(data)
    
    if update.message:
        bot.process_new_messages([update.message])

    return "OK", 200

@app.route("/")
def set_webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://tgbot-46vemn21f-really650a.vercel.app/' + TOKEN)
    return "Webhook set up successfully!", 200

