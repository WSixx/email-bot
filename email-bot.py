import smtplib
from dotenv import load_dotenv
import os
import speech_recognition as sr
from email.message import EmailMessage

import pyttsx3

load_dotenv()
my_email = os.getenv('MY_GMAIL')

email_list = {
    'meu':'lucas.2007s@gmail.com',
    'lsp':'lsp.2007s@gmail.com',
    'ana': 'anajuliabigeli1@gmail.com'
}

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

def send_email(receive, subject, body):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(os.getenv('MY_GMAIL'), os.getenv('MY_PASSWORD'))
    email = EmailMessage()
    email['From'] = my_email
    email['To'] = receive
    email['Subject'] = subject
    email.set_content(body)
    server.send_message(email)



def get_email_info():
    talk('Enviar email para quem?')
    name = getInfo()
    receive  = email_list[name]
    print(receive)
    talk('Qual é o assunto do email?')
    subject = getInfo()
    print(subject)
    talk('Me diga qual o texto do seu email')
    body = getInfo()
    print(body)

    send_email(receive, subject, body)


get_email_info()