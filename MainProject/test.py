import pyautogui
import time


time.sleep(5)
pyautogui.moveTo(456,208)
for s in range(10):
    pyautogui.scroll(-3)
pyautogui.moveTo(456,208)
pyautogui.dragTo(456, 180, 0.1, button='left')
pyautogui.moveTo(456,208)
