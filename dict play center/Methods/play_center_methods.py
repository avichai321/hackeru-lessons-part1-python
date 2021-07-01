import datetime, csv
from time import sleep

def write_excel_from_dict_in_list_points(list1):
    d = datetime.datetime.now()
    x = 'Score\play center ' + str(d.day) + " " + str(d.month) + " " + str(d.year) + " " + str(d.hour) + " " + str(d.minute) + '.csv'
    with open(x, 'a', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "points"])
        list1.pop(0)
        for u in list1:
            writer.writerow([u["first"], u["last"], u["points"]])
        file.close()
def write_excel_from_dict_in_list(list1):
    d = datetime.datetime.now()
    x = 'Users\play center ' + str(d.day) + " " + str(d.month) + " " + str(d.year) + '.csv'
    with open(x, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "username", "password", "status_login", "points", "block", "admin"])
        list1.pop(0)
        for u in list1:
            writer.writerow([u["first"], u["last"], u["username"], u["password"], u["status_login"], u["points"], u["block"], u["admin"]])
        file.close()
def read_excel_to_dict(player):
    choise = input("1.Load file from today\n2.To enter a date")
    if choise == "1":
        d = datetime.datetime.now()
        x = 'Users\play center ' + str(d.day) + " " + str(d.month) + " " + str(d.year) + '.csv'
        try:
            with open(x, 'r', newline="") as file:
                keys = ["first", "last", "username", "password", "status_login", "points", "block", "admin"]
                reader = csv.DictReader(file, fieldnames=keys)
                results = []
                for row in reader:
                    results.append(dict(row))
                results.pop(0)
                player.extend(results)
                file.close()
            sleep(1.5)
            print("Loaded your users successfully\n")
        except FileNotFoundError:
            print("Sorry there is no file that created today ,please enter other date or open new game\nReturning to the main menu")
    elif choise == "2":
        a = datetime.datetime(int(input("Enter the year: ")), int(input("Enter number of month: ")), int(input("Enter the day: ")))
        x = 'Users\play center ' + str(a.day) + " " + str(a.month) + " " + str(a.year) + '.csv'
        try:
            with open(x, 'r') as file:
                keys = ["first", "last", "username", "password", "status_login", "points", "block", "admin"]
                reader = csv.DictReader(file, fieldnames=keys)
                results = []
                for row in reader:
                    results.append(dict(row))
                results.pop(0)
                player.extend(results)
                file.close()
                print("Loaded your users successfully")
        except FileNotFoundError:
            print("Sorry the file is not Exist please enter other date or open new game\nReturning to the main menu")

    else:
        print("Press only 1 or 2")
def say_hola(player,username):
    x = datetime.datetime.now()
    h = x.hour
    for u in player:
        if u["username"] == username:
            if 6 <= h < 12:
                print("\nboker tova " + str(u["first"]) + " " + str(u["last"]) + " boom boom boom!")
            elif 12 <= h < 18:
                print("\nGood afternoon " + str(u["first"]) + " " + str(u["last"]) + " boom boom boom!")
            elif 18 <= h < 21:
                print("\nGood evening " + str(u["first"]) + " " + str(u["last"]) + " boom boom boom!")
            else:
                print("\nGood night " + str(u["first"]) + " " + str(u["last"]) + " boom boom boom!")
def change_name(username, password, player):
    for u in player:
        if username == u["username"] and password == u["password"]  and u["block"] != 3:
            if u["status_login"] == True:
                u["first"] = input("Enter new first name")
                u["last"] = input("Enter new last name")
            elif u["status_login"] == False:
                print("you need to login before changing a name")
        elif username == u["username"] and password != u["password"]:
            if u["block"] != 3:
                print("something wrong")
                u["block"] += 1
            elif u["block"] == 3:
                print("you are blocked")
def create_user(player, username, password):
    for u in player:
        if username != u["username"]:
            f_name = input("please Enter your first name: ")
            L_name = input("please Enter your last name: ")
            player.append({"first": f_name, "last": L_name, "username": username, "password": password, "status_login": False, "points": 0, "block": 0, "admin" : 0})
            print("your user was created successfully")
        else:
            print("this user is exist")
    m = input("press option:\n1.add another user\nelse back to user menu\n>> ")
    if m == "1":
        create_user(player, username, password)
    else:
        return
def block(username, player):
    if player["username"] == username:
        if player["block"] != 3:
            player["block"] += 1
            return print("you left a " + str(3 - player["block"]) + " trys")
        else:
            return print("you are blocked")
