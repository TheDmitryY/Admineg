import random
def Gen_Email():
    validchars = 'abcdefghijklmnopqrstuvwxyz1234567890'
    loginlen = random.randint(4, 15)
    login = ''
    for el in range(loginlen):
        pos = random.randint(0,len(validchars)-1)
        login = login + validchars[pos]
    if login[0].isnumeric():
        pos = random.randint(0,len(validchars)-10)
        login = validchars[pos]+login
    servers = ['@gmail', '@yahoo', '@redmail', '@hotmail', '@bing']
    servpos = random.randint(0,len(servers)-1)
    email = login + servers[servpos]
    tlds = ['.com', '.ro', '.gov', '.net', '.org']
    tldpos = random.randint(0,len(tlds)-1)
    email = email + tlds[tldpos]
    return email

def Gens_Email():
    for i in range(5):
        print(Gen_Email())
