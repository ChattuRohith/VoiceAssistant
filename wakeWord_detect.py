import pyttsx3
import speech_recognition as sr
import whisper
import playsound

r = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty("voices")
engine.setProperty('rate', rate-60)
engine.setProperty('voice', 'english_rp+f3')
tiny_model = whisper.load_model('tiny.en')
base_model = whisper.load_model('base')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Command_input():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        try:
            print("Listening....")
            audio = r.listen(source, 10, 8)
            with open('query.wav','wb') as f:
                f.write(audio.get_wav_data())
            print('Recognizing')
            result = base_model.transcribe('query.wav')
            query_text = result['text']
            print("User Said: ", query_text)
            if len(query_text.strip()) == 0:
                speak("Empty command")
                print("Try saying...\nPlay songs\nOpen youtube\nTell jokes")
        except Exception as e:
            print("Error transcribing audio:", e)
            speak("Error transcribing audio:{}".format(e))
    return query_text


def wake_detect():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                print('To Wake the assistant Say "john" or "bot"')
                audio = r.listen(source, 10, 5)
                with open("wake_detect.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                result = tiny_model.transcribe('wake_detect.wav')
                text_input = result['text']
                if 'bot' in text_input.lower().strip() or 'john' in text_input.lower().strip():
                    playsound.playsound('/home/user/Downloads/dell.mp3')
                    speak('hello sir , how can I be of service')
                    break
                else:
                    print('No Wake Word Found')
            except Exception as e:
                print("Error Transcribing audio!!", e)
                continue
