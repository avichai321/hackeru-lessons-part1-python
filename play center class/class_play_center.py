from Methods import class_user_methods as c_um
from Games import oron_play, lotery, chokudate, XO
from time import sleep

player = {}
admin = c_um.User()
admin.load_u("admin" ,"admin" ,"admin" ,"admin123",True, 0, 0, 1)
player.update ({admin.username: admin})

print("play center - by Avichai (Avicii) Dahan\n")

def menu():
    choise = input("welcome to play center login\nplease choose one of the options:\n1.load a points file (if you want to continue from where you stop last time)\n2.User options\n3.Play center ((Remember you need to login before you can play))\n4.Quit and save in excel file\n>>")
    if choise == "1":
        c_um.read_excel_to_dict(player)
        menu()
    elif choise == "2":
        user_options(player)
    elif choise == "3":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        play_center(username, password, player)
    elif choise == "4":
        c_um.write_excel_from_dict_in_list(player)
        c_um.write_excel_from_dict_in_list_points(player)
        print("we saving your scores")
        sleep(2)
        print("Thanks for using our system bye bye")
        return
    else:
        print("please 1-4 only!")
        menu()

def user_options(player):
    choise = input("User options:\n0.user info\n1.Create user\n2.Login\n3.Logout\n4.Change name\n5.Change password\n6.Remove block(only admin)\n7.Give admin permission(only admin)\n8.Erase user from Users list (only admin)\n9.Main menu\n>> ")
    if choise == "9":
        menu()
        return
    username = input("Enter username: ")
    password = input("Enter password: ")
    mail1 = c_um.User()
    if choise == "1":
        x = mail1.create_user(username, password ,player)
        if x == True:
            player.update({mail1.username: mail1})
            print("the user was created")
        else:
            print("this user already exist!")
    elif choise == "8":
        print(player)
        x = mail1.erase_user(username, password, player)
        if x == False:
            print("The user is not exist!")
        else:
            player.pop(x)
            print("The user erased successfully")
    elif choise != "1" and choise != "8":
        for k in player:
            player1 = player[k]
            if (player1.username == username):
                if choise == "0":
                    player1.info(player, username, password)
                elif choise == "2":
                    player1.login(username, password)
                elif choise == "3":
                    player1.logout(username, password)
                elif choise == "4":
                    player1.change_name(username, password)
                elif choise == "5":
                    player1.change_password(username, password)
                elif choise == "6":
                    player1.release_block(username, password, player)
                elif choise == "7":
                    player1.get_admin(username, password, player)
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
        if username == player[u].username and player[u].password == password:
            if player[u].status_login == True:
                player[u].say_hola(username)
                choise = input("welcome to play center\nchoose one of the options:\n0.return to main menu\n1.oron play\n2.lottery\n3.chokudate\n4.tic tac toe(users clash! ,2 users neads at least 10 points)\n>>")
                if choise == "0":
                    menu()
                    return
                elif choise == "1":
                    z = oron_play.oron_play1()
                    player[u].points += int(z)
                    print(player[u].username + " points : " + str(player[u].points))
                elif choise == "2":
                    if player[u].points >= 5 and player[u].points % 5 == 0:
                        print("your points: " + str(player[u].points))
                        down_p = int(input("how many points you want to expend in 5 multiplication "))
                        if down_p % 5 == 0:
                            player[u].points -= down_p
                            x = lotery.lottery(down_p)
                            print(player[u].username + " points : " + str(player[u].points))
                            if x == 0:
                                print("sorry you earned no points")
                            else:
                                player[u].points += int(x)
                                print("your points right now: " + str(player[u].points))
                        else:
                            print("please insert amount divided by 5 ")
                    else:
                        print("you don`t have enough points, please play other game and comeback later ")
                elif choise == "3":
                    x = chokudate.game()
                    player[u].points += int(x)
                elif choise == "4":
                    username2 = (input("Enter second user name to play with: "))
                    password2 = (input("Enter second user password to play with: "))
                    for u2 in player:
                        if username2 == player[u2].username:
                            p2 = player[u2].login(username2, password2)
                            if p2 == True:
                                if player[u].points >= 10 and player[u2].points >= 10:
                                    x = XO.game(player[u].first, player[u2].first)
                                    if x == player[u2].first:
                                        player[u2].points += 10
                                        player[u].points -= 10
                                    else:
                                        player[u].points += 10
                                        player[u2].points -= 10
                                    print(player[u].username + " points : " + str(player[u].points) + "\n" + player[u2].username + " points : " + str(player[u2].points))
                            else:
                                print("one other following users doesn't have enough points, please get points and comeback")
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

menu()






