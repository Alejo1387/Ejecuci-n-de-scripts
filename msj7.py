import pyautogui, webbrowser
from time import sleep

# con esto entramos a whatsapp
webbrowser.open('https://web.whatsapp.com/send?phone=+573126532324')

# con esto esperamos los segundo que este dentro de sleep
sleep(30)

mensaje = """Es hora de continuar estudiando.

recuerda que queremos ser programadores.

Son las 4 PM."""

for i in range(1):
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')