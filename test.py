from wakeWord_detect import speak
from main import takeCommand
import os
import time
import random
import wikipedia
import requests
from lxml import html
import webbrowser
import ecapture as ec
import os, sys, subprocess
text = takeCommand()
from pynput.keyboard import Key, Controller
keyboard=Controller()

if 'pause music' in text.lower():
     keyboard.press(Key.media_play_pause)