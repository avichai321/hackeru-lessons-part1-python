print("into oop_class.py ")
'''
what is object?
how to get properties+values from object?
hoe to set properties+values of object?
how to add properties+values to object?
how to del properties+values to object?
'''


# create class
class Box:
    x = 0
    y = 0


# create object form class
# after we can change the ob..
box1 = Box()

print(box1.x)
print(type(box1.x))




print(type(box1))

foo = box1.x  # get ob
print(foo)

box1.y = 15  # set ob ( override the default )
print(box1.y)

box1.z = 10  # add to object (NOT to class)
print(box1.z)

del box1.y  # delete object property (NOT class property)
print(box1.y)  # return 0 (default set on main class - we can not change the default > only override  )

del box1.z
# print(box1.z)  # ERROR: AttributeError: 'Box' object has no attribute 'z'


