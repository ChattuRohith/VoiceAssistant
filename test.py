import json

from wakeWord_detect import speak
from main import takeCommand
import os
import time
import random
import wikipedia
import requests
from lxml import html
import webbrowser
import vlc
import ecapture as ec
import os, sys, subprocess
text = takeCommand()
# from pynput.keyboard import Key, Controller
# keyboard=Controller()
# if 'pause music' in text.lower():
#      keyboard.press(Key.media_play_pause)
# import vlc
# p = vlc.MediaPlayer("/home/user/Videos/Hi_Nanna.mkv")
# p.play()
# import pygame
from urllib.request import urlopen
# from newsdataapi import NewsDataApiClient
# if "news" in text.lower():
#     api=NewsDataApiClient(apikey="pub_35977e4e677390a3c1e2e98d7b28ac3a174a4")
#     response=api.sources_api("in")
#     print(response)
    # try:
    #     jsonObj = urlopen("https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey='pub_35977e4e677390a3c1e2e98d7b28ac3a174a4'")
    #     data = json.load(jsonObj)
    #     i = 1
    #     speak("Here are some top news from times of india")
    #     print('''=============== TIMES OF INDIA ============''' + '\n')
    #
    #     for item in data['articles']:
    #         print(str(i) + '. ' + item['title'] + '\n')
    #         print(item['description'] + '\n')
    #         speak(str(i) + '. ' + item['title'] + '\n')
    #         i += 1
    # except Exception as e:
    #     print(str(e))
# def NewsFromIndia():
#     query_params={
#         "source":"the-times-of-india",
#         "sortBy":"top",
#         "apiKey":"pub_35977e4e677390a3c1e2e98d7b28ac3a174a4"
#     }
#     main_url="https://newsapi.org/v1/articles"
#     res=requests.get(main_url,params=query_params)
#     open_india_page=res.json()
#     article = open_india_page["articles "]
#     results = []
#     for ar in article:
#         results.append(ar["title"])
#     for i in range(len(results)):
#         print(i + 1, results[i])
#     print(results)
#     speak(results)
# if 'news' in text.lower():
#     NewsFromIndia()
if 'play movies' in text.lower():
        # media_player = vlc.MediaPlayer()
        # media = vlc.Media("Hi_Nanna.mkv")
        # media_player.set_media(media)
        # media_player.play()
        # time.sleep(10)
        os.system('vlc Hi_Nanna')