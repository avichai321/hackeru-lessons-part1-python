import z_bank_account as bank
import z_rollate as rollate
import z_doron as doron
import z_x_o
import z_safe_box as safe_box


game = [rollate, doron, z_x_o, safe_box]
coast = 0
points = 0
counter = 0

def point_games(point):
    for g in game:
        g.point = point



def puy_points(payment, point):
    global points
    user = bank.user_account()
    if user.pay(payment):
        points += point
        print("congratulations, {0} have been added to your play center points".format(points))
    else:
        print("tha pay has been failed, check your bank")


def add_points():
    choice = input("""
    enter pack:
    0- exit
    1- 20 points for 3 sh
    2- 50 points for 10 sh
    3- 120 points for 20 sh
    4- 240 points for 40 sh
    """)
    if choice == "0":
        return
    elif choice == "1":
        puy_points(3, 20)
    elif choice == "2":
        puy_points(10, 50)
    elif choice == "3":
        puy_points(20, 120)
    elif choice == "4":
        puy_points(40, 240)


def games():
    global points
    choice = input("""
    enter your choice:
    0- exit
    1- rollate
    2- doron
    3- X&O
    4- safe box
    """)
    if choice == "0":
        return
    elif choice == "1":
        rollate.start()
        points = rollate.point
    elif choice == "2":
        doron.start()
        points = doron.point
    elif choice == "3":
        z_x_o.start()
        points = z_x_o.point
    elif choice == "4":
        safe_box.start()


def play():
    point_games(points)
    choice = input("""
    {0}
    enter your choice:
    0- back to account page
    1- add points
    2- games
    """.format(points))
    if choice == "0":
        return
    elif choice == "1":
        add_points()
    elif choice == "2":
        games()
    else:
        print("enter valid choice")
        play()
    play()
