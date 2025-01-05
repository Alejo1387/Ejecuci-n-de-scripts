import pywhatkit

mensaje = """Descanza un rato, son las 3 PM"""

try:
    pywhatkit.sendwhatmsg("+573126532324", mensaje, 18,3)
except:
    print('Ocurrio un error')