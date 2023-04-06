import os
import time
import signal
import pyautogui
import subprocess
from threading import Thread
from selenium import webdriver
from time import strftime
from PIL import ImageFont, ImageDraw, Image
import random

with Image.open('noback.png') as img:
    hours = ["01", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "21"]
    hour = strftime("%H")
    I1 = ImageDraw.Draw(img)
    font = ImageFont.truetype('HTML/SF-Pro-Display-Semibold.ttf', 22)
    dot_font = ImageFont.truetype('HTML/SFProDisplay-Regular.ttf', 33)
    if hour not in hours:
        if strftime("%M").startswith("1"):
            I1.text((56, 23), hour, font=font, fill=(255, 255, 255))
            I1.text((81, 12), ".", font=dot_font, fill=(255, 255, 255))
            I1.text((81, 4), ".", font=dot_font, fill=(255, 255, 255))
            I1.text((90, 23), strftime("%M"), font=font, fill=(255, 255, 255))
        else:
            I1.text((56, 23), hour, font=font, fill=(255, 255, 255))
            I1.text((81, 12), ".", font=dot_font, fill=(255, 255, 255))
            I1.text((81, 4), ".", font=dot_font, fill=(255, 255, 255))
            I1.text((90, 23), strftime("%M"), font=font, fill=(255, 255, 255))
    elif hour == "11":
        I1.text((57, 23), hour, font=font, fill=(255, 255, 255))
        I1.text((77, 11), ".", font=dot_font, fill=(255, 255, 255))
        I1.text((77, 3), ".", font=dot_font, fill=(255, 255, 255))
        I1.text((87, 23), strftime("%M"), font=font, fill=(255, 255, 255))
    else:
        I1.text((57, 23), hour, font=font, fill=(255, 255, 255))
        I1.text((80, 11), ".", font=dot_font, fill=(255, 255, 255))
        I1.text((80, 3), ".", font=dot_font, fill=(255, 255, 255))
        I1.text((89, 23), strftime("%M"), font=font, fill=(255, 255, 255))
    img.save('HTML/noback2.png')
    subprocess.call('ffmpeg -i HTML/noback.png -vf scale=646:1400 -y HTML/noback.png', shell=True)
