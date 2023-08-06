#from flask import Flask, request
#from telebot import Telebot 
#from telebot.types import *

#TOKEN = "6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM"
#bot = TeleBot(TOKEN, parse_mode="html")
#server = Flask(__name__)

#@bot.message_handler(commands =["start"])
#def start(message):
	#bot.send_message(message.chat.id, "Hello!")

#@server.route('/' + TOKEN, methods=['POST'])
#def getMessage():
    #update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    #if update.message:
        #bot.process_new_messages([update.message])
        
    #return "ok", 200

#@server.route("/")
#def webhook():
    #bot.remove_webhook()
    #bot.set_webhook(url='https://tgbot-flame.vercel.app/' + TOKEN)
    #return "ok", 200



from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
