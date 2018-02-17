import socket
from flask import Flask
from datetime import datetime

application = Flask(__name__)

@application.route("/")
def write_logfile():
    #create logfile in persistent storage with write append permission and write timestamp and pod
    with open("/mnt/logfile", "a") as file:
        file.write(str(datetime.now()) +": " + socket.gethostname() + "<br>\n") 

@application.route("/")
def get_from_logfile():
    #open logfile and return its contents
    fr = open("/mnt/logfile","r")
    log = fr.read()
    fr.close()
    return txt
    
@application.route("/")
def hello():
    write_logfile()
    log = get_from_logfile()
    text = "<html><title> Logfile <br></title><body>" + log + "</body></html>"
    return text


if __name__ == "__main__":
    application.run()
