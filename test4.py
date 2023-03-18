a = 60
import pywhatkit
from datetime import datetime
import time
while True == True:
    seconds = time.time()
    date = datetime.fromtimestamp(seconds)
    pywhatkit.send_mail( email_sender= "dariodealmeidaasensio@gmail.com",password="Gatito2009",subject="Hola",email_receiver = "dariodealmeidasensio@gmail.com", message="Hola, xd")