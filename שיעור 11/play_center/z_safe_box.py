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
            point -= int(x / 5)
            safe_box(x)
        else:
            roll_result = "You don't have points for that bid, pls enter another bid, your points is: " + str(point)
    else:
        plus = "+" + str(c)


def safe_box(y):
    global roll_result, plus, bid, point
    roll_result = ["_", "_", "_", "_", "_"]
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    code_x = []
    count_pass = 0
    count_in = 0
    for i in range(5):
        code_x = random.sample(nums, 5)
    while True:
        for i in roll_result:
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
                        roll_result = []
                        return
                    elif result == "i" or result == "d" or result == "r":
                        roll_result = "{0} solve the quest or exit".format(roll_result)
                    result = int(result)
                    break
                except:
                    roll_result = "{0} the result must be number".format(roll_result)
            roll_result[roll_result.index(i)] = result
        for i in roll_result:
            if i == code_x[roll_result.index(i)]:
                count_pass += 1
            elif i in code_x:
                count_in += 1
        if count_pass == 5:
            roll_result = "{0} you win".format(roll_result)
            plus = "+" + str(int(5 + 5 * (y / 5)))
            points(0, int(5 + 5 * (y / 5)))
            return
        else:
            roll_result = """{0} 
                     in code: {1}     pass: {2}   next: n
                          """.format(roll_result, count_in, count_pass)
            while True:
                result = input("""
            point = {0} {3}                                       rules
                                                             enter r
                            {1}

             stop     bid    start     increase bid     decrease bid
            enter e    {2}     enter s      enter i          enter d
                """.format(point, roll_result, bid, plus))
                if result == "e":
                    roll_result = []
                    return
                elif result == "n":
                    roll_result = ["_", "_", "_", "_", "_"]
                    count_pass = 0
                    count_in = 0
                    break
                elif result == "i" or result == "d" or result == "r":
                    roll_result = "{0} solve the quest or exit".format(roll_result)
            point -= int(y / 5)


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
        roll_result = """     every try coast {1} points
             True '+' result = {0} points
        """.format(str(int(5 + 5 * (bid / 5))), int(bid / 5))
    else:
        plus = ""
        roll_result = "       enter valid choice"
    start()
