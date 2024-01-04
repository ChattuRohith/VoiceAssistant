import datetime
import webbrowser
import os
import whisper
import subprocess
import speech_recognition as sr
import sounddevice
from wakeWord_detect import wake_detect
from wakeWord_detect import speak
# from gbard import bard_use
import warnings


warnings.filterwarnings("ignore", message='FP16 is not supported on CPU; using FP32 instead')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 10, 3)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("I am sorry, I am Unable to Recognize your voice.")
        return "None"

    return query


if __name__ == '__main__':
    wake_detect()
    while True:
        text = takeCommand()
        if text == "":
            print("Try saying...\nPlay songs\nOpen youtube\nTell jokes")
            continue
        sites = {'youtube': 'https://youtube.com', 'instagram': 'https://instagram.com', 'gmail': 'https://gmail.com',
                 'r g u k t': 'https://rgukt.ac.in', 'rgukt hub': 'https://hub.rgukt.ac.in',
                 'wikipedia': 'https://wikipedia.com'}
        for site in sites:
            if f'open {site}'.lower() in text.lower():
                print(f"Linux Assistant: Opening {site} ")
                speak(f'Opening {site} Master')
                webbrowser.open(sites[site])
        media = {'songs': '~/home/user/Music', 'movie': '~/home/user/Videos'}
        for m in media:
            if f'play {m}'.lower() in text.lower():
                print("Linux Assistant: Playing {}".format(m))
                speak(f'Playing {m} ')
                if m == 'songs':
                    os.system(f'rhythmbox {media[m]} * ')
                else:
                    os.system(f'vlc {media[m]} * ')

        if 'the time' in text.lower():
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {time}")
        apps = {'chrome': 'google-chrome', 'Visual Studio': 'code', 'V L C': 'vlc'}
        for a in apps:
            if f'open {a}'.lower() in text.lower():
                print(f"Linux Assistant: opening {a}")
                speak(f'opening {a}')
                os.system(f'{apps[a]}')
        if 'use google' in text.lower():
            print("Linux Assistant : I am Currently no t integrated with google intelligence")
            speak('I am Currently not integrated with google intelligence')

        #     bard_use()

        if 'exit'.lower() in text.lower():
            exit()
