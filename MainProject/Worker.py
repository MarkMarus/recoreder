import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from PageSaver import PageSaver

class Worker:
    def __init__(self, profile_id: str, dolphin):
        self.dolphin = dolphin
        port = self.dolphin.start_profile(profile_id)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        self.driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)
        PageSaver(self.driver)
        self.dolphin.stop_profile(profile_id)
        os.system('python -m http.server 1337')