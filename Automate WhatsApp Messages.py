import pyautogui
import webbrowser as wb
import time

wb.open('https://web.whatsapp.com/')
time.sleep(20)
for i in range(30):
    pyautogui.press('H')
    pyautogui.press('e')
    pyautogui.press('l')
    pyautogui.press('l')
    pyautogui.press('o')
    pyautogui.press('enter')
    print('Message Sent')
