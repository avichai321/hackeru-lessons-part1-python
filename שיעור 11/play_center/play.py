import json
import datetime
import z_play_center as p_c
import z_bank_account as bank


alert = ""
alert2 = ""

class user_account:
    __users = {"guest": {"username": "guest", "fullname": "guest", "password": "", "is_login": True, "points": 50}}
    __username = ""
    fullname = "guest"
    __password = ""
    is_login = False
    points = 0
    alert = ""
    def reg(self):
        file = open("play_center_data.json")
        self.__users = json.load(file)
        file.close()
        self.__username = input("enter username")
        self.fullname = input("enter first name") + " " + input("enter last name")
        self.__password = input("enter password")
        __password2 = input("enter password again")
        if self.__username not in self.__users.keys():
            if self.__password == __password2:
                self.is_login = True
                self.points = 100
                self.__users[self.__username] = {"username": self.__username, "fullname": self.fullname,
                                                 "password": self.__password, "is_login": self.is_login,
                                                 "points": self.points}
                data = json.dumps(self.__users)
                file = open("play_center_data.json", "w")
                file.write(data)
                self.say_hola()
                self.alert = "thanx for signup"
            else:
                self.alert = "the tow password not match, try again"
        else:
            self.alert = "this username has been used, try another,"


    def login(self):
        file = open("play_center_data.json")
        self.__users = json.load(file)
        file.close()
        for i in range(3):
            username = input("enter username")
            password = input("enter password")
            if username in self.__users.keys():
                if password == self.__users[username]["password"]:
                    self.__username = self.__users[username]["username"]
                    self.fullname = self.__users[username]["fullname"]
                    self.__password = self.__users[username]["password"]
                    self.points = self.__users[username]["points"]
                    self.is_login = True
                    self.__users[username]["is_login"] = True
                    self.say_hola()
                    data = json.dumps(self.__users)
                    file = open("play_center_data.json", "w")
                    file.write(data)
                    return
                else:
                    print("wrong username or password")
            else:
                print("wrong username or password")
        self.alert = "too many tries, try again another time"


    def logout(self):
        self.is_login = False
        self.__users[self.__username]["is_login"] = False
        self.alert = "good by"
        data = json.dumps(self.__users)
        file = open("play_center_data.json", "w")
        file.write(data)


    def change_password(self):
        for i in range(3):
            password = input("enter bast password")
            password2 = input("enter new password")
            password3 = input("enter new password again")
            if password == self.__password:
                if password2 == password3:
                    self.__users[self.__username]["password"] = password2
                    self.alert = "your password successful chang"
                    data = json.dumps(self.__users)
                    file = open("play_center_data.json", "w")
                    file.write(data)
                    return
                else:
                    print("the tow new passwords not match")
            else:
                print("wrong password try again")
        self.alert = "too many tries, try again another time"


    def change_fullname(self):
        fullname = input("enter first name") + " " + input("enter last name")
        self.fullname = fullname
        self.__users[self.__username]["fullname"] = fullname
        self.alert = "your fullname successful change"
        data = json.dumps(self.__users)
        file = open("play_center_data.json", "w")
        file.write(data)


    def save(self):
        self.__users[self.__username] = {"username": self.__username, "fullname": self.fullname,
                                         "password": self.__password, "is_login": self.is_login, "points": self.points}
        data = json.dumps(self.__users)
        file = open("play_center_data.json", "w")
        file.write(data)
        self.alert = "saved"

    def say_hola(self):
        time1 = datetime.datetime.now()
        if 6 <= time1.hour < 11:
            return "good morning {0}".format(self.fullname)
        elif 11 <= time1.hour < 14:
            return "good noon {0}".format(self.fullname)
        elif 14 <= time1.hour < 18:
            return "good afternoon {0}".format(self.fullname)
        elif 18 <= time1.hour < 21:
            return "good evening {0}".format(self.fullname)
        else:
            return "good night {0}".format(self.fullname)



class guest_account(user_account):
    def __init__(self):
        self.fullname = "guest"
        self.points = 50
        self.is_login = False
        self.say_hola()


def log():
    global user, alert, alert2
    while True:
        alert = "{0}enter yor choice".format(alert2)
        choice = input("""
            {0}
            0- back to main page
            1- login to your play center account
            2- continue as guest
        """.format(alert))
        if choice == "0":
            return
        elif choice == "1":
            user = user_account()
            user.login()
            if user.is_login:
                p_c.points = user.points
            break
        elif choice == "2":
            user = guest_account()
            p_c.points = user.points
            break
        else:
            alert2 = "enter valid choice, "


user = user_account()
def start():
    global user, alert, alert2
    alert = "{0}enter your choice:".format(alert2)
    try:
        if user.is_login:
            alert_login = """3- play center
         4- logout
         5- save
         6- change password
         7- change fullname
         8- bank account"""
        else:
            alert_login = """0- exit
         1- signup
         2- login
         3- play center
         8- bank account"""
    except:
        alert_login = """0- exit
         1- signup
         2- login
         3- play center
         8- bank account"""
    in_put = input("""         main page:
         {3}
         {4}
         {0}
         points: {2}
         {1}
    """.format(alert, alert_login, user.points, user.alert, user.say_hola()))
    if in_put == "0":
        if user.is_login:
            alert2 = "logout before, "
        else:
            return
    elif in_put == "1":
        if user.is_login:
            alert2 = "logout before, "
        else:
            user = user_account()
            user.reg()
    elif in_put == "2":
        if user.is_login:
            alert2 = "logout before, "
        else:
            log()
    elif in_put == "3":
        p_c.play()
        user.points = p_c.points
    elif in_put == "4":
        try:
            user.logout()
            user = user_account()
            p_c.points = user.points
        except:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "5":
        if user.is_login:
            user.save()
        else:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "6":
        if user.is_login:
            user.change_password()
        else:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "7":
        if user.is_login:
            user.change_fullname()
        else:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "8":
        bank.start()
    else:
        alert2 = "enter valid choice, "
        user.alert = ""
    start()


start()
