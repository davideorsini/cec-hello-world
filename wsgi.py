import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    flog = open('/mnt/log.txt', 'a')
#     text = "" + socket.gethostname() + time.time() + "\n"
#     flog.write(text)
    flog.close()
    return "Hello World! Greetings from "+ socket.gethostname() + time.time()"\n"


if __name__ == "__main__":
    application.run()
