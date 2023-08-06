from flask import Flask, request

server = Flask(__name__)


@server.route("/")
def web():
    return "ok", 200
