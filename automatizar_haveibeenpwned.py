import webbrowser
import time
import pyperclip
import pyautogui

documento = open('escribir_correos.txt','r')
documento = documento.read().split('\n')


# Ahora aquí ordenamos que se escriba con el teclado:

for email in documento:
    webbrowser.open_new("https://haveibeenpwned.com/")
    time.sleep(3)
    pyperclip.copy(email) # Copiamos en portapapeles los email.
    pyautogui.hotkey('ctrl', 'v', interval = 0.15) # Los pegamos en la web.
    pyautogui.press("enter")
