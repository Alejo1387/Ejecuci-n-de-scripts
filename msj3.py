import pyautogui, webbrowser
from time import sleep

# con esto entramos a whatsapp
webbrowser.open('https://web.whatsapp.com/send?phone=+573126532324')

# con esto esperamos los segundo que este dentro de sleep
sleep(30)

mensaje = """Ya debiste terminar de desayunar y arreglar todo.

Es hora de estudiar, recuerda hacer ejercicios y mostarlos.

Son las 10 AM."""

for i in range(1):
    pyautogui.typewrite(mensaje)
    pyautogui.press('enter')