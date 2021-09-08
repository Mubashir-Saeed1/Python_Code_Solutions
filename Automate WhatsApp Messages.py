import pyautogui
import webbrowser as wb
import time

wb.open('https://web.whatsapp.com/')
time.sleep(20)
for i in range(30):
    pyautogui.press('A')
    pyautogui.press('r')
    pyautogui.press('e')
    pyautogui.press('e')
    pyautogui.press('b')
    pyautogui.press('a')
    pyautogui.press('enter')
    print('Message Sent')