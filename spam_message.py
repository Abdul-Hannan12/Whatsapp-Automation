import pyautogui
import webbrowser as web
import time

msg = input('enter message to send: ')
times = int(input('enter the number of times to send the message: '))

# win_chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
# web.get(win_chrome_path).open('web.whatsapp.com')

web.open('web.whatsapp.com')

time.sleep(30)

for i in range(times):
    for char in msg:
        pyautogui.press('space' if char==' ' else char)
    pyautogui.press('enter')