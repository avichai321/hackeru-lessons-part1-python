print("into oop_class_methods.py ")
'''
what is methods? ( vs functions)
how to create methods?
how object call to functions?
'''


class Box:
    width = 0
    height = 0

    def set_info(self, w, h):
        self.width = w
        self.height = h

    def print_info(self):
        print("Box size: width = " + str(self.width) +
              " | height = " + str(self.height))


# create object from class
box1 = Box()
box1.print_info()  # Box size: width = 0 | height = 0
box1.set_info(50, 100)
box1.print_info()  # Box size: width = 50 | height = 100

box2 = Box()
box2.print_info()  # Box size: width = 0 | height = 0
box2.set_info(120, 80)
box2.print_info()  # Box size: width = 120 | height = 80


class Person():
    first = 'Israel'
    last = 'Israeli'
    age = 0

    def set_info(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def sayHola(self):
        return "Hola " + self.first + " " + self.last

    def birthday(self):
        self.age += 1
        return self.age


print("****************************************")
person1 = Person()
print(person1.sayHola())

person1.set_info('Gal', 'Lavi', 27)
print(person1.sayHola())
print(person1.age)  # 27

person1.birthday() # 28
print(person1.age) # 28

person1.birthday()
person1.birthday()
print(person1.age) # 30
