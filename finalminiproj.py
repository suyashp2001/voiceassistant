import calendar
import datetime
import random
import warnings

import gtts
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import wikipedia

warnings.filterwarnings("ignore")

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        audio = recog.listen(source)

    data = " "

    try:
        data = recog.recognize_google(audio)
        print("you said:" + data)

    except sr.UnknownValueError:
        print("assistant could not understand the audio")

    except sr.RequestError as ex:
        print(" request error" + ex)

    return data

def speaktome(audio_string):
    tts = gtts.gTTS( text=audio_string, lang='en' )
    h = random.randint( 1, 10000000 )
    audio_file = str( h ) + '.mp3'
    tts.save( audio_file )
    playsound( audio_file )
    print( audio_string )
    os.remove( audio_file )


def call(text):
    action_call = "friend"

    text = text.lower()

    if action_call in text:
        return True

    return False

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month  # currentmonth
    day_now = now.day  # currentday

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return f'Today is {week_now}, {month_now} the {ordinals[day_now - 1]}.'


def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello", "howdy", "whats good", "hello", "hey there"]

    response = ["hi", "hey", "hola", "greetings", "wassup", "hello", "howdy", "whats good", "hello", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]

while True:

    try:

        text = rec_audio()
        speak = " "

        if call(text):
            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = " "
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is" + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            talk(speak)

    except:
        talk("I dont know that")