from datetime import *
from time import *
from threading import *

def hour():
    x = datetime.now()
    m = int((x.strftime("%M")))
    h = int((x.strftime("%H")))
    if h < 0 or m < 34:
        return True
    else:
        return False

def countdown():
    global mytimer
    mytimer = 5
    for x in range (5):
        mytimer = mytimer - 1
        sleep(1)
        print(mytimer)

def azaka1():
    hour()
    if hour() == True:
        azaka = input("Have you hear an alarm\nIf you do, press 'Enter'")
        if azaka == "":
            print(hour())
            sleep(3)
            print("still here?")
            hour()


def kasam():
    c=0
    hour()
    countdown1 = Thread(target=countdown)
    countdown1.start()
    while mytimer > 0:
        azaka = input("Have you hear an alarm\nIf you do, press 'Enter'")
        if azaka == "":
            print(hour())
            sleep(3)
            print("still here?")
            c += 1
            hour()
        if mytimer == 0:
            break
    if c >= 5:
        print("lema haya shiur??")
    else:
        print("Mazal!")







def kasam2():
    c=0
    hour()
    countdown1 = Thread(target=countdown)
    countdown1.start()
    while mytimer > 0:
        azaka1()
        c += 1
        hour()
        if mytimer == 0 and hour() == False:
            break
        elif mytimer == 0:
            countdown1 = Thread(target=countdown)
            countdown1.start()
            continue
    if c >= 5:
        print("lema haya shiur??")
    else:
        print("Mazal!")
kasam()


