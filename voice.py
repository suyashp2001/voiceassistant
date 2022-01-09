# news api 3fbf45e56df34d81a28df2e09a94ee6f

import calendar
import ctypes
import datetime
import json
import os
import random
import smtplib
import subprocess
import time
import warnings
import webbrowser
from time import sleep

import gtts
import playsound
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import winshell
from pyttsx3 import engine
from selenium import webdriver
from twilio.rest import Client
import wolframalpha
import  time

warnings.filterwarnings("ignore")


engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

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


#def talk(text):
   # print(text)


    #tts = gTTS(text=text, lang="en")

   # audio = "Audio.mp3"
    #tts.save(audio)

  #  playsound.playsound(audio)

   # os.remove(audio)
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


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def send_emails(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("patankarsuyash7@gmail.com", "suyash@2865")
    server.sendmail("patankarsuyash7@gmail.com", to, content)
    server.close()


def pizza():
    driver = webdriver.Chrome(r"C:\Users\suyas\Desktop\chromedriver.exe")
    driver.maximize_window()
    talk("Opening Dominos")
    driver.get("https://www.dominos.co.in/")
    sleep(2)

    talk("getting ready for order")
    driver.find_element_by_link_text("ORDER ONLINE NOW").click()
    sleep(2)

    talk("Finding your location")
    driver.find_element_by_class_name("srch-cnt-srch-inpt").click()
    sleep(2)

    location = " D-104,New Kunj Vihar,Ramesh Nagar, Amboli, Andheri-west,Mumbai-400058"
    talk("Entering your location")
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input'
    ).send_keys(location)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li/div[2]'
        # tp check og '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[2]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li/div[2]/span[2]'
    ).click()
    sleep(2)

    try:
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]'
        ).click()
        sleep(2)
    except:
        talk("Your location could not be found")
        exit()
    talk("Logging in")

    phone_num = '7506823061'
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input'
    ).send_keys(phone_num)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input'
    ).click()
    sleep(2)
    talk("What is your OTP")
    sleep(3)
    otp_log = rec_audio()
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input'
    ).send_keys(otp_log)
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button'
    ).click()
    sleep(2)

    talk("Do you want me to order from your favourites")
    query_fav = rec_audio()

    if "yes" in query_fav:
        try:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[2]/div/div[7]/div/div/div[2]/div[3]/div/button/span'
            ).click()
            sleep( 1 )
        except:
            talk( "Entered OTP is incorrect" )
            exit()

        talk( "Adding your favourites to the cart" )

        talk( "doyou waant me to add extra cheese to your pizza?" )
        ex_cheese = rec_audio()
        if "yes" in ex_cheese:
            talk( "extra cheese added" )
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[4]/div/div[1]/div/div/div[2]/div[3]/div[2]/button/span'
            ).click()
        elif "no" in ex_cheese:
            talk( "No extra cheese added" )
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span'
            ).click()
        else:
            talk( "I dont know that" )
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span'
            ).click()

        talk( "would you like to increase the quantity" )
        qty = rec_audio()
        qty_pizza = 0
        if "yes" in qty:
            talk( "How many more pizzas do you want to add" )
            try:
                qty_pizza = rec_audio()
                qty_pizza = int( qty_pizza )
                if qty_pizza > 0:
                    talk_plz = f"Adding{qty_pizza} more pizzas"
                    talk( talk_plz )
                    for i in range( qty_pizza ):
                        driver.find_element_by_xpath(
                            '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]'
                        ).click()
            except:
                talk( "I dont know that" )
        else:
            pass

        total_pizza = qty_pizza + 1
        tell_num = f"This is your list of orders.{total_pizza} pizzas and Do you want to checkout"
        talk( tell_num )
        check_order = rec_audio()
        if "yes" in check_order:
            talk( "Checking out" )
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'
            ).click()
            sleep( 1 )
            total = driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[5]/span[2]/span'
            )
            total_price = f'Total price is {total.text}'
            talk( total_price )
            sleep( 1 )
        else:
            exit()
        talk( "Placing order" )
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button/span'
        ).click()
        sleep( 2 )
        try:
            talk( "saving your details" )
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/font/font/input'
            ).click()
            sleep( 2 )
        except:
            talk( "the store is currently offline" )
        talk( "Do you want to confirm your order" )
        confirm = rec_audio()
        if "yes" in confirm:
            talk( "placing your order" )
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button/span/font/font'
            ).click()
            sleep( 2 )
            talk( "Your order is placed successfully. Dominos will be reaching you soon. Enjoy your food!" )
        else:
            exit()
    else:
        exit()



