from time import *

Exist_users = [
    ["avichai321@gmail.com", "avichai123", False, 0 ,1],
    ["avicii123@gmail.com", "avicii123", False, 0, 0],
    ["dahan202@gmail.com", "dahan202", False, 0, 0]
]


def get_options():
    choice =input("\nwellcome!\n==========\nPlease enter your choice:\n0.print all lists\n100.Stop the process\n\n1.Register your Email Address.\n2.Login to the system.\n3.logout your user from the system.\n4.Delete your user from the all system.\n5.Release from block (only admin user)\n6.Give admin premissoins (only admin user)\n")
    if choice == "0":
        info()
        get_options()
    elif choice =="100":
        return print("Bye bye")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        logout()
    elif choice == "4":
        delete()
    elif choice == "5":
        release_block()
    elif choice == "6":
        Get_admin()
    else:
        print("Enter one following numbers only!!!\n")
        get_options()
    sleep(2)
    get_options()

def info():
    List_choise=input("which list you want to see?\n1.All users\n2.Logged users\n3.Blocked users\n4.everything (only admin) ")
    if List_choise == "1":
        for i in range(len(Exist_users)):
            print(Exist_users[i][0])
            sleep(1)
    elif List_choise == "2":
        for lu in range(len(Exist_users)):
            if Exist_users[lu][2] == True:
                print(Exist_users[lu][0])
                sleep(1)
            else:
                print("there are no logged in users")
    elif List_choise == "3":
        for lu in range(len(Exist_users)):
            if Exist_users[lu][3] >= 3:
                print(Exist_users[lu][0])
                sleep(1)
            else:
                print("there are no blocked users")
        print(3)
    elif List_choise == "4":
        username = input("Enter your Email address: ")
        password = input("Enter a password: ")
        for u in Exist_users:
            if username == u[0] and u[1] == password and u[3] < 3:
                if u[4] == 1:
                    for r in Exist_users:
                        print(r)
                        return
                sleep(1)
                print("This is not a admin user!")
                return
            elif username == u[0] and u[1] != password:
                print("username or password is incorrect!")
                sleep(1)
                print(str(2 - u[3]) + " trys are left!")
                u[3] += 1
                return


def register():
    username = input("Enter your Email address: ")
    password = input("Enter a password: ")
    for u in Exist_users:
        if username == u[0]:
            sleep(1)
            print("the user is already exist!\n")
            return
    Exist_users.append([username, password, False, 0, 0])
    sleep(1)
    print("The user added successfully!\n\n")
    return

def login():
    username = input("Enter your Email address: ")
    password = input("Enter a password: ")
    for u in Exist_users:
        if username == u[0] and u[1] == password and u[3] < 3:
                if u[2] == True:
                    sleep(1)
                    print("you already login in other device please logout!")
                    return
                u.remove(False)
                u.append(True)
                sleep(1)
                print("You are logged in - wellcome")
                return
        elif u[3] == 3:
                sleep(1)
                print("you user is blocked use other")
                return
        elif username == u[0] and u[1] != password:
            print("username or password is incorrect!")
            sleep(1)
            print(str(2-u[3]) + " trys are left!")
            u[3] += 1
            return
    sleep(1)
    print("the user not exist please register")

def logout():
    username = input("Enter your Email address: ")
    password = input("Enter a password: ")
    for u in Exist_users:
        if username == u[0] and u[1] == password and u[3] < 3:
            if u[2] == True:
                u.remove(True)
                u.append(False)
                sleep(1)
                print("you successfully logged out!")
                return
            sleep(1)
            print("you already logged out!")
            return
        elif u[3] == 3:
                sleep(1)
                print("you user is blocked use other")
                return
        elif username == u[0] and u[1] != password:
            print("username or password is incorrect!")
            sleep(1)
            print(str(2 - u[3]) + " trys are left!")
            u[3] += 1
            return
    print("the user not exist please register")

def delete():
    username = input("Enter your Email address: ")
    password = input("Enter a password: ")
    for u in Exist_users:
        if username == u[0] and u[1] == password and u[3] < 3:
            if u[2] == True:
                u.clear()
                sleep(1)
                print("The user has deleted successfully")
                return
            sleep(1)
            print("you need to login before you can delete a user")
        elif u[3] == 3:
            sleep(1)
            print("you user is blocked use other")
            return
        elif username == u[0] and u[1] != password:
            print("username or password is incorrect!")
            sleep(1)
            print(str(2 - u[3]) + " trys are left!")
            u[3] += 1
            return
    print("the user not exist please register")

def release_block():
    username = input("Enter your Email address: ")
    password = input("Enter a password: ")
    for u in Exist_users:
        if username == u[0] and u[1] == password and u[3] < 3:
            if u[4] == 1:
                for lu in range(len(Exist_users)):
                    if Exist_users[lu][3] >= 3:
                        print(Exist_users[lu][0])
                        sleep(1)
                        choise=input("\nEnter the username you want to release from block: ")
                        for u in Exist_users:
                            if choise == u[0]:
                                u.pop(3)
                                u.insert(3,0)
                                sleep(1)
                                print("the user has released from block")
                                return
                        print("something has went wrong!")
                        return
                    else:
                        sleep(1)
                        print("there are no blocked users")
                        return
            sleep(1)
            print("This is not a admin user!")
            return
        elif username == u[0] and u[1] != password:
            print("username or password is incorrect!")
            sleep(1)
            print(str(2 - u[3]) + " trys are left!")
            u[3] += 1
            return
    print("the user not exist!")

def Get_admin():
    username = input("Enter your Email address: ")
    password = input("Enter a password: ")
    for u in Exist_users:
        if username == u[0] and u[1] == password and u[3] < 3:
            if u[4] == 1:
                for i in range(len(Exist_users)):
                    print(Exist_users[i][0])
                    sleep(1)
                choise = input("\nEnter the username you want to give him admin premissions: ")
                for t in Exist_users:
                    if choise == t[0]:
                        t.pop()
                        t.append(1)
                        sleep(1)
                        print("the user is admin now")
                        return
                print("something has went wrong!")
                return
            sleep(1)
            print("This is not a admin user!")
            return
        elif username == u[0] and u[1] != password:
            print("username or password is incorrect!")
            sleep(1)
            print(str(2 - u[3]) + " trys are left!")
            u[3] += 1
            return
    print("the user not exist!")



get_options()