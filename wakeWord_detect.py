import pyttsx3
import speech_recognition as sr
import whisper
import playsound

r = sr.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 60)
tiny_model = whisper.load_model('tiny')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


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
                if 'bot' in text_input.lower().strip():
                    speak('hey there , how can I be of service')
                    playsound.playsound('/home/user/Downloads/dell.mp3')
                    break
                else:
                    print('No Wake Word Found')
            except Exception as e:
                print("Error Transcribing audio!!", e)
                continue
