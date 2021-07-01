import datetime ,csv
from time import sleep



class User():
    def __init__ (self):
        self.first = "first"
        self.last = "last"
        self.username = "username"
        self.password = "password"
        self.status_login = False
        self.points = 0
        self.block = 0
        self.admin = 0

    def load_u(self, first, last, username, password, status_login, points, block, admin):
        self.first = first
        self.last = last
        self.username = username
        self.password = password
        self.status_login = status_login
        self.points = points
        self.block = block
        self.admin = admin

    def create_user (self, username, password ,player):
            if username in player:
                return False
            else:
                self.first = input("Enter your first name: ")
                self.last = input("Enter your last name: ")
                self.username = username
                self.password = password
                self.status_login = False
                self.points = 0
                self.block = 0
                self.admin = 0
                return True

    def erase_user(self, username, password, player):
        chack = 0
        while chack == 0:
            if (username == self.username and password == self.password and self.block != 3 and self.admin == 1) or (username == "admin" and password == "admin123"):
                e_user = input("Enter the username you want to erase: ")
                for k in player:
                    if k == e_user:
                        print("we erasing now the user!")
                        return e_user
                    else:
                        return False
                chack = 1
            elif username == self.username and password != self.password:
                if self.block != 3:
                    User.block(self, username)
                else:
                    print("you are blocked")
                    chack = 1
            else:
                print("please check your user maybe is not exist or you don`t have admin permission")
    def release_block(self, username, password, player):
        chack = 0
        while chack == 0:
            if (username == self.username and password == self.password and self.block != 3 and self.admin == 1) or (username == "admin" and password == "admin123"):
                c_pass = input("Enter the username you want to cancel his block: ")
                for k in player:
                    if k == c_pass:
                        player[k].block = 0
                        print("This block has canceled!")
                    else:
                        print("This user is not exist!")
                chack = 1
            elif username == self.username and password != self.password:
                if self.block != 3:
                    User.block(self, username)
                else:
                    print("you are blocked")
                    chack = 1
            else:
                print("please check your user maybe is not exist or you don`t have admin permission")
    def get_admin(self, username, password, player):
        chack = 0
        while chack == 0:
            if (username == self.username and password == self.password and self.block != 3 and self.admin == 1) or (username == "admin" and password == "admin123"):
                c_pass = input("Enter the username you want to change his permissions: ")
                for k in player:
                    if k == c_pass:
                        player[k].admin = 1
                        print("This user get admin permission!")
                    else:
                        print("This user is not exist!")
                    chack = 1
            elif username == self.username and password != self.password:
                if self.block != 3:
                    User.block(self, username)
                else:
                    print("you are blocked")
                    chack = 1
            else:
                print("please check your user maybe is not exist or you don`t have admin permission")
    def info(self, player, username, password):
        chack = 0
        choise = input("Choose the info you want:\n1.for points and login information\n2.for full player information (only user with admin permission)")
        if choise == "1":
            while chack == 0:
                if self.username == username and self.password == password and self.block != 3 or (username == "admin" and password == "admin123"):
                    for u in player:
                         print("username: " + player[u].username + " status login: " + str(player[u].status_login) + " points: " + str(player[u].points))
                         sleep(1)
                    chack = 1
                elif username == self.username and password != self.password:
                     if self.block != 3:
                         User.block(self, username)
                     else:
                         print("you are blocked")
                         chack = 1
        if choise == "2":
            while chack == 0:
                if (self.username == username and self.password == password and self.block != 3 and self.admin == 1) or (username == "admin" and password == "admin123"):
                    for u2 in player:
                        print("first: " + player[u2].first + " last: " + player[u2].last + " username: " + player[u2].username + " password: " + player[u2].password + " status login: " + str(player[u2].status_login) + " points: " + str(player[u2].points) + " block: " + str(player[u2].block) + " admin: " + str(player[u2].admin))
                        sleep(1)
                    chack = 1
                elif username == self.username and password != self.password:
                    if self.block != 3:
                        User.block(self, username)
                    else:
                        print("you are blocked")
                        chack = 1

    def say_hola(self, upass):
        x = datetime.datetime.now()
        h = x.hour
        if upass == self.username:
           if 6 <= h < 12:
                print("boker tova " + self.first + " " + self.last + " boom boom boom!")
           elif 12 <= h < 18:
                print("Good afternoon " + self.first + " " + self.last + " boom boom boom!")
           elif 18 <= h < 21:
                print("Good evening " + self.first + " " + self.last + " boom boom boom!")
           else:
                print("Good night " + self.first + " " + self.last + " boom boom boom!")

    def block(self, upass):
        if upass == self.username:
           if self.block != 3:
                self.block += 1
                return print("you left a " + str(3 - self.block) + " trys")
           else:
                return print("you are blocked")

    def login(self , upass, ppass):
           if upass == self.username and ppass == self.password and self.block != 3:
                if self.status_login == False:
                     self.status_login = True
                     print("you are logged in")
                else:
                     print("you already logged in")
                return True
           elif upass == self.username and ppass != self.password:
                if self.block != 3:
                     User.block(self, upass)
                else:
                    print("you are blocked")
                    return False

    def logout(self,upass, ppass):
        chack = 0
        while chack == 0:
           if upass == self.username and ppass == self.password:
                if self.status_login == True:
                     self.status_login = False
                     print("you are logged out")
                else:
                     print("you already logged out")
                chack = 1

           elif upass == self.username and ppass != self.password:
                if self.block != 3:
                     User.block(self, upass)
                else:
                     print("you are blocked")
                     chack = 1

    def change_name(self,upass ,ppass):
        chack = 0
        while chack == 0:
           if upass == self.username and ppass == self.password:
                if self.status_login == True:
                     self.first = input("Enter new first name")
                     self.first = input("Enter new last name")
                else:
                     print("you need to login before changing a name")
           elif upass == self.username and ppass != self.password:
                if self.block != 3:
                     User.block(self, upass)
                else:
                     print("you are blocked")
                     chack = 1

    def change_password(self, upass, ppass):
        chack = 0
        while chack == 0:
           if upass == self.username and ppass == self.password:
                new_password = input("Enter new password")
                new_password2 = input("Please repeat your new password")
                if new_password == new_password2:
                     self.password = new_password
                     chack = 1
                else:
                     print("your passwords not similar")
           elif upass == self.username and ppass != self.password:
                if self.block != 3:
                     User.block(self, upass)
                else:
                     print("you are blocked")
                     chack = 1



