from Methods import play_center_methods as p_um
from Games import oron_play, lotery, chokudate, XO
from time import sleep

player =[
    {"first": "admin", "last": "admin", "username": "admin", "password": "admin123", "status_login": True, "points": 0, "block": 0, "admin": 1},
    {"first": "avichai", "last": "dahan","username": "avichai123", "password": "123456", "status_login": True, "points": 50, "block": 0, "admin" : 0},
    {"first": "avicii", "last": "dahan", "username": "avicii321", "password": "123456", "status_login": True, "points": 50, "block": 0, "admin": 0}
    ]
print("play center - by avichai (avicii) Dahan\n")
def menu():
    choise = input("welcome to play center login\nplease choose one of the options:\n1.load a points file (if you want to continue from where you stop last time)\n2.User options\n3.Play center ((Remember you need to login before you can play))\n4.Quit and save in excel file\n>>")
    if choise == "1":
        p_um.read_excel_to_dict(player)
        menu()
    elif choise == "2":
        user_options(player)
    elif choise == "3":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        play_center(username, password, player)
    elif choise == "4":
        p_um.write_excel_from_dict_in_list(player)
        p_um.write_excel_from_dict_in_list_points(player)
        print("we saving your scores")
        sleep(2)
        print("Thanks for using our system bye bye")
        return
    else:
        print("please 1-4 only!")
        menu()
def user_options(player):
    choise = input("User options:\n0.user info\n1.Create user\n2.Login\n3.Logout\n4.Change name\n5.Change password\n6.Remove block(only admin)\n7.Give admin permission(only admin)\n8.Erase user from Users list (only admin)\n9.Main menu\n>> ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if choise == "0":
        p_um.info(player,username,password)
    elif choise == "1":
        p_um.create_user(player, username, password)
    elif choise == "2":
        p_um.login(player, username, password)
    elif choise == "3":
        p_um.logout(player)
    elif choise == "4":
        p_um.change_name(username, password, player)
    elif choise == "5":
        p_um.change_password(player)
    elif choise == "6":
        p_um.release_block(username, password, player)
    elif choise == "7":
        p_um.get_admin(username, password, player)
    elif choise == "8":
        p_um.erase_user(username,password,player)
    elif choise == "9":
        menu()
        return
    else:
        print("please choose one of the options")
        user_options(player)
    exit = input("Are you done?:\n1.user menu\npress enter to return main menu\n >>")
    if exit == "1":
        user_options(player)
    else:
        menu()
def play_center(username,password,player):
    print("***********************")
    for u in player:
        if username == u["username"] and u["password"] == password:
            if u["status_login"] == True:
                p_um.say_hola(player, username)
                choise = input("welcome to play center\nchoose one of the options:\n0.return to main menu\n1.oron play\n2.lottery\n3.chokudate\n4.tic tac toe(users clash!, 2 users neads at least 10 points)\n>>")
                if choise == "0":
                    menu()
                    return
                elif choise == "1":
                    x = oron_play.oron_play1()
                    u["points"] += int(x)
                    print(u["username"] + " points : " + str(u["points"]))
                elif choise == "2":
                    if u["points"] >= 5 and u["points"] % 5 == 0:
                        print("your points: " + str(u["points"]))
                        down_p = int(input("how many points you want to expend in 5 multiplication "))
                        if down_p % 5 == 0:
                            u["points"] -= down_p
                            x = lotery.lottery(down_p)
                            print(u["username"] + " points : " + str(u["points"]))
                            if x == 0:
                                print("sorry you earned no points")
                            else:
                                u["points"] += int(x)
                                print("your points right now: " + str(u["points"]))
                        else:
                            print("please insert amount divided by 5 ")
                    else:
                        print("you don`t have enough points, please play other game and comeback later ")
                elif choise == "3":
                    x = chokudate.game()
                    u["points"] += int(x)
                elif choise == "4":
                    username2 = (input("Enter second user name to play with: "))
                    password2 = (input("Enter second user password to play with: "))
                    p2 = p_um.login(player,username2, password2)
                    if p2 == True:
                        for u2 in player:
                            if username2 == u2["username"]:
                                if u["points"] >= 10 and u2["points"] >= 10:
                                    x = XO.game(u["first"], u2["first"])
                                    if x == u2["first"]:
                                        u2["points"] += 10
                                        u["points"] -= 10
                                    else:
                                        u["points"] += 10
                                        u2["points"] -= 10
                                    print(u["username"] + " points : " + str(u["points"]) + "\n" + u2["username"] + " points : " + str(u2["points"]))
                                else:
                                    print("one other following users doesn't have enough points, please get points and comeback")
                    else:
                        print("something wrong try again")
                else:
                    print("press only one of the following numbers")
                play_center(username, password, player)
            else:
                print("you need to login first")
    exit = input("press one of the options\n1.play center\nelse: main menu")
    if exit == "1":
        play_center(username, password, player)
    else:
        menu()
        return


menu()

