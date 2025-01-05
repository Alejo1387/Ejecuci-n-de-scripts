import pyautogui, webbrowser
from time import sleep

# con esto entramos a whatsapp
webbrowser.open('https://web.whatsapp.com/send?phone=+573126532324')

# con esto esperamos los segundo que este dentro de sleep
sleep(30)

for i in range(1):
    pyautogui.typewrite('Es hora de despertarse, son las 7 AM.')
    pyautogui.press('enter')