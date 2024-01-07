from bardapi import Bard
from playsound import playsound
import speech_recognition as sr
import whisper
import warnings
from bardapi import chat
from wakeWord_detect import speak

token = 'Your google bard SSPID1'

bard = Bard(token=token)

r = sr.Recognizer()

base_model = whisper.load_model('base')


def prompt_bard(prompt):
    result = bard.get_answer(prompt)
    return result['content']


# using whisper to recognise the speech
def whisper_recog():
    with sr.Microphone as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                print('Listening ... Speak your query to bard')
                audio = r.listen(source)
                with open("prompt.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                result = base_model.transcribe('prompt.wav')
                if result['language'] != 'en':
                    speak('Please speak in English')
                    print('Language is out of my Knowledge')
                else:
                    query = result['text']
                print('using bard intelligence to answer: ', query, '\n')
                if len(query.strip()) == 0:
                    print('Empty prompt or No prompt recognized')
                    speak("Empty prompt. Please speak again")
                    continue
                else:
                    break
            except Exception as e:
                print("Error recognizing audio :", e)
                continue
    return query


def bard_use():
    query = whisper_recog()
    response = prompt_bard(query)
    print("Linux Assistant: ", response)
    speak(response)
    return response
