import smtplib
from dotenv import load_dotenv
import os
import speech_recognition as sr

import pyttsx3

load_dotenv()
my_email = os.getenv('MY_GMAIL')

listener =sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def getInfo():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            info = listener.recognize_google(voice, language='pt-BR')
            return info.lower()
    except:
        pass

def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(os.getenv('MY_GMAIL'), os.getenv('MY_PASSWORD'))
    server.sendmail(my_email, 'lucas.2007s@gmail.com',getInfo())

email_list = {
    'Meu':'lucas.2007s@gmail.com',
    'lsp':'lsp.2007s@gmail.com',
}

def get_email_info():
    talk('Enviar email para quem?')
    name = getInfo()
    talk('Qual é o assunto do email?')
    subject = getInfo()
    talk('Me diga qual o texto do seu email')
    body = getInfo()


get_email_info()