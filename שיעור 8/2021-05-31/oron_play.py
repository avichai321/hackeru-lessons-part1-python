import random

def sayHola():
    first = input("Enter first name")
    last = input('Enter last name')
    print("Hola " + first + " " + last)

def play_oron():
    sayHola()
    num1 = random.randrange(1, 11)
    num2 = random.randrange(1, 11)
    op = ["+", "-", "*", "/"]
    op1 = random.choice(op)
    user_sum = int(input(str(num1) + op1 + str(num2) + " = "))
    if op1 == op[0]:
        if(user_sum == num1+num2):
            print('10 points')
            return True
        else:
            print('TRY again')
            return False
    elif op1 == op[1]:
        if (user_sum == num1 - num2):
            print('10 points')
            return True
        else:
            print('TRY again')
            return False
    elif op1 == op[2]:
        if (user_sum == num1 * num2):
            print('10 points')
            return True
        else:
            print('TRY again')
            return False
    elif op1 == op[3]:
        if (user_sum == num1/num2):
            print('10 points')
            return True
        else:
            print('TRY again')
            return False



def play_oron_minus():
    sayHola()
    pass

play_oron_plus()