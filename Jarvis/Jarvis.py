from ctypes.wintypes import WIN32_FIND_DATAA
from json import load
from re import L, T
import bs4
from numpy.lib.function_base import extract, place
import pyttsx3
import speech_recognition as sr
import datetime
import winsound
import wikipedia
import webbrowser
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
import time
import os
import smtplib
import keyboard
from keyboard import press, press_and_release
import cv2
from playsound import playsound
from requests import get
from PyDictionary import PyDictionary
import pywhatkit
from pywikihow import search_wikihow
import operator
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import instaloader
import pyautogui
import requests
import psutil
import speedtest
import urllib.request
import numpy as np
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from requests.models import encode_multipart_formdata

# text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    print("   ")
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I'm Jarvis Sir,please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said....: {query}\n")

    except:
        print("Say that again please....")
        return "None"
    query = query.lower()
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender@gmail.com', 'senderpassword')
    server.sendmail('sender@gmail.com', to, content)
    server.close()


def TaskExecution():
    speak("Verification successful")
    speak("Welcome back")
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia....:")
            speak(results)

        elif 'youtube search' in query:
            speak("This is what I found")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Youtube launched....")

        elif 'google search' in query:
            query = query.replace("google search", "")
            query = query.replace("google", "")
            speak("This is what I found...!")
            pywhatkit.search(query)
            try:
                result = wikipedia.summary(query, 2)
                speak(result)
            except:
                speak("No related data available!")

        elif 'where is' in query:
            Place = query.replace("where is ", "")
            Place = query.replace("is ", "")
            Url_Place = "https://www.google.com/maps/place/" + str(Place)
            geolocator = Nominatim(user_agent="myGeocoder")
            location = geolocator.geocode(Place, addressdetails=True)
            target_location = location.latitude, location.longitude
            webbrowser.open(url=Url_Place)
            location = location.raw['address']
            target = {'city': location.get('city', ''),
                      'state': location.get('state', ''),
                      'country': location.get('country', '')}
            current_loca = geocoder.ip('me')
            current_latlon = current_loca.latlng
            distance = str(great_circle(current_latlon, target_location))
            distance = str(distance.split(' ', 1)[0])
            distance = round(float(distance), 2)
            speak(target)
            speak(f"{Place} is {distance} kilometre away from your location")

        elif 'pause' in query:
            keyboard.press('k')
        elif 'resume' in query:
            keyboard.press('space bar')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'forward' in query:
            keyboard.press('l')
        elif 'backward' in query:
            keyboard.press('j')
        elif 'fullscreen' in query:
            keyboard.press('f')
        elif 'captions' in query:
            keyboard.press('c')
        elif 'miniplayer' in query:
            keyboard.press('i')

        elif 'open chrome' in query:
            os.startfile(
                'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')
        elif 'close chrome' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'google search' in query:
            speak("This is what I found")
            query = query.replace("google search", "")
            pywhatkit.search(query)
            speak("Done....")

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
        elif 'close tab' in query:
            keyboard.press_and_release('ctrl + w')
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
        elif 'open incognito mode' in query:
            keyboard.press_and_release('ctrl + shift + n')
        elif 'minimize' in query:
            keyboard.press_and_release('alt + space + n')
        elif 'maximize' in query:
            keyboard.press_and_release('alt + space + x')
        elif 'closed tab' in query:
            keyboard.press_and_release('ctrl + shift + t')
        elif 'next tab' in query:
            keyboard.press_and_release('ctrl + tab')
        elif 'download page' in query:
            keyboard.press_and_release('ctrl + j')
        elif 'reload' in query:
            keyboard.press_and_release('fn + F5')

        elif 'send whatsapp message' in query:
            speak("Tell me the mobile number....")
            phone = int(takeCommand())
            ph = '+91' + phone
            speak("Tell me the message....")
            msg = takeCommand()
            speak("Tell me the time")
            speak("Time in hour!!")
            hour = int(takeCommand())
            speak("Time in minute!!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg(ph, msg, hour, min, 10)
            speak("Sending message.....")

        elif 'create qr' in query:
            qr = pyqrcode.create("Arshad")
            qr.png("Jarvis.png", scale=8)
        elif 'decode qr' in query:
            d = decode(Image.open("Jarvis.png"))
            print(d[0].data.decode("ascii"))

        elif 'take screenshot' in query:
            speak("Please switch to the window that you need to take screenshot")
            path = takeCommand().lower()
            path1name = path + ".png"
            path1 = "C:\\Users\Mohamed Arshed\\Pictures\\Screenshots" + path1name
            time.sleep(4)
            img = pyautogui.screenshot()
            img.save(path1)
            speak("Please hold the screen for a while")
            time.sleep(2)
            os.startfile("C:\\Users\Mohamed Arshed\\Pictures\\Screenshots")
            speak("Screenshot is saved in our main folder")

        elif 'hide all files' in query or 'visible for everyone' in query:
            speak("Please tell me you want to hide this folder or make it visible")
            condition = takeCommand().lower()
            if 'hide' in condition:
                os.system("attrib +h /s /d")
                speak("All the files are hidden")

            elif 'visible' in query:
                os.system("attrib -h /s /d")
                speak("All the files are visible")

            elif 'leave it' in query:
                speak("ok")

        elif 'open dictionary' in query:
            speak("Dictionary activated....")
            while True:
                speak("Tell me which category you want")
                prob1 = takeCommand().lower()
                if 'meaning' in prob1:
                    speak("Tell me a word")
                    m = takeCommand()
                    result = PyDictionary.meaning(m)
                    speak(f"The meaning of {m} is {result}")

                elif 'synonym' in prob1:
                    speak("Tell me a word")
                    s = takeCommand()
                    result = PyDictionary.synonym(s)
                    speak(f"The synonym of {s} is {result}")

                elif 'antonym' in prob1:
                    speak("Tell me a word")
                    a = takeCommand()
                    result = PyDictionary.antonym(a)
                    speak(f"The antonym of {a} is {result}")

                elif 'exit' in prob1:
                    speak("Deactivated")
                    break

        elif 'please remember' in query:
            rememberMsg = query.replace("please remember", "")
            speak("You tell me to remind you that: "+rememberMsg)
            remember = open('Remainder.txt', 'w')
            remember.write(rememberMsg)
            remember.close()

        elif 'what do you remember' in query:
            remember = open('Remainder.txt', 'r')
            speak("You tell me that..." + remember.read())

        elif 'open notepad' in query:
            speak("Tell me, I am ready to write it")
            writes = takeCommand()
            time = datetime.datetime.now().strftime("%H:%M")
            filename = str(time).replace(":", "-") + "-note.txt"
            with open(filename, "w") as file:
                file.write(writes)
            path_1 = "D:\\Python Codings\\Projects\\Jarvis\\" + str(filename)
            os.startfile(path_1)

        elif 'open spotify' in query:
            os.startfile(
                'C:\\Users\\Mohamed Arshed\\AppData\\Roaming\\Spotify\\Spotify.exe')
        elif 'close spotify' in query:
            os.system("TASKKILL /f /im Spotify.exe")

        elif 'open LMS' in query:
            webbrowser.open('sathyabama.cognibot.in')
        elif 'close LMS' in query:
            os.system("TASKKILL /f /im Chrome.exe")

        elif 'Whats the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            speak(f"Time is {strTime}")

        elif 'set alarm' in query:
            speak("Enter the time....!")
            time = input("Time : ")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now == time:
                    speak("Alarm started...!")
                    winsound.PlaySound('beep', winsound.SND_LOOP)
                    speak("Alarm closed....!")

                elif now > time:
                    break

        elif 'youtube video download' in query:
            Folder_Name = ""

            def openLocation():
                global Folder_Name
                Folder_Name = filedialog.askdirectory()
                if(len(Folder_Name) > 1):
                    locationError.config(text=Folder_Name, fg="green")
                else:
                    locationError.config(
                        text="Please Choose Folder!!", fg="red")

            def DownloadVideo():
                choice = ytdchoices.get()
                url = ytdEntry.get()

                if(len(url) > 1):
                    ytdError.config(text="")
                    yt = YouTube(url)
                    print(yt.title)
                    print(yt.thumbnail_url)

                if(choice == choices[0]):
                    select = yt.streams.filter(progressive=True).first()
                elif(choice == choices[1]):
                    select = yt.streams.filter(
                        progressive=True, file_extension='mp4').last()
                elif(choice == choices[2]):
                    select = yt.streams.filter(only_audio=True).first()
                else:
                    ytdError.config(text="Paste Link again!!", fg="red")

                select.download(Folder_Name)
                ytdError.config(text="Download Completed!!")

            root = Tk()
            root.title("YTD Downloader")
            root.geometry("350x400")
            root.columnconfigure(0, weight=1)

            ytdLabel = Label(
                root, text="Enter the URL of the Video", font=("jost", 15))
            ytdLabel.grid()

            ytdEntryVar = StringVar()
            ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
            ytdEntry.grid()

            ytdError = Label(root, text="Error Msg",
                             fg="red", font=("jost", 10))
            ytdError.grid()

            saveLabel = Label(root, text="Save the Video File",
                              font=("jost", 15, "bold"))
            saveLabel.grid()

            saveEntry = Button(root, width=10, bg="red", fg="white",
                               text="Choose Path", command=openLocation)
            saveEntry.grid()

            locationError = Label(
                root, text="Error Msg of Path", fg="red", font=("jost", 10))
            locationError.grid()

            ytdQuality = Label(root, text="Select Quality", font=("jost", 15))
            ytdQuality.grid()

            choices = ["720p", "144p", "Only Audio"]
            ytdchoices = ttk.Combobox(root, values=choices)
            ytdchoices.grid()

            downloadbtn = Button(
                root, text="Donwload", width=10, bg="red", fg="white", command=DownloadVideo)
            downloadbtn.grid()

            developerlabel = Label(
                root, text="Dream Developers", font=("jost", 15))
            developerlabel.grid()
            root.mainloop()

        elif 'weather details' in query:
            speak("Please enter the city name")

            def getWeather(canvas):
                city = textField.get()
                api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
                    city+"&appid=be33984512985aeb0c0f05ccef2b9784"
                json_data = requests.get(api).json()
                condition = json_data['weather'][0]['main']
                temp = int(json_data['main']['temp'] - 273.15)
                min_temp = int(json_data['main']['temp_min'] - 273.15)
                max_temp = int(json_data['main']['temp_max'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
                sunrise = time.strftime('%I:%M:%S', time.gmtime(
                    json_data['sys']['sunrise'] - 21600))
                sunset = time.strftime('%I:%M:%S', time.gmtime(
                    json_data['sys']['sunset'] - 21600))
                final_info = condition + "\n" + str(temp) + "°C"
                final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(
                    pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
                label1.config(text=final_info)
                label2.config(text=final_data)
            canvas = tk.Tk()
            canvas.geometry("600x500")
            canvas.title("Weather App")
            f = ("poppins", 15, "bold")
            t = ("poppins", 35, "bold")
            textField = tk.Entry(canvas, justify='center', width=20, font=t)
            textField.pack(pady=20)
            textField.focus()
            textField.bind('<Return>', getWeather)
            label1 = tk.Label(canvas, font=t)
            label1.pack()
            label2 = tk.Label(canvas, font=f)
            label2.pack()
            canvas.mainloop()

        elif 'covid cases' in query:
            api = "https://disease.sh/v3/covid-19/all"
            json_data = requests.get(api).json()
            total_cases = str(json_data['cases'])
            total_deaths = str(json_data['deaths'])
            today_cases = str(json_data['todayCases'])
            today_deaths = str(json_data['todayDeaths'])
            today_recovered = str(json_data['todayRecovered'])
            updated_at = json_data['updated']
            date = datetime.datetime.fromtimestamp(updated_at/1e3)
            label.config(text="Total Cases: "+total_cases +
                         "/n"+"Total Deaths: "+total_deaths +
                         "/n"+"Today Cases: "+today_cases +
                         "/n"+"Today Deaths: "+today_deaths +
                         "/n"+"Today Recovered: "+today_recovered)
            label2.config(text=date)
            canvas = tk.Tk()
            canvas.geometry("400x400")
            canvas.title("COVID TRACKER")

            f = ("poppins", 15, "bold")

            button = tk.Button(canvas, font=f, text="Load")
            button.pack(pady=20)

            label = tk.Label(canvas, font=f)
            label.pack(pady=20)

            label2 = tk.Label(canvas, font=f)
            label2.pack()

            canvas.mainloop()

        elif'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif 'open mobile camera' in query:  # connect to wifi in which mobile you have to access webcam
            URL = "https://56.127.183.210:8080/shot.png"
            while True:
                img_arr = np.array(
                    bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break
            cv2.destroyAllWindows()

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute' in query:
            pyautogui.press("volumemute")

        elif 'ip' in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")

        elif 'news' in query:
            main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=421a783f003d4749a985de43170f93f9'
            main_page = requests.get(main_url).json()
            articles = main_page["articles"]
            head = []
            day = ["1st", "2nd", "3rd", "4th", "5th",
                   "6th", "7th", "8th", "9th", "10th"]
            for ar in articles:
                head.append(ar["title"])
            for i in range(len(day)):
                speak(f"{day[i]} news is...: {head[i]}")

        elif 'instagram profile' in query:
            speak("Please enter the username correctly")
            name = input("Enter username here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Here is the profile of the user {name}")
            time.sleep(5)
            speak("Would to like to download the profile")
            condition = takeCommand().lower()
            if 'yes' in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("I am done, Profile is saved in our main folder")
            else:
                pass

        elif 'mail' in query:
            speak("what should I say")
            query = takeCommand().lower()
            if 'send file' in query:
                email = 'sender@gmail.com'
                password = 'senderpassword'
                send_to_mail = 'reciever@gmail.com'
                speak("Next, what is the subject for mail")
                query = takeCommand().lower()
                subject = query
                speak("Next, what is the message")
                query2 = takeCommand().lower()
                message = query2
                speak("Please enter the correct path of the file")
                file_location = input("Enter the path here")

                speak("Please wait, mail is sending")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_mail
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachments = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                encoders.encode_base64
                part.add_header('Content-Disposition',
                                "attachment; filename = %s" % filename)
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_mail, text)
                server.quit()
                speak("Email has been sent")

            else:
                email = 'sender@gmail.com'
                password = 'senderpasword'
                send_to_mail = 'reciever@gmail.com'
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                server.sendmail(email, send_to_mail, text)
                server.quit()
                speak("Email has been sent")

        elif 'calculator' in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("What you want to calculate")
                print("Listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)

            def get_operator_fn(op):
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    '/': operator.__truediv__,
                }[op]

            def eval_binary_expr(op1, oper, op2):
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("Result is")
            speak(eval_binary_expr(*(my_string.split())))

        elif 'temperature' in query:
            search = "Temperature in Thirukoilure"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            speak(f"Current {search} is {temp}")

        elif 'activate how to do' in query:
            speak("How to do mode is activated")
            while True:
                speak("what you want to know")
                how = takeCommand()
                try:
                    if 'exit' in how:
                        speak("Deactivated")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("I am not able to find this")

        elif 'battery percentage' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"system have {percentage} percent battery")
            if percentage >= 75:
                speak("We have maximum power")
            elif percentage >= 40 and percentage <= 75:
                speak("We have enough power")
            elif percentage >= 15 and percentage <= 30:
                speak("We don't have low power")
            elif percentage <= 15:
                speak("System will shutdown soon")

        elif 'internet speed' in query:
            speak("Checking the speed....")
            st = speedtest.Speedtest()
            dl = st.download()
            d1 = int(dl/800000)
            up = st.upload()
            u1 = int(up/800000)
            speak(
                f"The downloading speed is {d1} MBps and The uploading speed is {u1} MBps")

        elif 'windows automation' in query:
            speak("Windows Automation Activated....!")

            if 'home screen' in query:
                press_and_release('windows + m')

            elif 'show start' in query:
                press('windows')

            elif 'open settings' in query:
                press_and_release('windows + i')

            elif 'open search' in query:
                press_and_release('windows + s')

            elif 'screenshot' in query:
                press_and_release('windows + shift + s')

            elif 'restore windows' in query:
                press_and_release('windows + shift + m')

            else:
                speak("Sorry, no command found....!")

        elif 'shutdown computer' in query:
            os.system("shutdown /s /t 5")

        elif 'restart computer' in query:
            os.symlink("shutdown /r /t 5")

        elif 'sleep computer' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0, 1, 0")


if __name__ == "__main__":

    speak("This file is password protected")
    speak("Please enter the password to proceed")
    passssss = input("ENTER THE PASWORD: ")
    password = "18"
    passss = str(password)
    if passss == str(passssss):
        speak("Access Granted..")
        TaskExecution()
    else:
        speak("Access not Granted..")