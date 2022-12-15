import os
import time
import pyautogui
import subprocess
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By


class WebRecorder:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.first_page()
        time.sleep(5)
        self.second_page()
        time.sleep(5)
        self.third_page()

    def first_page(self):
        self.driver.get('http://localhost:1233/localhost/Statements.html')
        self.to_mobile()
        Thread(target=lambda: subprocess.call('ffmpeg -f avfoundation -r 60 -t 30 -s 1366x768 -i "1" video1.mp4', shell= True)).start()
        time.sleep(5)
        self.driver.execute_script("""
            window.scrollTo({
                top: 1000,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(5)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats")[0];
            elem.className = "p-list-chats m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(3)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats m-sidebar-visible m-prevent-scrolling")[0];
            elem.className = "p-list-chats";
        """)
        time.sleep(3)
        with open('localhost/js/OnlyFansLogoLoading.html', encoding='utf8') as f:
            code = f.read()
        self.driver.execute_script("""
            let page = document.querySelectorAll("[class='penis']")[0]
            page.innerHTML = arguments[0];
        """, code)
        time.sleep(0.2)
        self.driver.execute_script("""
            let pager = document.querySelectorAll("[class='penis']")[0]
            pager.innerHTML = ' ';
            let elemr = document.querySelectorAll("[id='statements']")[0]
            elemr.innerHTML = arguments[0];
        """, code)
        time.sleep(0.5)
        
        with open('localhost/js/loading/statements/2.html', encoding='utf8') as f:
            code = f.read()
        self.driver.execute_script("""
            let elem = document.querySelectorAll("[id='statements']")[0]
            elem.innerHTML = arguments[0];
        """, code)
        time.sleep(0.5)
        with open('localhost/Statements.html', encoding='utf8') as f:
            code = f.read()
        self.driver.execute_script("""
            let blyat = document.querySelectorAll("[id='statements']")[0]
            blyat.innerHTML = arguments[0];
        """, code)
        # self.driver.get("http://localhost:1233/localhost/js/loading/statements/1.html")
        time.sleep(5)
        self.driver.execute_script("""
            window.scrollTo({
                top: 1303,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(15)
        subprocess.call('ffmpeg -i video1.mp4 -vf "crop=619:1346:580:410" -c:v libx264 -crf 17 -c:a copy result1.mp4', shell= True)
        # subprocess.call('''ffmpeg -i result1.mkv -i Untitled.mp4 -filter_complex '[1:v]colorkey=0x00ff00:0.1:[ckout];[0:v][ckout]overlay[out]' -map '[out]' result1.mp4''', shell=True)
        # os.remove('result1.mp4')
        # os.remove('video1.mp4')

    def third_page(self):
        self.driver.get('http://localhost:1233/localhost/Statements.html')
        Thread(target=lambda: subprocess.run('ffmpeg -f avfoundation -r 60 -t 30 -s 1366x768 -i "1"  video3.mp4', shell= True)).start()
        time.sleep(5)
        self.driver.execute_script("""
            window.scrollTo({
                top: 1368,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(2)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats")[0];
            elem.className = "p-list-chats m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(5)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats m-sidebar-visible m-prevent-scrolling")[0];
            elem.className = "p-list-chats";
        """)
        time.sleep(3)
        self.driver.get("http://localhost:1233/localhost/js/loading/LoadingToMessages.html")
        time.sleep(5)
        self.driver.get("http://localhost:1233/localhost/Send.html")
        time.sleep(3)
        self.driver.execute_script("""
            let elem = document.querySelectorAll("[class='']")[0];
            elem.className = "m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(15)
        subprocess.call('ffmpeg -i video3.mp4 -vf "crop=619:1346:580:410" -c:v libx264 -crf 17 -c:a copy result3.mp4', shell= True)
        # subprocess.call('''ffmpeg -i result3.mkv -i Untitled.mp4 -filter_complex '[1:v]colorkey=0x00ff00:0.1:[ckout];[0:v][ckout]overlay[out]' -map '[out]' result3.mp4''', shell=True)
        # os.remove('result3.mkv')
        # os.remove('video3.mp4')

    def second_page(self):
        self.driver.get('http://localhost:1233/localhost/Profile.html')
        Thread(target=lambda: subprocess.run('ffmpeg -f avfoundation -r 60 -t 30 -s 1366x768 -i "1" video2.mp4', shell= True)).start()
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
            let elem = document.querySelectorAll("[class='']")[0];
            elem.className = "m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(3)
        self.driver.get("http://localhost:1233/localhost/js/loading/LoadingToStatements.html")
        time.sleep(5)
        self.driver.execute_script("""
            window.scrollTo({
                top: 1368,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(4)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats")[0];
            elem.className = "p-list-chats m-sidebar-visible m-prevent-scrolling";
        """)
        time.sleep(2)
        self.driver.execute_script("""
            let elem = document.getElementsByClassName("p-list-chats m-sidebar-visible m-prevent-scrolling")[0];
            elem.className = "p-list-chats";
        """)
        time.sleep(15)
        subprocess.call('ffmpeg -i video2.mp4 -vf "crop=619:1346:580:410" -c:v libx264 -crf 17 -c:a copy result2.mp4', shell= True)
        # subprocess.call('''ffmpeg -i result2.mkv -i Untitled.mp4 -filter_complex '[1:v]colorkey=0x00ff00:0.1:[ckout];[0:v][ckout]overlay[out]' -map '[out]' result2.mp4''', shell=True)
        # os.remove('result2.mkv')
        # os.remove('video2.mp4')

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
        pyautogui.moveTo(0, 0)
