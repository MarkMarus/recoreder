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


# macbook air 13 - 646:1400:562:355
# macbook pro - 646:1396:563:354

class WebRecorder:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.first_page()
        time.sleep(5)
        self.second_page()
        time.sleep(5)
        self.third_page()

    def run_localhost(self, number):
        self.console = subprocess.Popen(f'ffmpeg -f avfoundation -r 60 -i "1" video{number}.mp4', stdout=subprocess.PIPE, shell=True)

    def first_page(self):
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant1.html')
        self.to_mobile()
        Thread(target=lambda: self.run_localhost(1)).start()
        time.sleep(5)
        pyautogui.moveTo(456,180)
        pyautogui.dragTo(456, 198, 0.1, button='left')
        pyautogui.moveTo(456,180)
        time.sleep(0.7)
        self.driver.execute_script("""
            window.scrollTo({
                top: -100,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(1)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats")[0];
            elem.className = "p-list-chats m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(3)
        self.driver.execute_script("""
            elem123456 = document.getElementById('reload-image');
            elem123456.click();
        """)
        time.sleep(0.7)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats m-sidebar-visible m-prevent-scrolling")[0];
            elem.className = "p-list-chats";
        """)
        time.sleep(0.01)
        self.driver.execute_script("""
            elem01 = document.querySelectorAll("[data-testid='navstate']")[0];
            elem01.style = "";
            elem123 = document.querySelectorAll("[id='style']")[0];
            elem123.innerHTML = "#first_load { display: none; } #main_page {display: none; }";""")
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem1234 = document.querySelectorAll("[id='style']")[0];
            elem1234.innerHTML = "#logo_loading { display: none; } #main_page {display: none; }";""")
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem123456 = document.querySelectorAll("[id='style']")[0];
            elem123456.innerHTML = "#logo_loading { display: none; } #first_load {display: none; }";""")
        time.sleep(5)
        pyautogui.moveTo(456,180)
        pyautogui.dragTo(456, 198, 0.1, button='left')
        pyautogui.moveTo(456,180)
        time.sleep(0.7)
        self.driver.execute_script("""
            window.scrollTo({
                top: -100,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(15)
        self.console.send_signal(signal.SIGTERM)
        time.sleep(5)
        subprocess.call('ffmpeg -i video1.mp4 -vf "crop=646:1396:563:354" -crf 17 -c:a copy result1.mp4', shell=True)
        subprocess.call('ffmpeg -i result1.mp4 -i HTML/noback.png -filter_complex "[0:v][1:v] overlay=0:0" -c:a copy result/output1.mp4', shell=True)
        os.remove('result1.mp4')
        os.remove('video1.mp4')

    def third_page(self):
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant3.html')
        Thread(target=lambda: self.run_localhost(3)).start()
        time.sleep(5)
        pyautogui.moveTo(456,180)
        pyautogui.dragTo(456, 198, 0.1, button='left')
        pyautogui.moveTo(456,180)
        time.sleep(0.7)
        self.driver.execute_script("""
            window.scrollTo({
                top: -100,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(1)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats")[0];
            elem.className = "p-list-chats m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(5)
        self.driver.execute_script("""
            elem0102 = document.querySelectorAll("[data-testid='mess']")[0];
            elem0102.style = "background-color: rgb(0 175 240 / 10%); border-radius: 50%;";
        """)
        time.sleep(0.1)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats m-sidebar-visible m-prevent-scrolling")[0];
            elem.className = "";
        """)
        time.sleep(0.01)
        self.driver.execute_script("""
            elem010203 = document.querySelectorAll("[data-testid='mess']")[0];
            elem010203.style = "";
            elem001 = document.querySelectorAll("[id = 'style']")[0];
            elem001.innerHTML = "#main_page { display: none; } #send { display: none; } #messages {display: none; }";
        """)
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem01 = document.querySelectorAll("[id = 'style']")[0];
            elem01.innerHTML = "#main_page { display: none; } #send { display: none; } #loading {display: none; }";
        """)
        time.sleep(5)
        self.driver.execute_script("""
            elem001 = document.querySelectorAll("[data-testid='newmess']")[0];
            elem001.style = "color: #0091ea; background-color: #0091ea14; border-radius: 50%; margin-top: -39px;"
            elem007 = document.querySelectorAll("[data-testid='ejjiauf']")[0];
            elem007.style = "margin-bottom: 0;";
        """)
        time.sleep(0.1)
        self.driver.execute_script("""
            elem02 = document.querySelectorAll("[id = 'style']")[0];
            elem02.innerHTML = "#messages { display: none; } #loading { display: none; } #main_page {display: none; }";
        """)
        time.sleep(3)
        self.driver.execute_script("""
            let elem = document.querySelectorAll("[class='']")[0];
            elem.className = "m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(15)
        self.console.send_signal(signal.SIGTERM)
        time.sleep(5)
        subprocess.call('ffmpeg -i video3.mp4 -vf "crop=646:1396:563:354" -crf 17 -c:a copy result3.mp4', shell= True)
        subprocess.call('ffmpeg -i result3.mp4 -i HTML/noback.png -filter_complex "[0:v][1:v] overlay=0:0" -c:a copy result/output3.mp4', shell=True)
        os.remove('result3.mp4')
        os.remove('video3.mp4')

    def second_page(self):
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant2.html')
        Thread(target=lambda: self.run_localhost(2)).start()
        time.sleep(5)
        self.driver.execute_script("""
            window.scrollTo({
                top: 100,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(2)
        self.driver.execute_script("""
            window.scrollTo({
                top: -100,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(1)
        self.driver.execute_script("""
            let elem = document.querySelectorAll("[class='']")[0];
            elem.className = "m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(3)
        self.driver.execute_script("""
            elem0102034 = document.querySelectorAll("[data-testid='prst']")[0];
            elem0102034.style = "color: rgb(1, 175, 240); background-color: rgb(0 175 240 / 5%);";
        """)
        time.sleep(0.1)
        self.driver.execute_script("""
            elem01020345 = document.querySelectorAll("[data-testid='prst']")[0];
            elem01020345.style = "";
            elem0 = document.querySelectorAll("[class='m-sidebar-visible m-prevent-scrolling']")[0];
            elem0.className = "";
        """)
        self.driver.execute_script("""
            elem1 = document.querySelectorAll("[id='style']")[0];
            elem1.innerHTML = "#statement { display: none; } #main_page { display: none; }";
        """)
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem123 = document.querySelectorAll("[id='style']")[0];
            elem123.innerHTML = "#first_load { display: none; } #main_page { display: none; }";
        """)
        time.sleep(5)
        pyautogui.moveTo(456,180)
        pyautogui.dragTo(456, 198, 0.1, button='left')
        pyautogui.moveTo(456,180)
        time.sleep(0.7)
        self.driver.execute_script("""
            window.scrollTo({
                top: -100,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(1)
        self.driver.execute_script("""
            elem01 = document.querySelectorAll("[class='']")[0];
            elem01.className = "p-list-chats m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(2)
        self.driver.execute_script("""
            let elem02 = document.getElementsByClassName("p-list-chats m-sidebar-visible m-prevent-scrolling")[0];
            elem02.className = "p-list-chats";
        """)
        time.sleep(15)
        self.console.send_signal(signal.SIGTERM)
        time.sleep(5)
        subprocess.call('ffmpeg -i video2.mp4 -vf "crop=646:1396:563:354" -crf 17 -c:a copy result2.mp4', shell=True)
        subprocess.call('ffmpeg -i result2.mp4 -i HTML/noback.png -filter_complex "[0:v][1:v] overlay=0:0" -c:a copy result/output2.mp4', shell=True)
        os.remove('result2.mp4')
        os.remove('video2.mp4')

    def to_mobile(self):
        time.sleep(5)
        pyautogui.press('F12')
        time.sleep(2)
        time.sleep(3)
        pyautogui.keyDown('command')
        pyautogui.keyDown('shift')
        pyautogui.keyDown('m')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('command')
        pyautogui.keyUp('m')
        time.sleep(5)
        pyautogui.moveTo(305, 135)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(306, 233)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(532, 135)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(547, 300)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(100, 500)

    def image(self):
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
            subprocess.call('ffmpeg -i HTML/noback.png -vf scale=646:1396:563:354 -y HTML/noback.png', shell=True)
