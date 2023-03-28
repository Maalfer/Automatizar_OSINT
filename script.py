import webbrowser
import time
import pyperclip
import pyautogui
from colorama import Fore, Style

# Establecemos unos colores para usarlos posteriormente:
amarillo = Fore.YELLOW
verde = Fore.GREEN
# Abrimos el .txt con cada una de las IP.

documento = open('direcciones_ip.txt','r')
documento = documento.read().split('\n')

# Ahora aquí ordenamos que se escriba con el teclado:

eleccion = input(Fore.GREEN + "Escribe el nombre de la herramienta que quieras utilizar para analizar las direcciones IP" + Fore.YELLOW +
"""\n1 - Symantec
2 - AbuseIP
3 - VirusTotal: \n""" + Style.RESET_ALL + "¿Cual es tu elección? --> ")

if eleccion=="Symantec":
    for ip in documento:

        webbrowser.open_new("https://sitereview.bluecoat.com/#/")
        time.sleep(3)
        pyperclip.copy(ip) # Copiamos en portapapeles las IP.
        pyautogui.hotkey('ctrl', 'v', interval = 0.15) # Los pegamos en la web.
        pyautogui.press("enter")

if eleccion=="AbuseIP":
    for ip in documento:
        
        webbrowser.open_new("https://www.abuseipdb.com/")
        time.sleep(3)
        for i in range(15):
            pyautogui.press('tab')
        pyperclip.copy(ip) # Copiamos en portapapeles las IP.
        pyautogui.hotkey('ctrl', 'v', interval = 0.15) # Los pegamos en la web.
        pyautogui.press("enter")

if eleccion=="Virustotal":
    for ip in documento:

        webbrowser.open_new("https://www.virustotal.com/gui/home/search")
        time.sleep(3)
        for i in range(6):
            pyautogui.press('tab')
        pyperclip.copy(ip) # Copiamos en portapapeles las IP.
        pyautogui.hotkey('ctrl', 'v', interval = 0.15) # Los pegamos en la web.
        pyautogui.press("enter")
