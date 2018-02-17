import socket
from flask import Flask
import calendar
import time

application = Flask(__name__)

@application.route("/")
def hello():
 
    return "Hello World! Greetings from "+ socket.gethostname() + calendar.timegm(time.gmtime()) + "\n"


if __name__ == "__main__":
    application.run()
