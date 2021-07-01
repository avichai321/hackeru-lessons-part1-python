from datetime import *
import random
from time import sleep


sum_points= 0
def game():
    global sum_points
    print("wellcome to Chukudate game!\nThe game who teach you about datetime library in python\nevery right answer give you 10 points wrong answer give you -5 points\nlets play!")
    sleep(3)
    d = datetime.now()
    questions = ["Day", "Year", "Month", "Day in the year", "Number of month", "Morning_Night", "Day in month", "Minute", "Hour", "Second", "Date today"]
    q = random.choice(questions)
    if q == questions[0]:
        print("subject: " + q)
        a = input("which day are we now? (first letter must be Upper)\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%A"))
        if a == d.strftime("%A") or a == d.strftime("%a"):
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nstr:\nd.strftime("%A") or d.strftime("%a")')
    elif q == questions[1]:
        print("subject: " + q)
        a = input("which year are we now?\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%Y"))
        if a == d.strftime("%Y"):
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nint:\nd.year\nstr:\nd.strftime("%Y")')
    elif q == questions[2]:
        print("subject: " + q)
        a = input("which month are we now?\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%B"))
        if a == d.strftime("%B"):
            print("you are correct you get 10 points")
            print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nstr:\nd.strftime("%B")')
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nint:\nd.year\nstr:\nd.strftime("%Y")')
    elif q == questions[3]:
        print("subject: " + q)
        a = input("which day are we in the year?\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%j"))
        if a == d.strftime("%j"):
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nstr:\nd.strftime("%j")')
    elif q == questions[4]:
        print("subject: " + q)
        a = input("what is the number of the month are we now?\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%m"))
        if a == d.strftime("%m"):
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nint:\nd.mounth\nstr:\nd.strftime("%m")')
    elif q == questions[5]:
        print("subject: " + q)
        a = input("we are in the daylight or night?\n>>")
        print("your Answer: " + a)
        if a == "daylight" and 6 <= d.hour < 20:
            print("correct answer: daylight")
            print("you are correct you get 10 points")
            sum_points += 10
        elif a == "night" and (6 > d.hour or d.hour >= 20):
            print("your Answer: " + a)
            print("correct answer: night")
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nint:\nd.hour\nstr:\nAM PM:d.strftime("%H")\n1-12:d.strftime("%I")')
    elif q == questions[6]:
        print("subject: " + q)
        a = input("which day in the month are we now?\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%d"))
        if a == d.strftime("%d"):
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nstr:\nd.strftime("%d")')
    elif q == questions[7]:
        print("subject: " + q)
        a = input("What is the minute right now?\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%M"))
        if a == d.strftime("%M"):
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nint:\nd.minute\nstr:\nd.strftime("%M")')
    elif q == questions[8]:
        print("subject: " + q)
        a = input("What is the hour right now?\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%H"))
        if a == d.strftime("%H") or a == d.strftime("%I"):
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nint:\nd.hour\nstr:\nd.strftime("%H") or d.strftime("%I")')
    elif q == questions[9]:
        print("subject: " + q)
        a = input("What is the second right now (luck question worth 30 points!)?\n>>")
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%S"))
        if a == d.strftime("%S"):
            print("you are correct you get 30 points")
            sum_points += 30
        else:
            print("wrong answer no point has taken from you")
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nint:\nd.second\nstr:\nd.strftime("%S")')
    elif q == questions[10]:
        print("subject: " + q)
        a = input('What is the date today? (enter your answer like this "m/day/year")\n>>')
        print("your Answer: " + a)
        print("correct answer: " + d.strftime("%x"))
        if a == d.strftime("%x"):
            print("you are correct you get 10 points")
            sum_points += 10
        else:
            print("wrong answer 5 points has take from you")
            sum_points -= 5
        print('the command who bring you the answer in datetime library is: d = datetime.datetime.now()\nstr:\nd.strftime("%x")')
    Exit= input("Are you want to continue:\n1.continue 2.Exit to play center")
    if Exit == "1":
        game()
    elif Exit == "2":
        print("Thanks for playing you get a " + str(sum_points) + " points\nSayonara\n")
        return int(sum_points)