def login(player, username, password):
    for u in player:
        if  username == u["username"] and password == u["password"] and u["block"] != 3:
            if u["status_login"] == True:
                print("you already logged in")
            else:
                u["status_login"] = True
                print("you successfully logged in")
            return True
        elif username == u["username"] and password != u["password"]:
            if u["block"] != 3:
                block(username, u)
            else:
                print("you are blocked")
                return False
def logout(player):
    chack = 0
    username = input("Enter your username")
    password = input("Enter your password")
    while chack == 0:
        for u in player:
            if username == u["username"] and password == u["password"]  and u["block"] != 3:
                if u["status_login"] == True:
                    u["status_login"] = False
                    print("you have logged out successfully if you want to play you need to login ")
                else:
                    print("you already logged out")
                chack = 1
            elif username == u["username"] and password != u["password"]:
                if u["block"] != 3:
                    block(username, u)
                else:
                    print("you are blocked")
                    chack = 1
def change_password(player):
    chack = 0
    username = input("Enter your username")
    password = input("Enter your password")
    while chack == 0:
        for u in player:
            if username == u["username"] and password == u["password"] and u["block"] != 3:
                new_password = input("Enter new password")
                new_password2 = input("Please repeat your new password")
                if new_password == new_password2:
                    u["password"] = new_password
                    chack = 1
                else:
                    print("your passwords not similar")
            elif username == u["username"] and password != u["password"]:
                if u["block"] != 3:
                    block(username, u)
                else:
                    print("you are blocked")
                    chack = 1
def info(player, username, password):
    chack = 0
    choise = input("Choose the info you want:\n1.for points and login information\n2.for full player information (only user with admin permission)")
    if choise == "1":
        while chack == 0:
            for u in player:
                if username == u["username"] and password == u["password"] and u["block"] != 3:
                    print("username: " + str(u["username"]) + " status login: " + str(
                        u["status_login"] + " points: " + u["points"]))
                    sleep(1)
                    chack = 1
                elif username == u["username"] and password != u["password"]:
                    if u["block"] != 3:
                        block(username, u)
                    else:
                        print("you are blocked")
                        chack = 1
    elif choise == "2":
        while chack == 0:
            for u in player:
                if username == u["username"] and password == u["password"] and u["block"] != 3:
                    if u["admin"] == 1:
                        for u2 in player:
                            print(u2)
                            sleep(1)

                    else:
                        print("This user don`t have admin permission")
                    chack = 1
                elif username == u["username"] and password != u["password"]:
                    if u["block"] != 3:
                        block(username, u)
                    else:
                        print("you are blocked")
                        chack = 1
    else:
        print("Enter 1 or 2 only!")
        info(player, username, password)

def release_block(username, password, player):
    chack = 0
    while chack == 0:
        for u in player:
            if (username == u["username"] and password == u["password"] and u["block"] != 3) or (username == "admin" and password == "admin123"):
                if u["admin"] == 1:
                    c_pass = input("Enter the username you want to cancel his block")
                    for u2 in player:
                        if u2["username"] == c_pass:
                            u2["block"] = 0
                        else:
                            print("This user is not exist!")
                chack = 1
            elif username == u["username"] and password != u["password"]:
                if u["block"] != 3:
                    block(username, u)
                else:
                    print("you are blocked")
                    chack = 1

def get_admin(username, password, player):
    chack = 0
    while chack == 0:
        for u in player:
            if (username == u["username"] and password == u["password"] and u["block"] != 3) or (username == "admin" and password == "admin123"):
                if u["admin"] == 1:
                    c_pass = input("Enter the username you want to change his permissions")
                    for u2 in player:
                        if u2["username"] == c_pass:
                            u2["admin"] = 1
                        else:
                            print("This user is not exist!")
                    chack = 1
            elif username == u["username"] and password != u["password"]:
                if u["block"] != 3:
                    block(username, u)
                else:
                    print("you are blocked")
                    chack = 1


def erase_user(username, password, player):
    chack = 0
    while chack == 0:
        for u in player:
            if (username == u["username"] and password == u["password"] and u["block"] != 3) or (username == "admin" and password == "admin123"):
                if u["admin"] == 1:
                    c_pass = input("Enter the username you want to erase from users list")
                    for u2 in player:
                        if u2["username"] == c_pass:
                           player.pop(u2)
                           print("The user erased successfully")
                        else:
                            print("This user is not exist!")
                    chack = 1
            elif username == u["username"] and password != u["password"]:
                if u["block"] != 3:
                    block(username, u)
                else:
                    print("you are blocked")
                    chack = 1