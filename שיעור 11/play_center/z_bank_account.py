import json
import datetime


alert = ""
alert2 = ""

class user_account:
    __users = {"admin": {"username": "admin", "fullname": "admin", "password": "admin1234", "is_login": False,
                         "total": 0, "credit": 0}}
    __username = ""
    fullname = "gust"
    __password = ""
    is_login = False
    total = 0
    __credit = 0
    alert = ""
    def reg(self):
        file = open("bank_accounts.json")
        self.__users = json.load(file)
        file.close()
        self.__username = input("enter username")
        self.fullname = input("enter first name") + " " + input("enter last name")
        self.__password = input("enter password")
        __password2 = input("enter password again")
        if self.__username not in self.__users.keys():
            if self.__password == __password2:
                self.is_login = True
                self.total = 0
                self.__credit = 0
                self.__users[self.__username] = {"username": self.__username, "fullname": self.fullname,
                                                 "password": self.__password, "is_login": self.is_login,
                                                 "total": self.total, "credit": self.__credit}
                self.save()
                self.say_hola()
                self.alert = "thanx for signup"
            else:
                self.alert = "the tow password not match, try again"
        else:
            self.alert = "this username has been used, try another,"


    def login(self):
        file = open("bank_accounts.json")
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
                    self.total = self.__users[username]["total"]
                    self.__credit = self.__users[username]["credit"]
                    self.is_login = True
                    self.__users[username]["is_login"] = True
                    self.say_hola()
                    self.save()
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
        self.save()


    def change_password(self):
        for i in range(3):
            __password = input("enter bast password")
            __password2 = input("enter new password")
            __password3 = input("enter new password again")
            if __password == self.__password:
                if __password2 == __password3:
                    self.__users[self.__username]["password"] = __password2
                    self.alert = "your password successful chang"
                    self.save()
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
        self.save()


    def withdrawal(self):
        while True:
            try:
                amount = int(input("enter amount to withdrawal"))
                break
            except:
                print("your enter must be number")
        if (self.total + self.__credit) >= amount:
            self.total -= amount
            self.__users[self.__username]["total"] -= amount
            self.alert = "thanx, take your money"
            self.save()
        else:
            self.alert = "you don't have enough money to withdrawal"


    def deposit(self):
        while True:
            try:
                amount = int(input("enter amount to deposit"))
                break
            except:
                print("your enter must be number")
        self.total += amount
        self.__users[self.__username]["total"] += amount
        self.alert = "thanx, you successful deposit your money"
        self.save()

    def pay(self, payment):
        self.login()
        if self.is_login:
            if (self.total + self.__credit) >= payment:
                self.total -= payment
                self.__users[self.__username]["total"] -= payment
                self.logout()
                self.save()
                return True
            else:
                return False
        else:
            return False


    def save(self):
        data = json.dumps(self.__users)
        file = open("bank_accounts.json", "w")
        file.write(data)


    def admin_login(self):
        for i in range(3):
            __password = input("enter admin password")
            if __password == self.__users["admin"]["password"]:
                self.__username = "admin"
                self.fullname = "admin"
                self.is_login = True
                self.say_hola()
                return
            else:
                print("wrong password try again")
        self.alert = "too many tries, try again another time"


    def change_credit(self):
        file = open("play_center_data.json")
        self.__users = json.load(file)
        file.close()
        username = input("enter username to change credit for it")
        if username in self.__users:
            while True:
                try:
                    new_credit = int(input("enter new credit"))
                    break
                except:
                    print("your enter must be number")
        else:
            self.alert = "that username not found, try another"
            return
        self.__users[username]["credit"] = new_credit
        self.is_login = False
        self.alert = "{0}'s credit successful change"
        self.save()


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


def log():
    global user, alert, alert2
    while True:
        alert = "{0}enter yor choice".format(alert2)
        choice = input("""
            {0}
            0- back to main page
            1- login to your bank account
            2- login as admin
        """.format(alert))
        if choice == "0":
            return
        elif choice == "1":
            user = user_account()
            user.login()
            break
        elif choice == "2":
            user = user_account()
            user.admin_login()
            break
        else:
            alert2 = "enter valid choice, "


user = user_account()
def start():
    global user, alert, alert2
    alert = "{0}enter your choice:".format(alert2)
    try:
        if user.is_login and user.fullname != "admin":
            alert_login = """3- logout
         4- withdrawal
         5- deposit
         6- change password
         7- change fullname
        """
        elif user.is_login and user.fullname == "admin":
            alert_login = """3- logout
         8- change credit
            """
        else:
            alert_login = """0- exit
         1- signup
         2- login"""
    except:
        alert_login = """0- exit
         1- signup
         2- login"""
    in_put = input("""         main page:
         {3}
         {4}
         {0}
         total: {2}
         {1}
    """.format(alert, alert_login, user.total, user.alert, user.say_hola()))
    if in_put == "0":
        user.alert = ""
        if user.is_login:
            alert2 = "logout before, "
        else:
            return
    elif in_put == "1":
        user.alert = ""
        if user.is_login:
            alert2 = "logout before, "
        else:
            user = user_account()
            user.reg()
    elif in_put == "2":
        user.alert = ""
        if user.is_login:
            alert2 = "logout before, "
        else:
            log()
    elif in_put == "3":
        user.alert = ""
        try:
            if user.fullname == "admin":
                user = user_account()
                user.alert = "good by"
            else:
                user.logout()
                user = user_account()
        except:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "4":
        user.alert = ""
        if user.is_login and user.fullname != "admin":
            user.withdrawal()
        else:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "5":
        user.alert = ""
        if user.is_login and user.fullname != "admin":
            user.deposit()
        else:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "6":
        user.alert = ""
        if user.is_login:
            user.change_password()
        else:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "7":
        user.alert = ""
        if user.is_login and user.fullname != "admin":
            user.change_fullname()
        else:
            alert2 = "enter valid choice, "
            user.alert = ""
    elif in_put == "8":
        user.alert = ""
        if user.is_login and user.fullname == "admin":
            user.change_credit()
        else:
            alert2 = "enter valid choice, "
            user.alert = ""
    else:
        alert2 = "enter valid choice, "
        user.alert = ""
    start()

