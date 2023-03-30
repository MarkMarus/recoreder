from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from threading import Thread
from PageSaver import PageSaver
from WebRecorder import WebRecorder
from Edit import Edit
import subprocess
import time
import pyautogui

class Worker:
    def __init__(self, profile_id: str, dolphin):
        with open('data/profiles_main.txt', encoding='utf8') as f:
            info = [line.strip() for line in f.readlines() if profile_id in line][0].split(' ')
            main_balance = info[1]
            fans = info[2]
            percent = info[3]
            pend_balance = info[4]
        self.dolphin = dolphin
        port = self.dolphin.start_profile(profile_id, headless=False)
        options = webdriver.ChromeOptions()
        options.headless = False
        options.add_argument("--start--maximized")
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        self.driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)
        print('Браузер запущен')
        PageSaver(self.driver, main_balance, fans, percent, pend_balance, profile_id)
        pyautogui.moveTo(30,700)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.keyDown('Fn')
        pyautogui.press('f')
        pyautogui.keyUp('Fn')
        # self.dolphin.stop_profile(profile_id)
        Thread(target=lambda: subprocess.call('python3 -m http.server 1233', shell=True)).start()
        time.sleep(5)
        WebRecorder(self.driver)
        self.dolphin.stop_profile(profile_id)
