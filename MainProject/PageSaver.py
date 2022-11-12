import os
import time
from selenium import webdriver

class InitializeJS:
    def __init__(self):
        with open("JS/earnings.js") as f:
            self.earnings = f.read()
        with open("JS/avatar.js") as f:
            self.avatar = f.read()

class PageSaver:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.avatar = self.get_avatar()
        self.save_earnings()

    def save_earnings(self):
        cur_path = os.getcwd()
        cur_path = cur_path.replace('\\', '/')
        self.driver.get(f"{cur_path}/HTML/Statements%20-%20OnlyFans.html")
        time.sleep(10)
        self.driver.execute_script(InitializeJS().earnings, '$3,123.00')
        self.driver.execute_script(InitializeJS().avatar, self.avatar)
        with open('HTML/Statements - OnlyFans.html', 'w', encoding='utf8') as f:
            f.write(self.driver.page_source)

    def get_avatar(self) -> str:
        self.driver.get("https://onlyfans.com")
        time.sleep(10)
        return self.driver.execute_script("""
            let avatarBtn = document.querySelectorAll("[class='l-header__menu__item m-avatar-item m-avatar-item']")[0];
            return avatarBtn.getElementsByTagName("img")[0].getAttribute('src');
        """)