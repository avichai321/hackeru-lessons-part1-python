import random
wrong = 0
exp = 0
lvl = 1
i = str(11)
def oron():
    global wrong
    while wrong != 5:
        global i,exp,lvl
        num1 = random.randint(1, int(i))
        num2 = random.randint(1, int(i))
        print('exp '+ str(exp))
        if exp % 5 == 0:
            lvl += 1
            i = str(lvl)+'1'
        print('lvl '+str(lvl))
        targil = int(input(str(num1)+'+' + str(num2) + ' ='))
        if num1 + num2 == targil:
            exp += 1
            print("correct")
        else:
            wrong += 1
        if wrong == 5:
            print("Game over\n Youre lvl is " + str(lvl)+' \n '+ str(exp)+' Correct answers')
oron()