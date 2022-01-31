import os
import sys
import time
import pyautogui
import keyboard
working_dir = os.path.abspath(os.getcwd())
html_filename = str(sys.argv[1])
if ".html" not in html_filename:
    print("Failed: File type not compatible")
    exit()
else:
    os.system('cd C:\Program Files\Google\Chrome\Application && chrome.exe file:///' + working_dir + "\\" + html_filename)
while True:
    if (keyboard.is_pressed("ctrl+s")):
        pyautogui.keyDown('alt')
        time.sleep(.2)
        pyautogui.press('tab')
        time.sleep(.2)
        pyautogui.keyUp('alt')
        time.sleep(.5)
        pyautogui.hotkey('f5')