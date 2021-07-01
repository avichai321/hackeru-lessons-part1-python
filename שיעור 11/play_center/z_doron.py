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
            doron(x)
        else:
            roll_result = "You don't have points for that bid, pls enter another bid, your points is: " + str(point)
    else:
        plus = "+" + str(c)


def doron(y):
    global roll_result, plus, bid
    roll = range(1, 101)
    roll_signs = []
    signs = ["+", "-", "*", "/"]
    roll_signs.append(random.sample(signs, 1))
    while True:
        roll_num = random.sample(roll, 2)
        if roll_signs[0][0] != "/":
            break
        elif roll_signs[0][0] == "/" and (roll_num[0] % roll_num[1]) == 0:
            break
    roll_result = "{0} {2} {1} = ".format(str(roll_num[0]), str(roll_num[1]), roll_signs[0][0])
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
                print("                                 good by")
                return
            elif result == "i" or result == "d" or result == "r":
                roll_result = roll_result = "{0} + {1} =  solve the quest or exit".format(str(roll_num[0]), str(roll_num[1]))
            result = int(result)
            break
        except:
            roll_result = "{0} + {1} =  the result must be number".format(str(roll_num[0]), str(roll_num[1]))
    if roll_signs[0][0] == "+":
        if result == (roll_num[0] + roll_num[1]):
            roll_result = "{0} + {1} = {2} pass".format(str(roll_num[0]), str(roll_num[1]), str(result))
            plus = "+" + str(int(5 + 5 * (y / 5)))
            points(0, int(5 + 5 * (y / 5)))
            return
        else:
            roll_result = "{0} + {1} = {2} loose".format(str(roll_num[0]), str(roll_num[1]), str(result))
            plus = "+0"
    elif roll_signs[0][0] == "-":
        if result == (roll_num[0] - roll_num[1]):
            roll_result = "{0} - {1} = {2} pass".format(str(roll_num[0]), str(roll_num[1]), str(result))
            plus = "+" + str(int(5 + 5 * (y / 5)))
            points(0, int(5 + 5 * (y / 5)))
            return
        else:
            roll_result = "{0} - {1} = {2} loose".format(str(roll_num[0]), str(roll_num[1]), str(result))
            plus = "+0"
    elif roll_signs[0][0] == "*":
        if result == (roll_num[0] * roll_num[1]):
            roll_result = "{0} * {1} = {2} pass".format(str(roll_num[0]), str(roll_num[1]), str(result))
            plus = "+" + str(int(5 + 5 * (y / 5)))
            points(0, int(5 + 5 * (y / 5)))
            return
        else:
            roll_result = "{0} * {1} = {2} loose".format(str(roll_num[0]), str(roll_num[1]), str(result))
            plus = "+0"
    elif roll_signs[0][0] == "/":
        if result == int(roll_num[0] / roll_num[1]):
            roll_result = "{0} / {1} = {2} pass".format(str(roll_num[0]), str(roll_num[1]), str(result))
            plus = "+" + str(int(5 + 5 * (y / 5)))
            points(0, int(5 + 5 * (y / 5)))
            return
        else:
            roll_result = "{0} / {1} = {2} loose".format(str(roll_num[0]), str(roll_num[1]), str(result))
            plus = "+0"


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
        roll_result = """     True result = {0} points
        """.format(str(int(5 + 5 * (bid / 5))))
    else:
        plus = ""
        roll_result = "       enter valid choice"
    start()
