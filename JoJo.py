import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import time

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

r=sr.Recognizer()

def wishme():
    hour=datetime.datetime.now().hour
    if hour >=0 and hour < 12:
        print("Hello Mayank Sir, JoJo Here, Good Morning\n")
        speak("Hello Mayank Sir, JoJo Here, Good Morning")

    elif hour>=12 and hour <=3:
        print("Hello Mayank Sir, JoJo Here, Good Afternoon\n")
        speak("Hello Mayank Sir, JoJo Here, Good Afternoon")
    else:
        print("Hello Mayank Sir, JoJo Here, Good Evening\n")
        speak("Hello Mayank Sir, JoJo Here, Good Evening")
def speak(strr):
    engine.say(strr)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        try:
            print("How Can I Help You Sir Tell Me I Am Listening......\n")
            speak("How Can I Help You Sir tell me i am listening")
            audio=r.listen(source)
            text=r.recognize_google(audio,language='en-IN')
            print(text)
            return text.lower()
        except:
            print("Sir I am not able to listen you Speak again")
            speak("Sir I am not able to listen you speak again")
if __name__ == "__main__":
    wishme()
    tm=time.time()
    f=open('plan.txt','r')

    while True:
        
        if time.time() - tm>(45*60):
            tm=time.time()
            print("Mayank Sir Please Drink water, Its Your Drinking Time")
            speak("Mayank Sir Please Drink water, Its Your Drinking Time")

        text=listen()
        if 'open youtube' in text:
            speak("opening youtube")
            webbrowser.open('youtube.com')
        
        elif 'open google' in text:
            speak("opening google")
            webbrowser.open('google.com')
        
        elif 'open github' in text:
            speak("opening github")
            webbrowser.open('github.com')

        elif 'jojo what is ' in text:
            queryyy=text.replace('jojo what is ',"")
            result=wikipedia.summary(queryyy,sentences=2)
            print(result)
            speak(result)
        
        elif 'open vs code' in text:
            print("Opening VS Code\n")
            speak("Opening VS Code")
            os.startfile(r"C:\Users\JXX\Downloads\VSCode-win32-ia32-1.48.2\Code.exe")
        
        elif 'play music' in text:
            print("Playing One of your Favourite Song\n")
            speak("Playing One of your Favourite Song")
            path=r"E:\Songs"
            songs=os.listdir(path)
            os.startfile(os.path.join(path,songs[random.randint(0,len(songs))]))
        
        elif 'time' in text:
            print("Currrent Time is\n")
            speak("Current Time is")
            timestr=datetime.datetime.now().strftime("%H:%M:%S")
            print(timestr)
            speak(timestr)

        elif 'date' in text:
            print("Todays Date is\n")
            speak("Todays Date is")
            timestr=datetime.datetime.now().date()
            print(timestr)
            speak(timestr)
        
        elif 'yourself' in text:
            print("Mayank Sir My Name Is Jojo And I Am Your Personal Desktop Assistant\n")
            speak("Mayank Sir My Name Is Jojo And I Am Your Personal Desktop Assistant")
            print("Mayank Sir I Can Do The Following Things For You\n")
            speak("Mayank Sir I Can Do The Following Things For You")
            print("I Can Open Any Website For You")
            speak("I Can Open Any Website For You")
            print("I Can Search Anything Over Internet For You")
            speak("I Can Search Anything Over Internet For You")
            print("I Can Tell You About Your Plans For The Week")
            speak("I Can Tell You About Your Plans For The Week")
            print("I Can Push Your Repositries To Your Github")
            speak("I Can Push Your Repositries To Your Github")
            print("I Can Play Your Favourite Music")
            speak("I Can Play Your Favourite Music")
            print("I Can Set Reminders For You")
            speak("I Can Set Reminders For You")
            print("I Also Care For You, So I Will Remind You To Drink Water After Every 45 Minutes")
            speak("I Also Care For You, So I Will Remind You To Drink Water After Every 45 Minutes")
        
        elif 'plans' in text:
            for pn in f:
                print(pn)
                speak(pn)
        elif 'remind' in text:
            with open("reminder.txt","a") as fh:
                text.replace("remind","")
                try:
                    text.replace("jojo","")
                except:
                    pass
                fh.write(f"{text}\n")
            print("Okay Sir I Will Remind You")
            speak("Okay Sir I Will Remind You")
    f.close()