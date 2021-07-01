print('into file loop while.. ')

def daniel():
    i = 1
    while i <= 10:
        print('hola')
        print(i)
        i += 1  # i = i + 1

# daniel()

def exWhile5():
    end = int(input("Enter End number"))
    i = 0
    while i <= end:
        print(i)
        i += 1

# exWhile5()


def exWhile8():
    start = int(input("Enter start number")) # 5
    end = int(input("Enter end number"))  # 10

    if start < end:  # start 5 end 10
        while start <= end:
            print(start)
            start += 1
    else:  # start 10 end 5
        while end <= start:
            print(end)
            end += 1

exWhile8()

def exLoops1():
    num = int(input("Enter number.."))
    i = 1
    all_txt = ''
    while i <= num:
        txt = input("Enter word ")
        all_txt = all_txt + txt + " "
        i += 1
    else:
        print(all_txt)


# exLoops1()


