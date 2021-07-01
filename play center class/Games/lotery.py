from random import randint
from time import sleep

def randomwlist():
    winlist=[]
    i=1
    b=winlist.append(randint(1,20))
    while(i<=5):
        a=randint(1, 20)
        if(a!=b) and (a not in winlist):
            winlist.insert(i,a)
            i += 1
    return winlist

def game(play):
    row=1
    sum=0
    while(0<play):
        print("\nRound number: " + str(row))
        row=row+1
        play=play-1
        winlist=randomwlist()
        sleep(0.5)
        print("\nThe winnner's numbers are: " + str(winlist) + "\n=======")
        sleep(2)
        gu_list = randomwlist()
        k = 1
        for i in range (len(gu_list)):
            print("Lottery number " + str(k) + ": " + str(gu_list[i]))
            sleep(0.5)
            k=k+1
            if(gu_list[i] in winlist):
                winlist.remove(gu_list[i])

        print("\n" + str(len(winlist)) + " numbers are left\n")
        if(3<len(winlist)<=6):
            print("Sorry, you win nothing try again!")
        elif(len(winlist)==0):
            print("Congratulation, you won 150 points")
            sum += 150
        elif(len(winlist)==1):
            print("Congratulation, you won 100 points")
            sum += 100
        elif(len(winlist)==2):
            print("Congratulation, you won 50 points")
            sum += 50
        elif(len(winlist)==3):
            print("Congratulation, you won 20 points")
            sum += 20
        print("\nonly "+ str(play) +" turns remain")
        sleep(3)
    print("\n\nIts the end of the game!\n---------\nYour total prize is: " + str(sum) + " points\n\nThanks for playing!\n")
    return sum

def lottery(budget):
    print("Wellcome to our lottery game!!!\n---------\nHow it works:\n======\n1.Enter how many points you want to expend and we will tell you how many rounds you can play \n2.Each round we will roulette 6 wining numbers (betwween 1 - 20)\n3.Then we will begin the lottery.\n-----------\nThe prizes:\n======\nIf you guess:\n-----\n6 numbers =  you will win 150 points\n5 numbers =  you will win 100 points\n4 numbers =  you will win 50 points\n3 numbers =  you will win 20 points\n======\nGood luck!!")
    play = budget//5
    print("\nThe number of rounds you can play: " + str(play) + " turns")
    sleep(3)
    print("\nlet's begin\n=========\n")
    sleep(1)
    x = game(play)
    return x