while True:

    try:

        text = rec_audio()
        speak = " "

        if call(text):
            speak = speak + say_hello(text)

            if "date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today
                print(" " + get_today)

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
                print(" " + "It is" + str(hour) + ":" + minute + " " + meridiem + " .")

            elif "wikipedia" in text or "Wikipedia" in text:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki
                    print(" " + wiki)

            elif "who are you" in text or "define yourself" in text:
                speak = speak + """Hello, I am an Assistant. Your Assistant. I am here to make your life easier.You can command me to perform various tasks such as solving mathematical questions or opening applications and many other things.."""
                print("Hello, I am an Assistant. Your Assistant. I am here to make your life easier.You can command me to perform various tasks such as solving mathematical questions or opening applications and many other things..")

            elif "your name" in text:
                speak = speak + "my name is Assistant"
                print("my name is Assistant")

            elif "who am I" in text:
                speak = speak + "You are human for whom I was created."
                print("You are human for whom I was created.")

            elif "why do you exist" in text or "why did you come" in text:
                speak = speak + "My existence is for making your life easier."
                print("My existence is for making your life easier.")

            elif "how are you" in text:
                speak = speak + "I am fine thankyou"
                speak = speak + "\nHow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "Its good to know you are fine"

            elif "open" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Opening Google chrome"
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )
                elif "word" in text.lower():
                    speak = speak + "Opening Microsoft word"
                    os.startfile(
                        r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
                    )

                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft excel"
                    os.startfile(
                        r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
                    )

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube"
                    webbrowser.open("https://youtube.com/")

                elif "google" in text.lower():
                    speak = speak + "Opening google"
                    webbrowser.open("https://google.com/")

                else:
                    speak = speak + "application not available"

            elif "on youtube" in text.lower():
                ind = text.lower().split().index("on youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )
                speak = speak + "opening" + str(search) + "on youtube"

            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.google.com/search?q=" +
                    "+".join(search)
                )
                speak = speak + "searching" + str(search) + "on google"

            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.google.com/search?q=" +
                    "+".join(search)
                )
                speak = speak + "searching" + str(search) + "on google"

            elif "change background" in text or "change wallpaper" in text:  # dir issue
                img = r'C:\Users\suyas'
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = speak + "Background changed successfully"

            elif "play music" in text or "play song" in text:  # not working
                talk("here you go with music")
                music_dir = r'C:\Users\suyash\Music'
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                random = os.path.join(music_dir, d)
                playsound.playsound(random)

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Emptied successfully"

            elif "note" in text or "remember this" in text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that."

            elif "joke" in text or "jokes" in text:
                speak = speak + pyjokes.get_joke()
                print(" "+ pyjokes.get_joke())

            elif "where is" in text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                print("This is where " + str(location) + " is.")
                webbrowser.open(url)



            elif "news" in text:
                url = ('https://newsapi.org/v2/top-headlines?'
                       # 'q=Apple&'
                       # 'from=2021-09-02&'
                       'country=in&'
                       'apiKey=3fbf45e56df34d81a28df2e09a94ee6f')

                try:
                    response = requests.get(url)
                except:
                    talk("please check your connection")

                news = json.loads(response.text)

                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    talk(str(new["title"]))
                    engine.runAndWait()
                    print(str(new["description"]), "\n")
                    talk(str(new["description"]))
                    engine.runAndWait()

            elif "order a pizza " in text or "pizza" in text:
                pizza()



            elif "weather" in text:
                key = "b13327a47ab55c80f843ddaa62ec9c8c"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                ind = text.split().index("in")
                location = text.split()[ind + 1:]
                location = "".join(location)
                url = weather_url + "appid=" + key + "&q=" + location
                js = requests.get(url).json()
                if js["cod"] != "404":
                    weather = js["main"]
                    temperature = weather["temp"]
                    temperature = temperature - 273.15
                    humidity = weather["humidity"]
                    desc = js["weather"][0]["description"]
                    weather_response = "In " + str(location) + " the temperature  in Celcius is " + str(
                        round(temperature)) + " the humidity " + str(
                        humidity) + " and the weather description  is " + str(desc)
                    print("In " + str(location) + " the temperature  in Celcius is " + str(
                        round(temperature)) + " the humidity " + str(
                        humidity) + " and the weather description  is " + str(desc))
                    speak = speak + weather_response
                else:
                    speak = speak + "not found"

            elif "email myself" in text or "gmail myself" in text:
                try:
                    print("What should I say?")
                    talk("What should I say?")
                    content = rec_audio()
                    to = "suyashs.patankar@gmail.com"
                    send_emails(to, content)
                    speak = speak + "Email has been send!!"
                except Exception as e:
                    print(e)
                    talk("I am not able to send this email")

            elif "email" in text or "gmail" in text:
                try:
                    print("What should I say?")
                    talk("What should I say?")
                    content = rec_audio()
                    to = input("Enter senders address:")
                    send_emails(to, content)
                    speak = speak + "Email has been send!!"
                except Exception as e:
                    print(e)
                    talk("I am not able to send this email")

            elif "send message" in text or "send a message" in text:
                account_sid = "AC20104f55411071b7bbb68fc024e62ba0"
                auth_token = "7307bb3e747c0d0bbb86a604b920f228"
                client = Client(account_sid, auth_token)

                talk("What should I send?")
                message = client.messages.create(
                    body=rec_audio(), from_= "+19522602558", to= "7506823061"
                )

                print(message.sid)
                speak = speak + "message send successfully"

            elif "calculate" in text:
                app_id = "6PU83W-LRAJRA56YT"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "the answer is " + answer
                print("the answer is " + answer)

            elif "what is" in text or "who is" in text:
                app_id = "6PU83W-LRAJRA56YT"
                client = wolframalpha.Client( app_id )
                ind = text.lower().split().index( "is" )
                text = text.split()[ind + 1:]
                res = client.query( " ".join( text ) )
                answer = next( res.results ).text
                speak = speak + "the answer is " + answer
                print( "the answer is " + answer )

            elif "dont listen" in text or "stop listening" in text or "do not listen" in text:
                talk("for how many seconds do yo want me to sleep")
                a = int(rec_audio())
                time.sleep()
                speak = speak + str(a) +" seconds completed. Now you ask me anything."

            elif "exit" in text or "quit" in text:
                exit()

            talk(speak)



    except:
        talk("I don't know that")
