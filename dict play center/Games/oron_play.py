import random


wrong = 0
exp = 0
lvl = 1
oron_points = 0
i = 11

def oron_play1():
    print("welcome to oron play\nlet`s start!")
    global wrong, exp, i, lvl, oron_points
    while wrong != 5:
        num1 = random.randrange(1, i)
        num2 = random.randrange(1, i)
        op = ["+", "-", "*"]
        op1 = random.choice(op)
        user_sum = input(str(num1) + op1 + str(num2) + " = ")
        x = oron_calculator(user_sum, op1, op, num1, num2)
        if x == 0:
            wrong += 1
        else:
            exp += 1
            if exp % 5 == 0:
                lvl += 1
                i += 10
                print("congratulation you leveled up\nyour level is: " + str(lvl))
        oron_points += x
        print(oron_points)
    print("This is the end of the game\nyour points will add to your user in the play center\nbye bye!\n\n")
    wrong = 0
    return oron_points

def oron_calculator(user_sum,op1,op ,num1, num2):
    points = 0
    if op1 == op[0]:
        if int(user_sum) == (num1 + num2):
            print('10 points')
            print("correct")
            points += 10
        else:
            print("wrong you have left " + str(5-wrong) + " trys" )
            print('The correct answer is: ' + str(num1 + num2))
    elif op1 == op[1]:
        if int(user_sum) == (num1 - num2):
            print('10 points')
            print("correct")
            points += 10
        else:
            print("wrong you have left " + str(5-wrong) + " trys")
            print('The correct answer is: ' + str(num1 - num2))
    elif op1 == op[2]:
        if int(user_sum) == (num1 * num2):
            print('10 points')
            print("correct")
            points += 10
        else:
            print("wrong you have left " + str(5-wrong) + " trys")
            print('The correct answer is: ' + str(num1 * num2))
    return points