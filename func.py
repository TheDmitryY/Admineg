import os
from mp3 import  Conventer
from audiobook import Book_Menu
import webbrowser
def title():
    print(" █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗███████╗ ██████╗")
    print("██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔════╝██╔════╝")
    print("███████║██║  ██║██╔████╔██║██║██╔██╗ ██║█████╗  ██║  ███╗")
    print("██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║   ██║")
    print("██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╔╝")
    print("╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ")

def menu():
    title()
    print("                 ╔════════════════════╗                  ")
    print("                 ║   1. Convertors    ║                  ")
    print("                 ║   2. Fast Opening  ║                  ")
    print("                 ║   3. Generators    ║                  ")
    print("                 ║   4. Network       ║                  ")
    print("                 ║   5. About         ║                  ")
    print("                 ╚════════════════════╝                  ")
    option = input("")
    if option == "1":
        Convertors_Menu()
    elif option == "2":
        FastOpen_Menu()
    elif option == "3":
        Generator_Menu()
    elif option == "4":
        Network_Menu()
    elif option == "5":
        About_Menu()

def Convertors_Menu():
        title()
        print("                 ╔════════════════════╗                  ")
        print("                 ║   1. MP4           ║                  ")
        print("                 ║   2. Audiobook     ║                  ")
        print("                 ║   3. Back          ║                  ")
        print("                 ╚════════════════════╝                  ")
        activity_choise = input("")
        if activity_choise == "1":
            Conventer()
        elif activity_choise == "2":
            Book_Menu()
        elif activity_choise == "3":
            menu()


def Generator_Menu():
    title()
    print("                 ╔════════════════════╗                  ")
    print("                 ║   1. Password      ║                  ")
    print("                 ║   2. QR-Code       ║                  ")
    print("                 ║   3. Email         ║                  ")
    print("                 ║   4. IP            ║                  ")
    print("                 ║   5. Back          ║                  ")
    print("                 ╚════════════════════╝                  ")


def FastOpen_Menu():
    title()
    print("                 ╔════════════════════╗                  ")
    print("                 ║   1. Apps          ║                  ")
    print("                 ║   2. Sites         ║                  ")
    print("                 ║   3. Back          ║                  ")
    print("                 ╚════════════════════╝                  ")
    Fast_choise = input("")
    if Fast_choise == "1":
        FastOpen_App()
    elif Fast_choise == "2":
        FastOpen_Sites()
    elif Fast_choise == "3":
        menu()


def Network_Menu():
    title()
    print("                 ╔════════════════════╗                  ")
    print("                 ║   1. Check IP      ║                  ")
    print("                 ║   2. IP Scanner    ║                  ")
    print("                 ║   3. Active Ports  ║                  ")
    print("                 ║   4. Back          ║                  ")
    print("                 ╚════════════════════╝                  ")


def About_Menu():
    title()
    print("                 ╔══════════════════════════╗                  ")
    print("                 ║   GitHub : TheDmitryY    ║                  ")
    print("                 ║   Telegram : HorekiSun   ║                  ")
    print("                 ║   Version : 1.0.0        ║                  ")
    print("                 ║   1. Back                ║                  ")
    print("                 ╚══════════════════════════╝                  ")

def FastOpen_App():
    Putty = "Apps\putty.exe"
    AnyDesk = "Apps\AnyDesk.exe"
    title()
    print("                 ╔══════════════════════════╗                  ")
    print("                 ║   1. Putty               ║                  ")
    print("                 ║   2. Anydesk             ║                  ")
    print("                 ║   3. Back                ║                  ")
    print("                 ╚══════════════════════════╝                  ")
    FastOpen_Choise = input("")
    if FastOpen_Choise == "1":
        os.startfile(Putty)
    if FastOpen_Choise == "2":
        os.startfile(AnyDesk)
    if FastOpen_Choise == "3":
        menu()

def FastOpen_Sites():
    title()
    print("                 ╔══════════════════════════╗                  ")
    print("                 ║   1. Virus Total         ║                  ")
    print("                 ║   2. Habr                ║                  ")
    print("                 ║   3. Stack Overflow      ║                  ")
    print("                 ║   4. Router Panel        ║                  ")
    print("                 ║   5. Back                ║                  ")
    print("                 ╚══════════════════════════╝                  ")
    FastSite_Choise = input("")
    if FastSite_Choise == "1":
        VirusTotal = 'https://www.virustotal.com'
        webbrowser.open(VirusTotal)
    elif FastSite_Choise == "2":
        Habr = 'https://habr.com/ru/articles/'
        webbrowser.open(Habr)
    elif FastSite_Choise == "3":
        StackOverflow = 'https://stackoverflow.com/'
        webbrowser.open(StackOverflow)
    elif FastSite_Choise == "4":
        Router = "http://192.168.0.1"
        webbrowser.open(Router)
    elif FastSite_Choise == "5":
        menu()