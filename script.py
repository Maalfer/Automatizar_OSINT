import webbrowser
import pyperclip
import pyautogui
import time
from colorama import Fore, Style

documento = open('direcciones_ip.txt','r')
documento = documento.read().split('\n')

eleccion = input(Fore.GREEN + "Escribe el nombre de la herramienta que quieras utilizar para analizar las direcciones IP: " + Fore.YELLOW +
"""\n1 - Symantec
2 - AbuseIP
3 - Virustotal: \n""" + Style.RESET_ALL + "¿Cuál es tu elección? --> ")

if eleccion=="1":
    for ip in documento:
        webbrowser.open_new("https://sitereview.bluecoat.com/#/")
        time.sleep(3)
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        pyautogui.press("enter")

elif eleccion=="2":
    for ip in documento:
        webbrowser.open_new("https://www.abuseipdb.com/")
        time.sleep(3)
        for i in range(15):
            pyautogui.press('tab')
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        pyautogui.press("enter")

elif eleccion=="3":
    for ip in documento:
        webbrowser.open_new("https://www.virustotal.com/gui/home/search")
        time.sleep(3)
        for i in range(6):
                pyautogui.press('tab')
        pyperclip.copy(ip)
        pyautogui.hotkey('ctrl', 'v', interval = 0.15)
        pyautogui.press("enter")

else:
     print("ERROR!!! Hay que insertar un número del 1 al 3")