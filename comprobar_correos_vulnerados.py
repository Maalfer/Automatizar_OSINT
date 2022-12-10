import webbrowser
import pyautogui
import time

documento = open('escribir_correos.txt','r')
documento = documento.read().split('\n')


# Ahora aquí ordenamos que se escriba con el teclado:

for email in documento:
    webbrowser.open_new("https://haveibeenpwned.com/")
    time.sleep(3)
    pyautogui.typewrite(email)
    pyautogui.press("enter")


