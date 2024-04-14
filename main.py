import datetime
import shutil
import webbrowser
import os
import time
import random
import requests
from lxml import html
import ecapture as ec
import speech_recognition as sr
import sounddevice
from wakeWord_detect import wake_detect
from wakeWord_detect import speak
from pynput.keyboard import Key, Controller
# from gbard import bard_use
import warnings
import vlc
from wakeWord_detect import wishMe
import pyjokes
import wikipedia
from wakeWord_detect import Command_input
from Data import *
import weather

warnings.filterwarnings("ignore", message='FP16 is not supported on CPU; using FP32 instead')
keyboard=Controller()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 10, 10)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        if len(query.strip()) == 0:
            speak("Empty command")
            print("Try saying...\nPlay songs\nOpen youtube\nTell jokes")

    except Exception as e:
        print(e)
        print("Linux Assistant: I am sorry, I am Unable to Recognize your voice.")
        speak("I am sorry, I am Unable to Recognize your voice.")
        return "None"

    return query




def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome ", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")

if __name__ == '__main__':
    v = wake_detect()
    if v == 2:
        print("Sorry sir, I couldn't find any wakeword . Anyways you can try the limited functions mentioned below")
        speak("Sorry sir, I couldn't find any wakeword . Anyways you can try the limited functions mentioned below")
        print("1.Search topics\n2.Open/ Close applications\n3.Entertain\n4.System Control (Volume control etc..)\n5.Ask jokes")
    else:
        wishMe()
    while True :
        text = takeCommand()
        for site in sites:
            if f'open {site}'.lower() in text.lower():
                print(f"Linux Assistant: Opening {site} ")
                speak(f'Opening {site} ')
                webbrowser.open(sites[site])

        for m in media:
            if f'play {m}'.lower() in text.lower():
                print("Linux Assistant: Playing {}".format(m))
                speak(f'Playing {m} ')
                if m == 'songs':
                    os.system(f'rhythmbox {media[m]} * ')
                else:
                    os.system(f'vlc {media[m]}')

        for a in apps:
            if f'open {a}'.lower() in text.lower():
                print(f"Linux Assistant: opening {a}")
                speak(f'opening {a}')
                os.system(f'{apps[a]}')
        if 'time' in text.lower():
            time = datetime.datetime.now().strftime("%H:%M")
            print("Linux Assistant :"+time)
            speak(f"the time is {time}")

        elif 'use google' in text.lower():
            print("Linux Assistant : I am Currently not integrated with google intelligence")
            speak('I am Currently not integrated with google intelligence')

        #   --------------bard_use()-----------------
        elif 'project guide' in text.lower():
            print("Linux Assistant : Hello Mister Surender sir,How can i help u")
            speak("Hello Mister Surender sir,How can i help u")
        elif 'good morning' in text.lower():
            print("Linux Assistant : Good Morning Sir")
            speak("Good Morning Sir")
        elif 'how are you' in text.lower():
            print("Linux Assistant : I am fine, Thank you")
            print("Linux Assistant : How are you, Sir")
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in text.lower():
            print("Linux Assistant : It's good to know that you are fine")
            speak("It's good to know that your fine")
            print("Linux Assistant : How can I assist you?")
            speak("How can I Assist you")
        elif 'joke' in text.lower():
            j=pyjokes.get_joke()
            print(j)
            speak(j)

        # Camera
        elif 'take selfie' in text.lower():
            print("Linux Assistant : Please smile:)")
            ec.capture(0, "Photos", "img.jpg")

        # Screenshot
        elif 'screenshot' in text.lower():
            print("Linux Assistant : Screenshot captured")
            os.system("gnome-screenshot --file=this_directory.png")

        # Volume up/down

        elif 'volume up' in text.lower():
            os.system("amixer -D pulse sset Master 10%+")
        elif 'volume down' in text.lower():
            os.system("amixer -D pulse sset Master 10%-")

        # Page up/down
        elif 'scroll up' in text.lower():
            os.system("sleep 0.5 && xdotool key 'Prior'")
        elif 'scroll down' in text.lower():
            os.system("sleep 0.5 && xdotool key 'Next'")

        # -------------------Computer power commands--------------------

        elif 'system sleep' in text.lower():
            print("Linux Assistant : System is about to sleep 3..2..1")
            time.sleep(3)
            os.system("systemctl suspend")
        elif 'system power off' in text.lower():
            print("Linux Assistant : System is shutting down...")
            time.sleep(3)
            os.system("systemctl poweroff")
        elif 'system restart' in text.lower():
            print("Linux Assistant : System is about to restart...")
            time.sleep(3)
            os.system("systemctl reboot -i")
        elif 'system log out' in text.lower():
            print("Linux Assistant : User is logging out...")
            time.sleep(3)
            os.system("systemctl logout")

        # --------------------Bluetooth/Wi-Fi-------------------
        elif 'enable bluetooth' in text.lower():
            print("Linux Assistant : Bluetooth is turned on")
            speak("Bluetooth is turned on")
            os.system("rfkill unblock bluetooth")
        elif 'disable bluetooth' in text.lower():
            print("Linux Assistant : Bluetooth is turned off")
            speak("Bluetooth is turned off")
            os.system("rfkill block bluetooth")
        elif 'enable Wi-Fi' in text.lower():
            print("Linux Assistant : Wi-Fi is turned on")
            speak("Wi-Fi is turned on")
            os.system("nmcli radio wifi on")
        elif 'disable Wi-Fi' in text.lower():
            print("Linux Assistant : Wi-Fi is turned off")
            speak("Wi-Fi is turned off")
            os.system("nmcli radio wifi off")
        # --------------------Write/show notes-------------------------

        elif 'write notes' in text.lower():
            print("Linux Assistant : what do you want me to write, sir")
            speak("what do you want me to write, sir")
            note = takeCommand()
            file = open('demonotes.txt', 'w')
            file.write(note)
        elif 'show notes' in text.lower():
            print("Showing Notes")
            speak("Showing Notes")
            file = open('demonotes.txt', 'r')
            os.system("gedit demonotes.txt")
            print("Linux Assistant :", file.read())
            speak(file.read())

        # ------------------Location-----------------------
        elif 'where is' in text.lower():
            text = text.replace("where is", "")
            location = text
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        # --------------Search google----------------

        elif 'search' in text.lower():
            text = text.replace("search", "")
            webbrowser.open("https://www.google.co.in/search?q=" + text)

        # -------------Wikipedia-----------------

        elif 'wikipedia' in text.lower():
            print('Linux Assistant : Searching Wikipedia...')
            speak('Searching Wikipedia...')
            text = text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=2)
            print("Linux Assistant : According to Wikipedia")
            speak("According to Wikipedia")
            print("Linux Assistant : "+results)
            speak(results)

        # ----------------WEATHER------------------
        elif 'weather' in text.lower():
            weather.get_weather()


        # -----------------Wolframalpha---------------------


        # ----------------Closing Applications------------------

        elif 'close visual studio' in text.lower():
            os.system("killall code")
        elif 'close chrome' in text.lower():
            os.system("killall chrome")
        elif 'close vlc' in text.lower():
            os.system("killall vlc")

        # -----------------Tab open/close----------------------------
        elif 'new tab' in text.lower():
            os.system("sleep 0.5 && xdotool key 'Control+t'")
        elif 'close tab' in text.lower():
            os.system("sleep 0.5 && xdotool key 'Control+w'")
        elif 'exit' in text.lower():
            print("Linux Assistant : Thanks for giving me your time")
            speak("Thanks for giving me your time")
            exit()
