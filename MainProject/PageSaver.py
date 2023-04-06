import re
import time
import pycountry
from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
import pandas as pd
import ssl

class PageSaver:
    def __init__(self, driver: webdriver, main_balance, fans, percent, pend_balance, profile_id, follows):
        self.main_balance = main_balance
        self.fans = int(fans)
        if self.fans < 1000:
            self.short_fans = self.fans
            self.short_fans = str(self.short_fans)
        else:
            self.short_fans = round(self.fans / 1000, 1)
            if str(self.short_fans).endswith('.0'):
                self.short_fans = int(self.short_fans)
            self.short_fans = f'{self.short_fans}K'
        self.follows = int(follows)
        if self.follows < 1000:
            self.follows = str(self.follows)
        else:
            self.follows = round(self.follows/1000, 1)
            if str(self.follows).endswith('.0'):
                self.follows = int(self.follows)
            self.follows = f'{self.follows}K'
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
        self.save_loading()
        self.loadingmsg()
        self.loadingsstate()
        self.save_chats()
        self.save_profile()
        self.save_send()
        self.save_variant_1()
        self.save_variant_2()
        self.save_variant_3()

    def save_payments(self, name, sum, date, time):
        fee = str(round(int(sum) * 0.2, 2)) + '0'
        netto = str(round(int(sum) - float(fee), 2)) + '0'
        sum = str(sum) + '.00'
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
        code = code.replace('SET_FANS', self.short_fans)
        code = code.replace('SET_PROFILE_NAME', self.profile_name)
        code = code.replace('SET_USER_NAME', self.user_name)
        code = code.replace('SET_FOLLOWS', str(self.follows))
        if self.home_value:
            code = code.replace('<!--SET_HOME_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.home_value} </span>')
        if self.msg_value:
            code = code.replace('<!--SET_MSG_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.msg_value} </span>')
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
        code = code.replace('SET_FANS', self.short_fans)
        code = code.replace('SET_PROFILE_NAME', self.profile_name)
        code = code.replace('SET_USER_NAME', self.user_name)
        if self.home_value:
            code = code.replace('<!--SET_HOME_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.home_value} </span>')
        if self.msg_value:
            code = code.replace('<!--SET_MSG_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.msg_value} </span>')
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
        code = code.replace('SET_FANS', self.short_fans)
        code = code.replace('SET_INFO_TEXT', self.info_text)
        code = code.replace('SET_BANNER', 'imgs/banner.png')
        code = code.replace('SET_FOLLOWS', self.follows)
        if self.home_value:
            code = code.replace('<!--SET_HOME_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.home_value} </span>')
        if self.msg_value:
            code = code.replace('<!--SET_MSG_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.msg_value} </span>')
        if self.story:
            with open('HTML/stories.html', encoding='utf-8') as ff:
                code = code.replace('<!-- SET_STORY -->', ff.read())
                code = code.replace('SET_STORY_IMAGE', 'imgs/story.png')
        code = code.replace('SET_AVATAR', 'imgs/avatar.png')
        with open('localhost/Profile.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_send(self):
        with open('HTML/Select users to send them a message - OnlyFans.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_FANFULL', str(self.fans))
        code = code.replace('SET_AVATAR', 'imgs/avatar.png')
        code = code.replace('SET_FANS', self.short_fans)
        code = code.replace('SET_PROFILE_NAME', self.profile_name)
        code = code.replace('SET_USER_NAME', self.user_name)
        code = code.replace('SET_FOLLOWS', self.follows)
        if self.home_value:
            code = code.replace('<!--SET_HOME_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.home_value} </span>')
        if self.msg_value:
            code = code.replace('<!--SET_MSG_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.msg_value} </span>')
        with open('localhost/Send.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_loading(self):
        with open('HTML/2.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_MAIN_BALANCE', self.main_balance)
        code = code.replace('SET_PENDING_BALANCE', self.pend_balance)
        code = code.replace('SET_PERCENT', f'{self.percent}%')
        if self.home_value:
            code = code.replace('<!--SET_HOME_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.home_value} </span>')
        if self.msg_value:
            code = code.replace('<!--SET_MSG_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.msg_value} </span>')
        with open('localhost/js/loading/statements/2.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_variant_1(self):
        with open('HTML/variant1.html', encoding='utf8') as f:
            code = f.read()
        with open('localhost/Statements.html', encoding='utf8') as f:
            code_s = f.read()
        with open('localhost/js/loading/statements/2.html', encoding='utf8') as f:
            code_h = f.read()
        code = code.replace("SET_SECOND", code_h)
        code = code.replace("SET_MAIN", code_s)
        code = code.replace('SET_PERCENT', f'{self.percent}%')
        if self.home_value:
            code = code.replace('<!--SET_HOME_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.home_value} </span>')
        if self.msg_value:
            code = code.replace('<!--SET_MSG_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.msg_value} </span>')
        with open('localhost/variant1.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_variant_2(self):
        with open('HTML/variant2.html', encoding='utf8') as f:
            code = f.read()
        with open('localhost/Profile.html', encoding='utf8') as f:
            code_p = f.read()
        with open('localhost/Statements.html', encoding='utf8') as f:
            code_s = f.read()
        with open('localhost/js/loading/statements/2.html', encoding='utf8') as f:
            code_h = f.read()
        code = code.replace("SET_SECOND", code_h)
        code = code.replace("SET_STATEMENT", code_s)
        code = code.replace("SET_MAIN", code_p)
        code = code.replace('SET_PERCENT', f'{self.percent}%')
        if self.home_value:
            code = code.replace('<!--SET_HOME_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.home_value} </span>')
        if self.msg_value:
            code = code.replace('<!--SET_MSG_VALUE-->', f'<span data-v-27a4a595="" class="l-header__menu__item__count"> {self.msg_value} </span>')
        with open('localhost/variant2.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def save_variant_3(self):
        with open('HTML/variant3.html', encoding='utf8') as f:
            code = f.read()
        with open('localhost/Messages.html', encoding='utf8') as f:
            code_p = f.read()
        with open('localhost/Statements.html', encoding='utf8') as f:
            code_s = f.read()
        with open('localhost/Send.html', encoding='utf8') as f:
            code_h = f.read()
        code = code.replace("SET_MESSAGES", code_p)
        code = code.replace("SET_SEND", code_h)
        code = code.replace("SET_MAIN", code_s)
        with open('localhost/variant3.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def loadingmsg(self):
        with open('HTML/LoadingToMessages.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_AVATAR', 'imgs/avatar.png')
        with open('localhost/js/loading/LoadingToMessages.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def loadingsstate(self):
        with open('HTML/LoadingToStatements.html', encoding='utf8') as f:
            code = f.read()
        code = code.replace('SET_AVATAR', 'imgs/avatar.png')
        with open('localhost/js/loading/LoadingToStatements.html', 'w+', encoding='utf8') as f:
            f.write(code)

    def get_chats(self):
        self.driver.get("https://onlyfans.com/my/chats/")
        time.sleep(10)
        self.chats = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-page-content g-sides-gaps']")[0].innerHTML;
        """)

    def get_profiles_info(self):
        self.driver.get("https://onlyfans.com")
        ssl._create_default_https_context = ssl._create_unverified_context
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
        pattern = re.compile(r'[\U0001F1E6-\U0001F1FF]{2}')
        for match in pattern.findall(self.profile_name):
            country = pycountry.countries.get(alpha_2=match)
            if country is not None:
                flag = chr(ord(country.emoji_flag[0]) + 127397) + chr(ord(country.emoji_flag[1]) + 127397)
                self.profile_name = self.profile_name.replace(match, flag)
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
        try:
            self.home_value = int(self.driver.execute_script("""
                return document.querySelectorAll('[class="l-header__menu__item__icon"]')[0];
                return elem.querySelector('[class="l-header__menu__item__count"]').textContent;
            """))
        except:
            self.home_value = 0
        try:
            self.msg_value = int(self.driver.execute_script("""
                elem = document.querySelectorAll('[class="l-header__menu__item__icon"]')[3];
                return elem.querySelector('[class="l-header__menu__item__count"]').textContent;
            """))
        except:
            self.msg_value = 0
        avatar = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-profile__header__user g-sides-gaps']")[0].getElementsByTagName('img')[0].getAttribute('src');
        """)
        banner = self.driver.execute_script("""
            return document.querySelectorAll("[class='b-profile__header']")[0].getElementsByTagName('img')[0].getAttribute('src');
        """)
        urlretrieve(avatar, 'localhost/imgs/avatar.png')
        urlretrieve(banner, 'localhost/imgs/banner.png')
        urlretrieve(avatar, 'localhost/js/loading/statements/imgs/avatar.png')
        urlretrieve(banner, 'localhost/js/loading/statements/imgs/banner.png')
        try:
            try:
                self.story = self.driver.execute_script("""
                    return document.querySelectorAll("[class='b-story-item__inside m-default-bg']")[0].getElementsByTagName('img')[1].getAttribute('src');
                """)
            except:
                self.story = self.driver.execute_script("""
                    return document.querySelectorAll("[class='b-story-item__inside m-default-bg']")[0].getElementsByTagName('img')[0].getAttribute('src');
                """)
            self.driver.get(self.story)
            self.driver.find_element(By.TAG_NAME, "img").screenshot('localhost/imgs/story.png')
        except:
            self.story = None
