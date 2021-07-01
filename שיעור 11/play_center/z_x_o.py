import random

point = 0
roll_result = []
bid = 5
plus = ""


def points(x, c):
    global roll_result, point, plus
    point += c
    if x > 0:
        if point - x >= 0:
            point -= x
            x_o(x)
        else:
            roll_result = "You don't have points for that bid, pls enter another bid, your points is: " + str(point)
    else:
        plus = "+" + str(c)


def x_o(y):
    global roll_result, plus, bid
    roll = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    roll2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    played_x = []
    played_o = []
    counter = 0
    roll_result = """      {0} | {1} | {2}
                                      {3} | {4} | {5}
                                      {6} | {7} | {8}
    """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]), str(roll[4]), str(roll[5]),
               str(roll[6]), str(roll[7]), str(roll[8]))
    while True:
        while True:
            try:
                result = input("""
                point = {0} {3}                                       rules
                                                                 enter r
                                {1}
    
                 stop     bid    start     increase bid     decrease bid
                enter e    {2}     enter s      enter i          enter d
                """.format(point, roll_result, bid, plus))
                if result == "e":
                    roll_result = ""
                    return
                elif result == "i" or result == "d" or result == "r" or result == "s":
                    roll_result = """      {0} | {1} | {2}
                                      {3} | {4} | {5}
                                      {6} | {7} | {8}
                                end the game before
                                        """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]), str(roll[4]),
                                                   str(roll[5]), str(roll[6]), str(roll[7]), str(roll[8]))
                    break
                elif int(result) not in roll:
                    roll_result = """           {0} | {1} | {2}
                                           {3} | {4} | {5}
                                           {6} | {7} | {8}
                            your choice must be number in the range
                                    """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]), str(roll[4]),
                                               str(roll[5]), str(roll[6]), str(roll[7]), str(roll[8]))
                    break
                result = int(result)
                break
            except:
                roll_result = """       {0} | {1} | {2}
                                       {3} | {4} | {5}
                                       {6} | {7} | {8}
                              your choice must be number
                    """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]), str(roll[4]), str(roll[5]),
                               str(roll[6]), str(roll[7]), str(roll[8]))
        for i in roll:
            if i in played_x:
                roll_result = """       {0} | {1} | {2}
                                       {3} | {4} | {5}
                                       {6} | {7} | {8}
                             this area hase been filed, chose another area
                    """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]), str(roll[4]), str(roll[5]),
                               str(roll[6]), str(roll[7]), str(roll[8]))
                break
            elif i == result:
                roll[i - 1] = "X"
                roll_result = """      {0} | {1} | {2}
                                      {3} | {4} | {5}
                                      {6} | {7} | {8}
                """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]), str(roll[4]), str(roll[5]),
                           str(roll[6]), str(roll[7]), str(roll[8]))
                played_x.append(i)
                roll2.remove(i)
                counter += 1
                break
            elif i not in roll and i not in played_x:
                roll_result = """       {0} | {1} | {2}
                                       {3} | {4} | {5}
                                       {6} | {7} | {8}
                            your choice must be number in the range
                                """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]), str(roll[4]),
                                           str(roll[5]), str(roll[6]), str(roll[7]), str(roll[8]))
                break
        if counter >= 5:
            if (1 in played_x and 2 in played_x and 3 in played_x) or (4 in played_x and 5 in played_x and 6 in played_x) or (7 in played_x and 8 in played_x and 9 in played_x) or (1 in played_x and 4 in played_x and 7 in played_x) or (2 in played_x and 5 in played_x and 8 in played_x) or (3 in played_x and 6 in played_x and 9 in played_x) or (1 in played_x and 5 in played_x and 9 in played_x) or (3 in played_x and 5 in played_x and 7 in played_x):
                roll_result = """               {0} | {1} | {2}
                                       {3} | {4} | {5}
                                       {6} | {7} | {8}
                                   you are the winner
                              """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]),
                                         str(roll[4]), str(roll[5]), str(roll[6]), str(roll[7]), str(roll[8]))
                plus = "+" + str(int(5 + 5 * (y / 5)))
                points(0, int(5 + 5 * (y / 5)))
                return
            elif counter == 9:
                roll_result = """               {0} | {1} | {2}
                                       {3} | {4} | {5}
                                       {6} | {7} | {8}
                                         draw
                              """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]),
                                         str(roll[4]), str(roll[5]), str(roll[6]), str(roll[7]), str(roll[8]))
                plus = "+" + str(y)
                points(0, int(y))
                plus = "+0"
                return
        x = random.choice(roll2)
        for n in roll2:
            if n == x:
                roll[n - 1] = "O"
                roll_result = """      {0} | {1} | {2}
                                      {3} | {4} | {5}
                                      {6} | {7} | {8}
                                """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]),
                                           str(roll[4]), str(roll[5]), str(roll[6]), str(roll[7]), str(roll[8]))
                played_o.append(n)
                roll2.remove(n)
                counter += 1
        if counter >= 5:
            if (1 in played_o and 2 in played_o and 3 in played_o) or (4 in played_o and 5 in played_o and 6 in played_o) or (7 in played_o and 8 in played_o and 9 in played_o) or (1 in played_o and 4 in played_o and 7 in played_o) or (2 in played_o and 5 in played_o and 8 in played_o) or (3 in played_o and 6 in played_o and 9 in played_o) or (1 in played_o and 5 in played_o and 9 in played_o) or (3 in played_o and 5 in played_o and 7 in played_o):
                roll_result = """               {0} | {1} | {2}
                                       {3} | {4} | {5}
                                       {6} | {7} | {8}
                                       you loose
                              """.format(str(roll[0]), str(roll[1]), str(roll[2]), str(roll[3]),
                                         str(roll[4]), str(roll[5]), str(roll[6]), str(roll[7]), str(roll[8]))
                plus = "+0"
                return


def start():
    global bid, roll_result, point, plus
    z = input("""
            point = {0} {3}                                       rules
                                                               enter r
                        {1}

             stop     bid    start     increase bid     decrease bid
            enter e    {2}    enter s      enter i          enter d
    """.format(point, roll_result, bid, plus))
    plus = ""
    if point != 0 and z == "s":
        points(bid, 0)
    elif z == "e":
        print("                                 good by")
        return
    elif point == 0:
        roll_result = """your point is 0, you can't play
                           exit the game, good by"""
        return
    elif z == "i":
        bid += 5
        roll_result = """     your bid increased to {0}
        """.format(str(bid))
    elif z == "d":
        if bid != 5:
            bid -= 5
            roll_result = """     your bid decreased to {0}
        """.format(str(bid))
    elif z == "r":
        roll_result = """     win the game to get {0} points
                             draw will give you back your bid
        """.format(str(int(5 + 5 * (bid / 5))))
    else:
        plus = ""
        roll_result = "       enter valid choice"
    start()

