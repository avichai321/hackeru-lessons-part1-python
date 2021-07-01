def exfor1():
    for i in range (1,11):
        print(i)


def exfor2():
    for i in range(2,8):
        print(i)


def exfor3():
    for i in range(11):
        print(10 - i)


def exfor4():
    for i in range(6):
        print(8 - i)

def exfor5():
    end = int(input("Enter a end number: "))
    for i in range(end + 1):
        print(i)

def exfor6():
    start = int(input("Enter start number: "))
    for i in range(start , 101):
        print(i)

def exfor7():
    start = int(input("Enter start number: "))
    end = int(input("Enter a end number: "))
    for i in range (start , end + 1):
        print(i)

def exfor8():
    start = int(input("Enter start number: "))
    end = int(input("Enter a end number: "))
    if start < end:
        for i in range(start, end + 1):
            print(i)
    else:
        print("the start number cannot be bigger then the end number")

exfor8()