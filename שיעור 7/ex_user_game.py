User_bank_account = {"first": "gal", "last": "lavi", "username": "gallavi", "password": "gal123", "status_login": False, "total": 0, "credit": 500 , "block": 0 }




def say_hola():
    print("hello " + str(User_bank_account["first"]) + " " + str(User_bank_account["last"]) + " !")


def block_user(username):
    for key, val in User_bank_account.items():
        if val == username:
            User_bank_account["block"] += 1


def logout(username):
    for key, val in User_bank_account.items():
        if val == username:
            User_bank_account["status_login"] = False
            print("you successfully logout")




def login():
    flag = 0
    while flag == 0:
        username = input("Enter Username")
        password = input("Enter Password")
        if username == User_bank_account["username"] and password == User_bank_account["password"]:
            User_bank_account["status_login"] = True
            flag = 1
        else:
            print("wrong username or password")
            print(User_bank_account["block"])
            block_user(username)
            if User_bank_account["block"] == 3:
                User_bank_account["status_login"] = False
                print("you are blocked")
                flag = 1
    if User_bank_account["block"] < 3:
        say_hola()
        c = input("\nwhat you want to do totay?:\nfor logout press 1\nfor hafkada press 2\nfor out mounny press 3\nfor change credit press 4\n")
        if c == "4":
            print("thank you for using our system bye bye")




def change_name():
    status = input("Enter 0 if you want to change First name 1 if you want to change Last name prees enter to both\n")
    if status =='0':
        fn = input('Enter first name')
        User_bank_account["first"] = fn
    elif status == '1':
        Ln = input('Enter last name')
        User_bank_account["last"] = Ln
    else:
        fn = input('Enter first name')
        Ln = input('Enter last name')
        User_bank_account["first"] = fn
        User_bank_account["last"] = Ln

def change_password():
    flag = 0
    while flag == 0:
        pass1 = input("Enter new password")
        if pass1 == User_bank_account["password"]:
            print("this password already in use")
        else:
            User_bank_account["password"] = pass1
            flag = 1
    print(User_bank_account)