a = 60
import pywhatkit
from datetime import datetime
import time
while True == True:
    seconds = time.time()
    date = datetime.fromtimestamp(seconds)
    pywhatkit.sendwhatmsg_instantly("+34 644 70 07 26" , "Hola", date.hour, date.minute)
