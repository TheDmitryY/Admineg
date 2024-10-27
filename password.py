import random, time

def Password_Menu():
    print("Welcome to Password Generator ! \n")
    Password_Generate()
def Password_Generate():
    lower_a = 'abcdefghijklmnopqrstuvxyz'
    upper_a = lower_a.upper()
    numbers = "0123456789"
    symbols = "@#*^!?()$&+"
    length = 12
    repeating = 1
    p = lower_a + upper_a + numbers + symbols
    option = input("[$] You wanna change generating settings? [y/n] ")

    if option == "y":
        print(" [1] Change password length")
        print(" [2] Change repeating password")
        choice = int(input("\n [$] Choose action --> "))

        if choice == 1:
            length = int(input(" [$] Enter password length: \n"))
            for _ in range(repeating):
                complete = ''.join(random.sample(p, length))
                print(" [$] Generated Password: ", complete + "\n")
                time.sleep(0.5)

        elif choice == 2:
            repeating = int(input(" [$] Enter password repeating: "))
            for _ in range(repeating):
                complete = "".join(random.sample(p, length))
                print(" [$] Generated Password: ", complete + "\n")
                time.sleep(0.5)

    elif option == "n":
        for _ in range(repeating):
            complete = "".join(random.sample(p, length))
            print(" [$] Generated Password: ", complete + "\n")
            time.sleep(0.5)