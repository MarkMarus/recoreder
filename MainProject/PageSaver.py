import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.request import urlretrieve

class PageSaver:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.get_profiles_info()
        self.get_chats()
        self.save_earnings()
        self.save_chats()
        self.save_profile()
        self.save_send()

    def save_earnings(self):
        with open('HTML/Statements - OnlyFans.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_MAIN_BALANCE', '$1,234.56')
        code = code.replace('SET_PENDING_BALANCE', '$8,910.11')
        code = code.replace('SET_PERCENT', '0.8%')
        code = code.replace('SET_AVATAR', 'avatar.png')
        code = code.replace('SET_PAYMENTS', '0')
        with open('Statements.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_chats(self):
        with open('HTML/Messages - OnlyFans.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('PASTE_CHATS', self.chats)
        code = code.replace('SET_AVATAR', 'avatar.png')
        with open('Messages.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_profile(self):
        with open('HTML/Profile.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_PROFILE_NAME', self.profile_name)
        code = code.replace('SET_USER_NAME', self.user_name)
        code = code.replace('SET_POSTS', self.posts_value)
        code = code.replace('SET_MEDIA_VALUE', self.media_value)
        code = code.replace('SET_LIKES', self.likes_value)
        code = code.replace('SET_FANS', '10K')
        code = code.replace('SET_INFO_TEXT', self.info_text)
        code = code.replace('SET_BANNER', 'banner.png')
        code = code.replace('SET_AVATAR', 'avatar.png')
        code = code.replace('SET_STORY_IMAGE', 'story.png')
        with open('Profile.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_send(self):
        with open('HTML/Select users to send them a message - OnlyFans.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_FANS', '1337')
        code = code.replace('SET_AVATAR', 'avatar.png')
        with open('Send.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def get_chats(self):
        self.driver.get("https://onlyfans.com/my/chats/")
        time.sleep(10)
        self.chats = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-chats__list-dialogues']")[0].innerHTML;
        """)

    def get_profiles_info(self):
        self.driver.get("https://onlyfans.com")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'user_posts'))
        )
        self.driver.execute_script("""
            document.querySelectorAll("[data-name='Profile']")[0].click();
        """)
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
        urlretrieve(avatar, 'avatar.png')
        urlretrieve(banner, 'banner.png')
        self.driver.get(story)
        self.driver.find_element(By.TAG_NAME, "img").screenshot('story.png')