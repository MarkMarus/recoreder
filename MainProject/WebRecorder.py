import os
import time
import pyautogui
import subprocess
from threading import Thread
from selenium import webdriver
from time import strftime
from PIL import ImageFont, ImageDraw, Image


class WebRecorder:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.first_page()
        time.sleep(5)
        self.second_page()
        time.sleep(5)
        self.third_page()

    def first_page(self):
        res = pyautogui.size()
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant1.html')
        self.to_mobile()
        Thread(target=lambda: subprocess.call('ffmpeg -f avfoundation -r 60 -t 22 -s {res} -i "1" video1.mp4', shell=True)).start()
        time.sleep(5)
        pyautogui.moveTo(456,208)
        pyautogui.dragTo(456, 180, 0.1, button='left')
        pyautogui.moveTo(456,208)
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
            elem123.innerHTML = "#first_load { display: none; } #second_load { display: none; } #main_page {display: none; }";""")
        time.sleep(0.2)
        self.driver.execute_script("""
            elem1234 = document.querySelectorAll("[id='style']")[0];
            elem1234.innerHTML = "#logo_loading { display: none; } #second_load { display: none; } #main_page {display: none; }";""")
        time.sleep(0.2)
        self.driver.execute_script("""
            elem12345 = document.querySelectorAll("[id='style']")[0];
            elem12345.innerHTML = "#logo_loading { display: none; } #first_load { display: none; } #main_page {display: none; }";""")
        time.sleep(0.2)
        self.driver.execute_script("""
            elem123456 = document.querySelectorAll("[id='style']")[0];
            elem123456.innerHTML = "#logo_loading { display: none; } #second_load { display: none; } #first_load {display: none; }";""")
        time.sleep(5)
        pyautogui.moveTo(456,208)
        pyautogui.dragTo(456, 180, 0.1, button='left')
        pyautogui.moveTo(456,208)
        time.sleep(0.7)
        self.driver.execute_script("""
            window.scrollTo({
                top: -100,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(15)
        subprocess.call('ffmpeg -i video1.mp4 -vf "crop=619:1346:580:410" -c:v libx264 -crf 17 -c:a copy cropped.mp4', shell=True)
        subprocess.call('ffmpeg -i cropped.mp4 -vf "crop=619:1346:580:410" -c:v libx264 -crf 17 -c:a copy result1.mp4', shell=True)
        subprocess.call('ffmpeg -i result1.mp4 -i HTML/noback.png -filter_complex "[0:v][1:v] overlay=0:0" -c:a copy result/output1.mp4', shell=True)
        os.remove('result1.mp4')
        os.remove('video1.mp4')

    def third_page(self):
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant3.html')
        Thread(target=lambda: subprocess.run('ffmpeg -f avfoundation -r 60 -t 30 -s 1366x768 -i "1"  video3.mp4', shell=True)).start()
        time.sleep(5)
        pyautogui.moveTo(456,208)
        pyautogui.dragTo(456, 180, 0.1, button='left')
        pyautogui.moveTo(456,208)
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
        time.sleep(0.3)
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
        subprocess.call('ffmpeg -i video3.mp4 -vf "crop=619:1346:580:410" -c:v libx264 -crf 17 -c:a copy result3.mp4', shell= True)
        subprocess.call('ffmpeg -i result3.mp4 -i HTML/noback.png -filter_complex "[0:v][1:v] overlay=0:0" -c:a copy result/output3.mp4', shell=True)
        os.remove('result3.mp4')
        os.remove('video3.mp4')

    def second_page(self):
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant2.html')
        Thread(target=lambda: subprocess.run('ffmpeg -f avfoundation -r 60 -t 30 -s 1366x768 -i "1" video2.mp4', shell=True)).start()
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
            elem1.innerHTML = "#second_load { display: none; } #statement { display: none; } #main_page { display: none; }";
        """)
        time.sleep(0.2)
        self.driver.execute_script("""
            elem12 = document.querySelectorAll("[id='style']")[0];
            elem12.innerHTML = "#first_load { display: none; } #statement { display: none; } #main_page { display: none; }";
        """)
        time.sleep(0.2)
        self.driver.execute_script("""
            elem123 = document.querySelectorAll("[id='style']")[0];
            elem123.innerHTML = "#first_load { display: none; } #second_load { display: none; } #main_page { display: none; }";
        """)
        time.sleep(5)
        pyautogui.moveTo(456,208)
        pyautogui.dragTo(456, 180, 0.1, button='left')
        pyautogui.moveTo(456,208)
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
        subprocess.call('ffmpeg -i video2.mp4 -vf "crop=619:1346:580:410" -c:v libx264 -crf 17 -c:a copy result2.mp4', shell=True)
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
        pyautogui.moveTo(305, 145)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(306, 251)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(532, 145)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(547, 312)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(100, 500)

    def image(self):
        with Image.open('noback.png') as img:
            I1 = ImageDraw.Draw(img)
            font = ImageFont.truetype('HTML/SFProDisplay-Regular.ttf', 21)
            I1.text((60, 22), strftime("%H:%M"), font=font, fill=(255, 255, 255))
            img.save('HTML/noback.png')
