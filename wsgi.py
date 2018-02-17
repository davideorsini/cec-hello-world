import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def hello():
    #create logfile in persistent storage with write append permission and write timestamp and pod
    with open("/mnt/logfile", "a") as myfile:
        myfile.write(str(datetime.now()) +": " + socket.gethostname() + "\n")
    
    #open logfile and return its contents
    fr = open("/mnt/logfile","r")
    log = fr.read()
    fr.close()
    return "Logfile\n"+ socket.gethostname() + "\n"
    #return "Hello World! Greetings from "+ socket.gethostname() + "\n"


if __name__ == "__main__":
    application.run()