def read_excel_to_dict(player):
        choise = input("1.Load file from today\n2.To enter a date\n>> ")
        if choise == "1":
            d = datetime.datetime.now()
            x = 'Users\play center ' + str(d.day) + " " + str(d.month) + " " + str(d.year) + '.csv'
            try:
                with open(x, 'r', newline="") as file:
                    keys = ["first", "last", "username", "password", "status_login", "points", "block", "admin"]
                    reader = csv.DictReader(file, fieldnames=keys)
                    results = []
                    for i in reader:
                        results.append(i)
                    results.pop(0)
                    for k in results:
                        user1 = User()
                        user1.load_u(k["first"], k["last"], k["username"], k["password"], bool(k["status_login"]),int(k["points"]), int(k["block"]), int(k["admin"]))
                        player.update({user1.username: user1})
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
                    for i in reader:
                        results.append(i)
                    results.pop(0)
                    for k in results:
                        user1 = User()
                        user1.load_u(k["first"], k["last"], k["username"], k["password"], k["status_login"], k["points"],
                                     k["block"], k["admin"])
                        player.update({user1.username: user1})
                        print(player)
                    file.close()
                    sleep(1.5)
                    print("Loaded your users successfully\n")
            except FileNotFoundError:
                print("Sorry the file is not Exist please enter other date or open new game\nReturning to the main menu")

        else:
            print("Press only 1 or 2")
def write_excel_from_dict_in_list_points(player):
    d = datetime.datetime.now()
    x = 'Score\play center ' + str(d.day) + " " + str(d.month) + " " + str(d.year) + " " + str(d.hour) + " " + str(d.minute) + '.csv'
    with open(x, 'a' , newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "points"])
        for u in player:
            writer.writerow([player[u].first, player[u].last, player[u].points])
        file.close()
def write_excel_from_dict_in_list(player):
    d = datetime.datetime.now()
    x = 'Users\play center ' + str(d.day) + " " + str(d.month) + " " + str(d.year) + '.csv'
    with open(x, 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "username", "password", "status_login", "points", "block", "admin"])
        for u in player:
            writer.writerow([player[u].first, player[u].last, player[u].username, player[u].password, player[u].status_login, player[u].points, player[u].block, player[u].admin])
        file.close()





