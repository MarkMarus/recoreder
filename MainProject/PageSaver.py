import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlretrieve
import pandas as pd

class PageSaver:
    def __init__(self, driver: webdriver, main_balance, fans, percent, pend_balance, profile_id):
        self.main_balance = main_balance
        self.fans = int(fans)
        if self.fans < 1000:
            self.short_fans = self.fans
        else:
            self.short_fans = round(self.fans / 1000, 1)
            if str(self.short_fans).endswith('.0'):
                self.short_fans = int(self.short_fans)
        self.percent = percent
        self.pend_balance = pend_balance
        data = pd.read_csv('./data/transactions.csv')
        transactions = data.loc[data['ID'] == int(profile_id)]
        name = [transactions.iloc[i]['Name'] for i in range(len(transactions))]
        sum = [transactions.iloc[i]['Sum'] for i in range(len(transactions))]
        date = [transactions.iloc[i]['Date'] for i in range(len(transactions))]
        time = [transactions.iloc[i]['Time'] for i in range(len(transactions))]
        self.transactions = list(zip(name, sum, date, time))
        self.driver = driver
        self.get_profiles_info()
        self.get_chats()
        self.save_earnings()
        self.save_chats()
        self.save_profile()
        self.save_send()

    def save_payments(self, name, sum, date, time):
        fee = int(int(sum) * 0.2)
        netto = int(int(sum) - fee)
        with open('HTML/Payment.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_DATE', date)
        code = code.replace('SET_TIME', time)
        code = code.replace('SET_AMOUNT', str(sum))
        code = code.replace('SET_FEE', str(fee))
        code = code.replace('SET_NETTO', str(netto))
        code = code.replace('SET_NAME', name)
        return code

    def save_earnings(self):
        with open('HTML/Statements - OnlyFans.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_MAIN_BALANCE', self.main_balance)
        code = code.replace('SET_PENDING_BALANCE', self.pend_balance)
        code = code.replace('SET_PERCENT', f'{self.percent}%')
        code = code.replace('SET_AVATAR', 'imgs/avatar.png')
        code = code.replace('SET_PAYMENTS', '0')
        code = code.replace('SET_FANS', f'{self.short_fans}k')
        code = code.replace('SET_PROFILE_NAME', self.profile_name)
        code = code.replace('SET_USER_NAME', self.user_name)
        for i in self.transactions:
            payment = self.save_payments(i[0], i[1], i[2], i[3])
            code = code.replace('<!--SET_PAYMENT-->', payment)
        with open('localhost/Statements.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_chats(self):
        with open('HTML/Messages - OnlyFans.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('PASTE_CHATS', self.chats)
        code = code.replace('SET_AVATAR', 'imgs/avatar.png')
        code = code.replace('SET_FANS', f'{self.short_fans}k')
        code = code.replace('SET_PROFILE_NAME', self.profile_name)
        code = code.replace('SET_USER_NAME', self.user_name)
        with open('localhost/Messages.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_profile(self):
        with open('HTML/Profile.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_PROFILE_NAME', self.profile_name)
        code = code.replace('SET_USER_NAME', self.user_name)
        code = code.replace('SET_POSTS', self.posts_value)
        code = code.replace('SET_MEDIA_VALUE', self.media_value)
        code = code.replace('SET_LIKES', self.likes_value)
        code = code.replace('SET_FANS', f'{self.short_fans}K')
        code = code.replace('SET_INFO_TEXT', self.info_text)
        code = code.replace('SET_BANNER', 'imgs/banner.png')
        code = code.replace('SET_AVATAR', 'imgs/avatar.png')
        code = code.replace('SET_STORY_IMAGE', 'imgs/story.png')
        with open('localhost/Profile.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_send(self):
        with open('HTML/Select users to send them a message - OnlyFans.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_FANS_FULL', str(self.fans))
        code = code.replace('SET_AVATAR', 'imgs/avatar.png')
        code = code.replace('SET_FANS', f'{self.short_fans}k')
        code = code.replace('SET_PROFILE_NAME', self.profile_name)
        code = code.replace('SET_USER_NAME', self.user_name)
        with open('localhost/Send.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def get_chats(self):
        self.driver.get("https://onlyfans.com/my/chats/")
        time.sleep(10)
        self.chats = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-chats__list-dialogues']")[0].innerHTML;
        """)

    def get_profiles_info(self):
        self.driver.get("https://onlyfans.com")
        while True:    
            try:
                self.driver.execute_script("""
                    document.querySelectorAll("[data-name='Profile']")[0].click();
                """)
                break
            except:
                time.sleep(2)
        time.sleep(10)
        self.profile_name = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-username']")[0].textContent;
        """)
        self.user_name = '@' + re.findall(".com/(.+)", self.driver.current_url)[0]
        self.posts_value = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-profile__sections__count']")[0].textContent;
        """)
        self.likes_value = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-profile__sections__count']")[1].textContent;
        """)
        self.media_value = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-tabs__nav__link__counter-title']")[1].textContent;
        """)
        self.info_text = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-user-info__text m-break-word']")[0].innerHTML;
        """)
        avatar = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-profile__header__user g-sides-gaps']")[0].getElementsByTagName('img')[0].getAttribute('src');
        """)
        banner = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-profile__header']")[0].getElementsByTagName('img')[0].getAttribute('src');
        """)
        story = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-story-item__inside m-default-bg']")[0].getElementsByTagName('img')[1].getAttribute('src');
        """)
        urlretrieve(avatar, 'localhost/imgs/avatar.png')
        urlretrieve(banner, 'localhost/imgs/banner.png')
        self.driver.get(story)
        self.driver.find_element(By.TAG_NAME, "img").screenshot('localhost/imgs/story.png')
