import pyttsx3
import os

def Book_Menu():
    print("Welcome to AudioBook Convertor!")
    Get_Book()
def Get_Book():
    filename = input("Enter file path : ")
    succes = input("Enter saved file name [file.mp3] : ")
    with open("%s" % filename, "r") as book:
        book_text = book.readlines()
    engine = pyttsx3.init()
    for i in book_text:

        engine.save_to_file(i, succes)
        engine.runAndWait()
        os.startfile(succes)
