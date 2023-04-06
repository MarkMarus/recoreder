import os
import glob
import random
import shutil
import threading
import time
import pyautogui
import subprocess
from selenium import webdriver
from time import strftime
from PIL import ImageFont, ImageDraw, Image
from win32com.client import Dispatch
import rotatescreen
import pywintypes
import win32api
import win32con
import psutil
import getpass


resolutions_crop = {
    '1920x1080': '578:1264:124:140',
    '1366x768': '484:1046:16:138'
}

resolutions_click = {
    '1920x1080': [(1409, 141), (548, 85), (547, 195), (772, 79), (830, 208), (1661, 409)],
    '1366x768': [(854, 139), (267, 84), (281, 192), (500, 82), (552, 182), (1154, 217)]
}

resolutions_move = {
    '1920x1080': [(1366, 579), (1919, 579)],
    '1366x768': [(812, 296), (1365, 296)]
}


class WebRecorder:
    def __init__(self, driver: webdriver):
        custom = False
        if int(pyautogui.size()[0]) > 1920:
            self.width = pyautogui.size()[0]
            self.height = pyautogui.size()[1]
            self.res()
            custom = True
        pyautogui.FAILSAFE = False
        self.obs_settings()
        self.screen = rotatescreen.get_primary_display()
        self.resolution = f'{pyautogui.size()[0]}x{pyautogui.size()[1]}'
        self.driver = driver
        self.first_page()
        print('1+')
        time.sleep(5)
        print('1++')
        self.second_page()
        print('2+')
        time.sleep(5)
        print('2++')
        self.third_page()
        print('3+')
        self.screen.rotate_to(0)
        if custom:
            self.res(self.width, self.height)
        time.sleep(1)

    def res(self, width=1920, height=1080):
        devmode = pywintypes.DEVMODEType()
        devmode.PelsWidth = width
        devmode.PelsHeight = height

        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

        win32api.ChangeDisplaySettings(devmode, 0)

    def first_page(self):
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant1.html')
        self.to_mobile()
        time.sleep(1)
        threading.Thread(target=lambda: subprocess.call('obs.lnk --minimize-to-tray --startrecording --scene "variant1"', shell=True)).start()
        time.sleep(8)
        self.driver.execute_script('''
            window.scrollTo({
                top: 1500,
                behavior: "smooth"
            })
        ''')
        time.sleep(0.7)
        self.driver.execute_script('''
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            })
        ''')
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
            elem123.innerHTML = "#first_load { display: none; } #main_page {display: none; }";""")
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem1234 = document.querySelectorAll("[id='style']")[0];
            elem1234.innerHTML = "#logo_loading { display: none; } #main_page {display: none; }";""")
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem123456 = document.querySelectorAll("[id='style']")[0];
            elem123456.innerHTML = "#logo_loading { display: none; } #first_load {display: none; }";""")
        time.sleep(5)
        self.driver.execute_script('''
            window.scrollTo({
                top: 1500,
                behavior: "smooth"
            })
        ''')
        time.sleep(0.7)
        self.driver.execute_script('''
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            })
        ''')
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
            elem123.innerHTML = "#first_load { display: none; } #main_page {display: none; }";""")
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem1234 = document.querySelectorAll("[id='style']")[0];
            elem1234.innerHTML = "#logo_loading { display: none; } #main_page {display: none; }";""")
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem123456 = document.querySelectorAll("[id='style']")[0];
            elem123456.innerHTML = "#logo_loading { display: none; } #first_load {display: none; }";""")
        time.sleep(5)
        self.driver.execute_script('''
            window.scrollTo({
                top: 1500,
                behavior: "smooth"
            })
        ''')
        time.sleep(0.7)
        self.driver.execute_script('''
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            })
        ''')
        time.sleep(5)
        has = True
        while has:
            for proc in psutil.process_iter():
                if proc.name() == "obs64.exe":
                    proc.kill()
            time.sleep(1)
            processes = [name.name() for name in psutil.process_iter()]
            if "obs64.exe" not in processes:
                break
        time.sleep(5)
        thread = threading.Thread(target=self.ffmpeg, args=("1",))
        thread.start()
        thread.join()

    def third_page(self):
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant3.html')
        time.sleep(1)
        threading.Thread(target=lambda: subprocess.call('obs.lnk --minimize-to-tray --startrecording --scene "variant3"', shell=True)).start()
        time.sleep(8)
        self.driver.execute_script('''
            window.scrollTo({
                top: 1500,
                behavior: "smooth"
            })
        ''')
        time.sleep(0.7)
        self.driver.execute_script('''
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            })
        ''')
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
        time.sleep(random.uniform(0.5, 1.5))
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
        time.sleep(5)
        has = True
        while has:
            for proc in psutil.process_iter():
                if proc.name() == "obs64.exe":
                    proc.kill()
            time.sleep(1)
            processes = [name.name() for name in psutil.process_iter()]
            if "obs64.exe" not in processes:
                break
        time.sleep(5)
        thread = threading.Thread(target=self.ffmpeg, args=("3",))
        thread.start()
        thread.join()

    def second_page(self):
        self.image()
        self.driver.get('http://localhost:1233/localhost/variant2.html')
        time.sleep(1)
        threading.Thread(target=lambda: subprocess.call('obs.lnk --minimize-to-tray --startrecording --scene "variant2"', shell=True)).start()
        time.sleep(8)
        self.driver.execute_script('''
            window.scrollTo({
                top: 100,
                behavior: "smooth"
            })
        ''')
        time.sleep(0.7)
        self.driver.execute_script('''
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            })
        ''')
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
            elem1.innerHTML = "#statement { display: none; } #main_page { display: none; }";
        """)
        time.sleep(random.uniform(0.5, 1.5))
        self.driver.execute_script("""
            elem123 = document.querySelectorAll("[id='style']")[0];
            elem123.innerHTML = "#first_load { display: none; } #main_page { display: none; }";
        """)
        time.sleep(5)
        self.driver.execute_script('''
            window.scrollTo({
                top: 1500,
                behavior: "smooth"
            })
        ''')
        time.sleep(0.7)
        self.driver.execute_script('''
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            })
        ''')
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
        time.sleep(5)
        has = True
        while has:
            for proc in psutil.process_iter():
                if proc.name() == "obs64.exe":
                    proc.kill()
            time.sleep(1)
            processes = [name.name() for name in psutil.process_iter()]
            if "obs64.exe" not in processes:
                break
        time.sleep(5)
        thread = threading.Thread(target=self.ffmpeg, args=("2",))
        thread.start()
        thread.join()

    def to_mobile(self):
        resol_clicks = resolutions_click[self.resolution]
        resol_move = resolutions_move[self.resolution]
        time.sleep(1)
        pyautogui.keyDown('F12')
        pyautogui.keyUp('F12')
        time.sleep(2)
        pyautogui.moveTo(resol_clicks[5])
        pyautogui.click()
        pyautogui.moveTo(resol_clicks[5])
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(resol_clicks[0])
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(resol_clicks[1])
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(resol_clicks[2])
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(resol_clicks[3])
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(resol_clicks[4])
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(resol_move[0])
        pyautogui.mouseDown()
        time.sleep(0.5)
        pyautogui.moveTo(resol_move[1])
        pyautogui.mouseUp()
        time.sleep(1)
        self.screen.rotate_to(90)
        time.sleep(0.5)
        pyautogui.moveTo(0, 0)

    def ffmpeg(self, number):
        video = glob.glob("*.avi")[0]
        print(1)
        subprocess.call(f'ffmpeg -i {video} -ss 00:00:02 -y video{number}.mp4')
        print(2)
        subprocess.call(f'ffmpeg -i video{number}.mp4 -c copy -an -y no_sound{number}.mp4')
        print(3)
        subprocess.call(f'ffmpeg -i no_sound{number}.mp4 -vf "crop={resolutions_crop[self.resolution]}" -qscale 0 -crf 0 -c:a copy -y result{number}.mp4')
        print(4)
        subprocess.call(f'ffmpeg -i result{number}.mp4 -i 123.mp3 -y sound{number}.mp4', shell=True)
        print(5)
        subprocess.call(f'ffmpeg -i sound{number}.mp4 -i HTML/noback.png -filter_complex "[0:v][1:v] overlay=0:0" -qscale 0 -c:a copy with_image{number}.mp4')
        print(6)
        subprocess.call(
            f'ffmpeg -i with_image{number}.mp4 -vf "scale=1080:2340" -y result/output{number}.mp4',
            shell=True)
        print(7)
        os.remove(f'video{number}.mp4')
        print(8)
        os.remove(f'no_sound{number}.mp4')
        print(9)
        os.remove(f'result{number}.mp4')
        print(10)
        os.remove(video)
        print(11)
        os.remove(f'sound{number}.mp4')
        print(12)
        os.remove(f'with_image{number}.mp4')
        print(13)

    def obs_settings(self):
        for proc in psutil.process_iter():
            if proc.name() == "obs64.exe":
                proc.kill()
        target = os.getcwd() + r"\obs-studio\bin\64bit"
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut("obs.lnk")
        shortcut.Targetpath = target + r"\obs64.exe"
        shortcut.WorkingDirectory = target
        shortcut.IconLocation = target + r"\obs64.exe"
        shortcut.save()
        threading.Thread(target=lambda: subprocess.call("obs.lnk --minimize-to-tray", shell=True)).start()
        time.sleep(3)
        for proc in psutil.process_iter():
            if proc.name() == "obs64.exe":
                proc.kill()
                break
        if os.path.exists(f"{os.getenv('APPDATA')}\\obs-studio\\basic\\profiles\\Без названия"):
            shutil.copy("OBS/basic.ini", f"{os.getenv('APPDATA')}\\obs-studio\\basic\\profiles\\Без названия")
        else:
            shutil.copy("OBS/basic.ini", f"{os.getenv('APPDATA')}\\obs-studio\\basic\\profiles\\Без назви")
        shutil.copy("OBS/Без названия.json", f"{os.getenv('APPDATA')}\\obs-studio\\basic\\scenes")
        shutil.copy("OBS/Без названия.json.bak", f"{os.getenv('APPDATA')}\\obs-studio\\basic\\scenes")
        shutil.copy("OBS/Без назви.json", f"{os.getenv('APPDATA')}\\obs-studio\\basic\\scenes")
        shutil.copy("OBS/Без назви.json.bak", f"{os.getenv('APPDATA')}\\obs-studio\\basic\\scenes")

    def image(self):
        if self.resolution == "1920x1080":
            with Image.open('noback_1920x1080.png') as img:
                hours = ["01", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "21"]
                hour = strftime("%H")
                I1 = ImageDraw.Draw(img)
                font = ImageFont.truetype('HTML/SF-Pro-Display-Semibold.ttf', 21)
                dot_font = ImageFont.truetype('HTML/SFProDisplay-Regular.ttf', 32)
                if hour not in hours:
                    if strftime("%M").startswith("1"):
                        I1.text((52, 23), hour, font=font, fill=(255, 255, 255))
                        I1.text((77, 11), ".", font=dot_font, fill=(255, 255, 255))
                        I1.text((77, 3), ".", font=dot_font, fill=(255, 255, 255))
                        I1.text((87, 23), strftime("%M"), font=font, fill=(255, 255, 255))
                    else:
                        I1.text((52, 23), hour, font=font, fill=(255, 255, 255))
                        I1.text((77, 11), ".", font=dot_font, fill=(255, 255, 255))
                        I1.text((77, 3), ".", font=dot_font, fill=(255, 255, 255))
                        I1.text((85, 23), strftime("%M"), font=font, fill=(255, 255, 255))
                elif hour == "11":
                    I1.text((54, 24), hour, font=font, fill=(255, 255, 255))
                    I1.text((74, 12), ".", font=dot_font, fill=(255, 255, 255))
                    I1.text((74, 4), ".", font=dot_font, fill=(255, 255, 255))
                    I1.text((83, 24), strftime("%M"), font=font, fill=(255, 255, 255))
                else:
                    I1.text((54, 24), hour, font=font, fill=(255, 255, 255))
                    I1.text((76, 12), ".", font=dot_font, fill=(255, 255, 255))
                    I1.text((76, 4), ".", font=dot_font, fill=(255, 255, 255))
                    I1.text((83, 24), strftime("%M"), font=font, fill=(255, 255, 255))
                img.save('HTML/noback.png')
        else:
            with Image.open('noback_1920x1080.png') as img:
                hours = ["01", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "21"]
                hour = strftime("%H")
                I1 = ImageDraw.Draw(img)
                font = ImageFont.truetype('HTML/SF-Pro-Display-Semibold.ttf', 21)
                dot_font = ImageFont.truetype('HTML/SFProDisplay-Regular.ttf', 32)
                if hour not in hours:
                    if strftime("%M").startswith("1"):
                        I1.text((52, 23), hour, font=font, fill=(255, 255, 255))
                        I1.text((77, 11), ".", font=dot_font, fill=(255, 255, 255))
                        I1.text((77, 3), ".", font=dot_font, fill=(255, 255, 255))
                        I1.text((87, 23), strftime("%M"), font=font, fill=(255, 255, 255))
                    else:
                        I1.text((52, 23), hour, font=font, fill=(255, 255, 255))
                        I1.text((77, 11), ".", font=dot_font, fill=(255, 255, 255))
                        I1.text((77, 3), ".", font=dot_font, fill=(255, 255, 255))
                        I1.text((85, 23), strftime("%M"), font=font, fill=(255, 255, 255))
                elif hour == "11":
                    I1.text((54, 24), hour, font=font, fill=(255, 255, 255))
                    I1.text((74, 12), ".", font=dot_font, fill=(255, 255, 255))
                    I1.text((74, 4), ".", font=dot_font, fill=(255, 255, 255))
                    I1.text((83, 24), strftime("%M"), font=font, fill=(255, 255, 255))
                else:
                    I1.text((54, 24), hour, font=font, fill=(255, 255, 255))
                    I1.text((76, 12), ".", font=dot_font, fill=(255, 255, 255))
                    I1.text((76, 4), ".", font=dot_font, fill=(255, 255, 255))
                    I1.text((83, 24), strftime("%M"), font=font, fill=(255, 255, 255))
                img.save('HTML/noback2.png')
                subprocess.call('ffmpeg -i HTML/noback2.png -vf scale=486:1054 -y HTML/noback.png', shell=True)
