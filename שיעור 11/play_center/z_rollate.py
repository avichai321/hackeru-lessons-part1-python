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
            rollate(x)
        else:
            roll_result = "You don't have points for that bid, pls enter another bid, your points is: " + str(point)
    else:
        plus = "+" + str(c)


def rollate(y):
    global roll_result, plus
    roll = ["poo", "Diamonds", "Cuba", "Tree", "Heart"]
    roll_result = random.choices(roll, weights=[1, 2, 2, 2, 2], k=4)
    diamonds_count = roll_result.count("Diamonds")
    cuba_count = roll_result.count("Cuba")
    tree_count = roll_result.count("Tree")
    heart_count = roll_result.count("Heart")
    if diamonds_count == 2:
        plus = "+" + str(int(5 + 5 * (y / 5)))
        points(0, int(5 + 5 * (y / 5)))
    elif diamonds_count == 3:
        plus = "+" + str(int(15 + 5 * (y / 5)))
        points(0, int(15 + 5 * (y / 5)))
    elif diamonds_count == 4:
        plus = "+" + str(int(45 + 5 * (y / 5)))
        points(0, int(45 + 5 * (y / 5)))
    elif cuba_count == 2:
        plus = "+" + str(int(5 + 5 * (y / 5)))
        points(0, int(5 + 5 * (y / 5)))
    elif cuba_count == 3:
        plus = "+" + str(int(15 + 5 * (y / 5)))
        points(0, int(15 + 5 * (y / 5)))
    elif cuba_count == 4:
        plus = "+" + str(int(45 + 5 * (y / 5)))
        points(0, int(45 + 5 * (y / 5)))
    elif tree_count == 2:
        plus = "+" + str(int(5 + 5 * (y / 5)))
        points(0, int(5 + 5 * (y / 5)))
    elif tree_count == 3:
        plus = "+" + str(int(15 + 5 * (y / 5)))
        points(0, int(15 + 5 * (y / 5)))
    elif tree_count == 4:
        plus = "+" + str(int(45 + 5 * (y / 5)))
        points(0, int(45 + 5 * (y / 5)))
    elif heart_count == 2:
        plus = "+" + str(int(5 + 5 * (y / 5)))
        points(0, int(5 + 5 * (y / 5)))
    elif heart_count == 3:
        plus = "+" + str(int(15 + 5 * (y / 5)))
        points(0, int(15 + 5 * (y / 5)))
    elif heart_count == 4:
        plus = "+" + str(int(45 + 5 * (y / 5)))
        points(0, int(45 + 5 * (y / 5)))
    else:
        plus = "+0"


def start():
    global bid, roll_result, point, plus
    z = input("""
            point = {0} {3}                                       rules
                                                               enter r
                        {1}

             stop     bid    start     increase bid     decrease bid
            enter e   {2}     enter s      enter i          enter d
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
        roll_result = """     True '+' result = {0} points
        """.format(str(int(5 + 5 * (bid / 5))))
    else:
        plus = ""
        roll_result = "       enter valid choice"
    start()
