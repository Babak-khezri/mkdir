from os import *
from random import *
system("cd ..\..\..")
name = "abcdefghijklmnopqrstuvwxyz#@!$%^&*()_+=-/\?.,:;><~`"
le = len(name) - 2
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