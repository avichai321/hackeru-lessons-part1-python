def exifElse1():
    Username = input("Enter Username")
    Password = input("Enter password")
    if (Password == "Hackeru123"):
        print("ברוך הבא למערכת")
    else:
        print("פרטים אינם תואמים")


def exifElse2():
    Username = input("Enter Username")
    Password = input("Enter password")
    if (Password == "Hackeru123") and (Username == "hackeru"):
        print("ברוך הבא למערכת")
    else:
        print("פרטים אינם תואמים")

def exifElse3():
    age = int(input("Enter Age"))
    if age >= 16:
        print("you can learn how to drive")
    else:
        print("you can`t drive")


def exifElse4():
    age = int(input("Enter Age"))
    if age <= 16:
        print("you cant drive")
    elif (16 < age) and (age <= 18):
        print("you can learn how to drive")
    elif (18 < age) and (age < 70):
        print("you can drive")
    else:
        print("you can drive with doctor premission")

def exifElse5():
    size = int(input("Enter size: "))
    if size >= 24 and size <= 30:
        print("your size is S")
    elif size >= 31 and size <= 36:
        print("your size is M")
    elif size > 36:
        print("you size is L")
    else:
        print("we dont have this size")

def exifElse6():
    num1 = int(input("Enter a number"))
    if num1%2 == 1:
        print("this is a odd number")
    elif num1%2 == 0:
        print("its a even number")


def exifElse7():
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    operator = input("Enter operator + or *: ")
    if operator == "+":
        print("your result is: " + str(num1+num2))
    elif operator == "*":
        print("your result is: " + str(num1*num2))
    else:
        print("you Entered wrong details")

def exifElse8():
    username = input("Enter username")
    password = input("Enter password")
    if username == "" or password == "":
        if password == "":
            print("Enter password")
        elif username == "":
            print("enter username")
    elif username == "hackeru" and password == "hacker123":
        print("welcome to the system")

    else:
        print("username or password is incorrect")
exifElse5()




