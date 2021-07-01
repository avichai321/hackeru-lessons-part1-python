print("into oop_class.py ")
'''
what is constructor? ( vs functions)
how to create constructor?
how object call to constructor?
'''

print('Demo 1 -  constructor  ( def __init__ )')


class Box:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def print_info(self):
        print("Box size: width = " + str(self.width) +
              " | height = " + str(self.height))


box1 = Box(50, 100)
box1.print_info()  # Box size: width = 50 | height = 100

box2 = Box(60, 90)
box2.print_info()  # Box size: width = 60 | height = 90


class Person:
    def __init__(self, first, last, age, city):
        self.first = first
        self.last = last
        self.age = age
        self.city = city

    def sayHola(self):
        print("Hola " + self.first + " I'm from " + self.city)

    def birthday(self):
        self.age += 1
        return self.age

    def move_city_to(self, new_city):
        self.city = new_city


person1 = Person('Gal', 'Lavi', 27, "Tel-Aviv")

person1.sayHola()

person1.birthday()
print(person1.age)

person1.birthday()
person1.birthday()
print(person1.age)

person1.move_city_to("Ramat-Gan")
person1.sayHola()


