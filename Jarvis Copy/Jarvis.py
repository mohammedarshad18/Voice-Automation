import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from PIL import Image
import cv2
from requests import get
import pywhatkit
from pywikihow import search_wikihow
import operator
import time
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

#text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
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
        print(f"User said: {query}\n")

    except Exception as e:
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

def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=421a783f003d4749a985de43170f93f9'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"{day[i]} news is: {head[i]}")


def TaskExecution():
    pyautogui.press('esc')
    speak("Verification successful")
    speak("Welcome back")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

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

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif 'open google' in query:
            speak("What should I search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif 'open lms' in query:
            webbrowser.open("sathyabama.cognibot.in")

        elif 'open spotify' in query:
            os.startfile('C:\\Users\\Mohamed Arshed\\AppData\\Roaming\\Spotify\\Spotify.exe')
             
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {strTime}")

        elif'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif 'open mobile camera' in query: #connect to wifi in which mobile you have to access webcam
            URL = "https://56.127.183.210:8080/shot.png"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                img = cv2.imdecode(img_arr,-1)
                cv2.imshow('IPWebcam',img)
                q = cv2.waitKey(1)
                if q == ord("q"):
                    break;
            cv2.destroyAllWindows()

        elif 'send message' in query:
            pywhatkit.sendwhatmsg("sendernumber","HELLO",2.30)

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
            speak("Here the news")
            news()

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

        elif 'screenshot' in query:
            speak("Please tell me the name of the screenshot file")
            name = takeCommand().lower()
            speak("Please hold the screen for a while")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot is saved in our main folder")

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
                part.add_header('Content-Disposition', "attachment; filename = %s" %filename)
                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email,password)
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
                server.login(email,password)
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
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    '/' : operator.__truediv__,
                }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            speak("Result is")
            speak(eval_binary_expr(*(my_string.split())))
           
        elif 'temperature' in query:
            search = "Temperature in Thirukoilure"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
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
            if percentage>=75:
                speak("We have maximum power")
            elif percentage>=40 and percentage<=75:
                speak("We have enough power")
            elif percentage>=15 and percentage<=30:
                speak("We don't have low power")
            elif percentage<=15:
                speak("System will shutdown soon")

        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"We have {dl} MB per second download speed and {up} MB per second uploading speed")       
   
        elif 'shutdown computer' in query:
            os.system("shutdown /s /t 5")

        elif 'restart computer' in query:
            os.symlink("shutdown /r /t 5")

        elif 'sleep computer' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0, 1, 0")

if __name__ == "__main__":

 path = 'Samples'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
def Images_and_Labels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faceSamples = []
    ids = []

    for imagePath in imagePaths:
        gray_img = Image.open(imagePath).convert('L')
        img_arr = np.array(gray_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_arr)

        for (x,y,w,h) in faces:
            faceSamples.append(img_arr[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

print("Training faces....")

faces,ids = Images_and_Labels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('Trainer/Trainer.yml')

print("Model trained successfully, Now we can recognize your face...")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('Trainer/Trainer.yml')
cascadePath = cv2.data.haarcascades +"haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX
id = 2
names = ['','Arshad']

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(3, 640)
cam.set(4, 480)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:
    ret,img = cam.read()
    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
        )
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w])

        if (accuracy < 100):
            id = names[id]
            accuracy = " {0}%".format(round(100 - accuracy))
            TaskExecution()

        else:
            id = "unknown"
            accuracy = " {0}%".format(round(100 - accuracy))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,0), 1)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)
    cv2.imshow('camera',img)

    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

print("Thanks for using this program....")
cam.release()
cv2.destroyAllWindows()