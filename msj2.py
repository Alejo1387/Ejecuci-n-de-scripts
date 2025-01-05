import pyautogui, webbrowser
from time import sleep

# con esto entramos a whatsapp
webbrowser.open('https://web.whatsapp.com/send?phone=+573126532324')

# con esto esperamos los segundo que este dentro de sleep
sleep(30)

mensaje = """Levantate, no se te olvide estudiar.

Es hora de arreglar la casa y alistarte para estudiar.

Son las 8 AM."""

for i in range(1):
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')