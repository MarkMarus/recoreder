import pyautogui
import time
import os
import subprocess
import glob
import shutil

class Recorder:
    def __init__(self):
        subprocess.call('open -a simulator', shell=True)
        time.sleep(20)
        self.x, self.y = pyautogui.size()
        self.x = self.x / 2
        self.y = self.y / 2 + 50
        self.record1()
        time.sleep(5)
        self.record2()
        time.sleep(5)
        self.record3()
        time.sleep(30)
        subprocess.call('pkill -x Simulator', shell=True)
        self.saver()

    def record1(self):
        time.sleep(5)
        pyautogui.keyDown('command')
        pyautogui.press('4')
        pyautogui.keyUp('command')
        subprocess.call('xcrun simctl openurl booted http://onlyfans:1233/localhost/Statements.html', shell=True)
        time.sleep(15)
        pyautogui.keyDown('command')
        pyautogui.press('r')
        pyautogui.keyUp('command')
        pyautogui.moveTo(870,500)
        pyautogui.dragTo(870, 300, 0.2, button='left')
        pyautogui.moveTo(870, 790)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(870, 170)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.moveTo(580,720)        
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(self.x, self.y)
        pyautogui.click()
        pyautogui.dragTo(870, 50, 0.2, button='left')
        pyautogui.moveTo(850, 60)
        time.sleep(2)
        pyautogui.click()

    def record2(self):
        pyautogui.keyDown('command')
        pyautogui.press('4')
        pyautogui.keyUp('command')
        subprocess.call('xcrun simctl openurl booted http://onlyfans:1233/localhost/Statements.html', shell=True)
        time.sleep(5)
        pyautogui.keyDown('command')
        pyautogui.press('r')
        pyautogui.keyUp('command')
        pyautogui.moveTo(870,500)
        pyautogui.dragTo(870, 300, 0.2, button='left')
        time.sleep(2)
        pyautogui.moveTo(870, 795)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(870, 170)
        pyautogui.click()
        time.sleep(1.5)
        pyautogui.moveTo(780, 740)
        pyautogui.click()
        pyautogui.moveTo(870, 170)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(870, 740)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(870, 170)
        pyautogui.click()
        pyautogui.moveTo(850, 60)
        pyautogui.click()

    def record3(self):
        time.sleep(1)
        time.sleep(5)
        pyautogui.keyDown('command')
        pyautogui.press('4')
        pyautogui.keyUp('command')
        subprocess.call('xcrun simctl openurl booted http://onlyfans:1233/localhost/Profile.html', shell=True)
        time.sleep(1)
        pyautogui.keyDown('command')
        pyautogui.press('r')
        pyautogui.keyUp('command')
        time.sleep(2)
        pyautogui.moveTo(870, 630)
        pyautogui.dragTo(870, 570, 0.2, button='left')
        time.sleep(2)
        pyautogui.moveTo(870, 795)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click()
        time.sleep(3)
        pyautogui.moveTo(870, 680)
        pyautogui.click()
        time.sleep(2)
        pyautogui.click(self.x, self.y)
        pyautogui.dragTo(870, 50, 0.2, button='left')
        time.sleep(1)
        pyautogui.moveTo(870, 795)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)
        pyautogui.moveTo(870, 170)
        pyautogui.click()
        pyautogui.moveTo(850, 60)
        time.sleep(2)
        pyautogui.click()

    def saver(self):
        with open('username.txt', encoding='utf8') as f:
            username = f.read().strip()
        files = [file for file in glob.glob(f'/Users/{username}/Desktop/Simulator*.mp4')]
        count = 1
        for file in files:
            print(file)
            shutil.move(file, f"video/{count}.mp4")
            os.remove(file)
            count += 1