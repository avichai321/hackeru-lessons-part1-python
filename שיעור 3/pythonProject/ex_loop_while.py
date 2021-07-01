def exWhile1():
    i=1
    while i<=10:
        print(i)
        i+=1

def exWhile2():
    i=2
    while i<=7:
        print(i)
        i+=1

def exWhile3():
    i=0
    while i<=10:
        print(i)
        i+=1

def exWhile4():
    i = 8
    while i >= 3:
        print(i)
        i -= 1

def exWhile5():
    end = int(input("enter end number"))
    i = 0
    while i <= end:
        print(i)
        i += 1

def exWhile6():
    start = int(input("Enter start number: "))
    i = 100
    while start <= i:
        print(start)
        start += 1

def exWhile7():
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
    while start <= end:
        print(start)
        start += 1

def exWhile8():
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
    if (start < end):
        while start <= end:
            print(start)
            start += 1
    elif (start > end):
        print("start cannot be bigger then end")
