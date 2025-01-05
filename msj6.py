import pyautogui, webbrowser
from time import sleep

# con esto entramos a whatsapp
webbrowser.open('https://web.whatsapp.com/send?phone=+573126532324')

# con esto esperamos los segundo que este dentro de sleep
sleep(30)

mensaje = """Descanza un rato, son las 3 PM"""

for i in range(1):
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')