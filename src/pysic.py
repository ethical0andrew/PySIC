import os
import sys
import time
import pyautogui
import keyboard
working_dir = os.path.abspath(os.getcwd())
with open('pysic_browser.txt') as inputfile:
    browser_name = inputfile.read()
if (browser_name == ""):
    print("Browser set to Google Chrome")
    print("browser_pysic.txt file is empty")
    browser_dir = "C:\Program Files\Google\Chrome\Application && chrome.exe file:///"
if (browser_name == "chrome"):
    print("Browser set to Google Chrome")
    browser_dir = "C:\Program Files\Google\Chrome\Application && chrome.exe file:///"
if (browser_name == "edge"):
    print("Browser set to Microsoft Edge")
    browser_dir = "C:\Program Files (x86)\Microsoft\Edge\Application && msedge.exe file:///"
if (browser_name == "firefox"):
    print("Browser set to Mozilla Firefox")
    browser_dir = "C:\Program Files\Mozilla Firefox && firefox.exe file:///"
if (browser_name == "brave"):
    print("Browser set to Brave")
    browser_dir = "C:\Program Files\BraveSoftware\Brave-Browser\Application && brave.exe file:///"
html_filename = str(sys.argv[1])
if ".html" not in html_filename:
    print("Failed: File type not compatible")
    exit()
else:
    os.system('cd ' + browser_dir + working_dir + "\\" + html_filename)
while True:
    if (keyboard.is_pressed("ctrl+s")):
        pyautogui.keyDown('alt')
        time.sleep(.2)
        pyautogui.press('tab')
        time.sleep(.2)
        pyautogui.keyUp('alt')
        time.sleep(.5)
        pyautogui.hotkey('f5')