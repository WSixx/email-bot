import smtplib
from dotenv import load_dotenv
import os
import speech_recognition as sr

from gtts import gTTS
from playsound import playsound

load_dotenv()
my_email = os.getenv('MY_GMAIL')

listener =sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('listening...')
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        info = listener.recognize_google(voice, language='pt-BR')
        print(info)
except:
    pass

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(os.getenv('MY_GMAIL'), os.getenv('MY_PASSWORD'))
    server.sendmail(my_email, 'lucas.2007s@gmail.com','First Message Text')