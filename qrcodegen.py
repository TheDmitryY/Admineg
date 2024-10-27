import qrcode
import  os

def Code_Menu():
    print("Welcome to QR-Code generator ! \n")
    Create_Code()

def Create_Code():
    text = input("Enter text for QR-Code : ")
    filename = input("Enter file name for saving" + ".png : ")
    img = qrcode.make(text)
    img.save(filename)
    print(f'QR-Code succesful created and saved to {filename} file ')
    os.startfile(filename)

