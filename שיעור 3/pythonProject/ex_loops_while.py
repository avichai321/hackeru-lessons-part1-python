def exLoops1():
    words = int(input("enter a number"))
    allwords = ""
    i = 1
    while i <= words:
        word = input("Enter a word")
        i += 1
        allwords += " " + word
    print(allwords)

def exloops2():
    nduct = 5
    i = 1
    allduct = 0
    while i <= nduct:
        price= int(input("Enter price: "))
        allduct += price
    print(allduct)

def exloops3():
    end = int(input("enter end number"))
    i = 1
    sum = 0
    while i <= end:
        sum += i
        i += 1
    print(sum)

def exloops4():
    prod = 1
    sump = 0
    while prod != 0:
        prod = int(input("Enter price: "))
        if prod != 0:
            sump += prod
        else:
            print(sump)

def exloops5():
    student = int(input("enter number of students: "))
    i = 1
    sum = 0
    while i <= student:
        grade = int(input("Enter grade: "))
        sum += grade
    print("the average of the grades is : " + str(sum/student))

def exloops6():
    student = int(input("enter number of students: "))
    i = 1
    top = 0
    while i <= student:
        grade = int(input("Enter grade: "))
        if grade > top:
            top = grade
        i += 1

    print("the number of student who tested is: " + str(student) + "and the top grade is: " + str(top))

def exloops7():
    student = int(input("enter number of students: "))
    i = 1
    passed = 0
    fail = 0
    while i <= student:
        grade = int(input("Enter grade: "))
        if grade < 70:
            fail += 1
        elif grade > 90:
            passed += 1
        i += 1
    print("In the class was tested " + str(student) + " students - " + str(fail) + " was failed and " + str(passed) + " was passed in excellent")

def exloops8():
    student = int(input("enter number of students: "))
    i = 1
    passed = 0
    fail = 0
    while i <= student:
        grade = int(input("Enter grade: "))
        if grade < 70:
            fail += 1
        elif grade > 90:
            passed += 1
        i += 1
    if passed > fail:
        print("this is a excellent class")
    elif passed < fail:
        print("the class was failed")








