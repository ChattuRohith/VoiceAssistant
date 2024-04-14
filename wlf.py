# Wolf ram alpha API

import wolframalpha
import speech_recognition as sr
from wakeWord_detect import speak
import sounddevice
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

    return query
# Taking input from user
print('Ask any Query/Doubt/Math Calculations etc..')
question = takeCommand()

# App id obtained by the above steps
app_id = 'Y8K4RR-3#######VT'

# Instance of wolf ram alpha
# client class

client = wolframalpha.Client(app_id)

# Stores the response from
# wolf ram alpha
res = client.query(question)

# Includes only text from the response
answer = next(res.results).text

print(f" Linux Assistant: {answer}")
speak(answer)
