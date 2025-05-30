from password import  Password_Menu; from qrcodegen import Code_Menu; from audiobook import Book_Menu; from audiobook import Book_Menu; from mp3 import  Conventer; import os, webbrowser
from pystyle import Colors, Colorate, System; from ip_generator import Gen_Ip; from email_generator import Gens_Email;
def title():
    print(Colorate.Horizontal(Colors.cyan_to_blue, " █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗███████╗ ██████╗", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔════╝██╔════╝", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "███████║██║  ██║██╔████╔██║██║██╔██╗ ██║█████╗  ██║  ███╗", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██║   ██║", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║███████╗╚██████╔╝", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝ ", 1))

def menu():
    title()
    print(Colorate.Horizontal(Colors.cyan_to_blue, "                 ╔════════════════════╗                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "                 ║   1. Convertors    ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "                 ║   2. Fast Opening  ║                  ", 2))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "                 ║   3. Generators    ║                  ", 2))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "                 ║   4. Network       ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "                 ║   5. About         ║                  ", 3))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "                 ╚════════════════════╝                  ", 1))
    Printes()
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
    else:
        menu()

def Convertors_Menu():
        System.Command("cls")
        title()
        print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╔════════════════════╗                  ", 1))
        print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   1. MP4           ║                  ", 1))
        print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   2. Audiobook     ║                  ", 1))
        print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   3. Back          ║                  ", 1))
        print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╚════════════════════╝                  ", 1))
        Printes()
        activity_choise = input("")
        if activity_choise == "1":
            Conventer()
        elif activity_choise == "2":
            Book_Menu()
        elif activity_choise == "3":
            menu()
        else:
            menu()


def Generator_Menu():
    System.Command("cls")
    title()
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╔════════════════════╗                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   1. Password      ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   2. QR-Code       ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   3. Email         ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   4. IP            ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   5. Back          ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╚════════════════════╝                  ", 1))
    Printes()
    Generator_Choise = input("")
    if Generator_Choise == "1":
        Password_Menu()
    elif Generator_Choise == "2":
        Code_Menu()
    elif Generator_Choise == "3":
        Gens_Email()
    elif Generator_Choise == "4":
        Gen_Ip()
    else:
        menu()



def FastOpen_Menu():
    System.Command("cls")
    title()
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╔════════════════════╗                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   1. Apps          ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   2. Sites         ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   3. Back          ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╚════════════════════╝                  ", 1))
    Printes()
    Fast_choise = input("")
    if Fast_choise == "1":
        FastOpen_App()
    elif Fast_choise == "2":
        FastOpen_Sites()
    elif Fast_choise == "3":
        menu()
    else:
        menu()


def Network_Menu():
    System.Command("cls")
    title()
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╔════════════════════╗                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   1. Check IP      ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   2. Active Ports  ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   3. Back          ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╚════════════════════╝                  ", 1))
    Printes()
    Network_Choise = input("")
    if Network_Choise == "1":
        Check_IP()
    elif Network_Choise == "2":
        Active_PortsNet()
    elif Network_Choise == "3":
        menu()
    else:
        menu()


def About_Menu():
    System.Command("cls")
    title()
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╔══════════════════════════╗                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   GitHub : TheDmitryY    ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   Telegram : HorekiSun   ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   Version : 1.0.0        ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   1. Back                ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╚══════════════════════════╝                  ", 1))
    Printes()
    About_Choise = input("")
    if About_Choise == "1":
        menu()
    else:
        menu()

def FastOpen_App():
    System.Command("cls")
    Putty = "Apps\putty.exe"
    AnyDesk = "Apps\AnyDesk.exe"
    title()
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╔══════════════════════════╗                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   1. Putty               ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   2. Anydesk             ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   3. Back                ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╚══════════════════════════╝                  ", 1))
    Printes()
    FastOpen_Choise = input("")
    if FastOpen_Choise == "1":
        os.startfile(Putty)
    if FastOpen_Choise == "2":
        os.startfile(AnyDesk)
    if FastOpen_Choise == "3":
        FastOpen_Menu()
    else:
        menu()

def FastOpen_Sites():
    System.Command("cls")
    title()
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╔══════════════════════════╗                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   1. Virus Total         ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   2. Habr                ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   3. Stack Overflow      ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   4. Router Panel        ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ║   5. Back                ║                  ", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue,"                 ╚══════════════════════════╝                  ", 1))
    Printes()
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
        FastOpen_Menu()
    else:
        menu()

def Check_IP():
    System.Command("cls")
    System.Command("ipconfig")
def Active_PortsNet():
    System.Command("cls")
    System.Command("netstat")

def Printes():
    print(Colorate.Horizontal(Colors.cyan_to_blue, "╔═══admins@username", 1))
    print(Colorate.Horizontal(Colors.cyan_to_blue, "╚═# ", 1))