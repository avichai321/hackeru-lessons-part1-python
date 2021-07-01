print("into oop_class_inherit.py ")

'''
what is inherit?
how to create sub class?
how to call constructor in sub class?
what the object can do?
'''


class Person:
    def __init__(self, first, last, age, city):
        self.first = first
        self.last = last
        self.age = age
        self.city = city

    def say_hola(self):
        print('Hola ' + self.first + " I'm from " + self.city)


class User(Person):

    def __init__(self, first, last, age, city, username, password):
        Person.__init__(self, first, last, age, city)
        self.password = password
        self.username = username
        self.uLogin = False
        print()

    def login(self, uName, uPass):
        if uName == self.username and uPass == self.password:
            self.uLogin = True
            print("user login")
            return True
        else:
            print("user NOT login")
            return False


u1 = User("Gal", "Lavi", 32, "Tel-Aviv", "gallavi", "gal123")
u1.say_hola()  # Hola Gal I'm from Tel-Aviv

u1.city = "Ramat-Gan"
u1.say_hola()  # Hola Gal I'm from Ramat-Gan

u1.login("gallavvfvf", "gavfl123")  # user NOT login
u1.login("gallavi", "gal123")  # user login



