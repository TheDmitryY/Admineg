from mp3 import  Conventer
from audiobook import Book_Menu
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
