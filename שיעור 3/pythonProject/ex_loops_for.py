def exloops1():
    words = int(input("Enter the amount of words in your sentence: "))
    sentence = ""
    for i in range(words):
        word = input("Enter a word: ")
        sentence += word + " "
    print(sentence)

def exlopps2():
    sum = 0
    for i in range(5):
        price = int(input("Enter a price: "))
        sum += price
    print("the sum of prices is: " + str(sum))

def exloops3():
    enum = int(input("Enter end number:" ))
    sum = 0
    for i in range(enum + 1):
        sum += i
    print("the summery of the numbers until the end number is: " + str(sum))

def exloops4():
    sum = 0
    price = int(input("Enter price: "))
    if price != 0:
        for i in range():
            sum += price
    elif price == 0:
        print("the sum of all products is: " + str(sum))

def exloops5():
    student = int(input("enter number of students: "))
    allgrade = 0
    for i in range(student + 1):
        grade = int(input("Enter a grade"))
        allgrade += grade
    print("in the class was tested " + str(student) + " and the average of the grades was " + str(allgrade/student))


def exloops6():
    student = int(input("enter number of students: "))
    allgrade = 0
    top = 0
    for i in range(student + 1):
        grade = int(input("Enter a grade"))
        if (grade > top):
            top = grade
        allgrade += grade
    print("in the class was tested " + str(student) + "ant the top grade was " + str(top))

def exloops7():
    student = int(input("enter number of students: "))
    passed = 0
    fail = 0
    for i in range(student + 1):
        grade = int(input("Enter a grade"))
        if grade > 90:
            passed += 1
        elif grade < 70:
            fail += 1
    print("in the class was tested " + str(student) + " the amount of students who fail is: " + str(fail) + " and the amount of students who excellent was: " + str(passed))

def exloops8():
    student = int(input("enter number of students: "))
    passed = 0
    fail = 0
    for i in range(student + 1):
        grade = int(input("Enter a grade"))
        if grade > 90:
            passed += 1
        elif grade < 70:
            fail += 1
    if passed > fail:
        print("this is a excellent class")
    elif passed < fail:
        print("the class was fail")
    else:
        print("this is a average class")