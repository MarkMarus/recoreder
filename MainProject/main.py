import configparser
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from DolphinAPI import DolphinAPI
from PageSaver import PageSaver

class Worker:
    def __init__(self):
        profile_id = '23242730'
        self.config = configparser.ConfigParser()
        self.config.read("app.conf")
        self.dolphin = DolphinAPI(self.config)
        port = self.dolphin.start_profile(profile_id)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        self.driver = webdriver.Chrome(service=Service('chromedriver.exe'), options=options)
        PageSaver(self.driver)

if __name__ == "__main__":
    Worker()