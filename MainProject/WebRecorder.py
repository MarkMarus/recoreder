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
        # self.third_page()

    def first_page(self):
        self.driver.get('http://localhost:1233/localhost/Statements.html')
        self.to_mobile()
        Thread(target=lambda: subprocess.run("ffmpeg -f gdigrab -framerate 30 -i desktop -t 30 video/output1.mp4")).start()
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
        self.driver.get("http://localhost:1233/localhost/js/loading/statements/1.html")
        time.sleep(5)
        self.driver.execute_script("""
            window.scrollTo({
                top: 1303,
                left: 0,
                behavior: 'smooth'
            });
        """)
        time.sleep(5)
        subprocess.run('ffmpeg -i video/output1.mp4 -filter:v "crop=300:534:255:169" video/1.mp4')
        os.remove('video/output2.mp4')

    def second_page(self):
        self.driver.get('http://localhost:1233/localhost/Statements.html')
        self.to_mobile()
        Thread(target=lambda: subprocess.run("ffmpeg -f gdigrab -framerate 30 -i desktop -t 34 video/output2.mp4")).start()
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
        time.sleep(5)
        subprocess.run('ffmpeg -i video/output2.mp4 -filter:v "crop=300:534:255:169" video/2.mp4')
        os.remove('video/output2.mp4')

    def third_page(self):
        self.driver.get('http://localhost:1233/localhost/Profile.html')
        self.to_mobile()
        Thread(target=lambda: subprocess.run("ffmpeg -f gdigrab -framerate 35 -i desktop -t 34 video/output3.mp4")).start()
        time.sleep(5)
        self.driver.execute_script("""
            window.scrollTo({
                top: 200,
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
        time.sleep(5)
        subprocess.run('ffmpeg -i video/output3.mp4 -filter:v "crop=300:534:255:169" video/3.mp4')
        os.remove('video/output3.mp4')

    def to_mobile(self):
        time.sleep(5)
        pyautogui.press('F12')
        time.sleep(5)
        try:
            point = pyautogui.locateCenterOnScreen('img.png')
            pyautogui.moveTo(point)
            pyautogui.click()
            time.sleep(5)
        except:
            pass
        pyautogui.moveTo(307, 118)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(272, 179)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(477, 115)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(543, 302)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(0, 0)
