print("into demo byReference")

# x and y  >> by value
x = 10
y = x
x = 50
print(x)   # 50
print(y)  # 10


# list1 and list2  >> by reference
list1 = ["Gal", "Ben", "Tal", "Ran"]
list2 = list1
list2.append("Shlomi")

print(list1)   # ['Gal', 'Ben', 'Tal', 'Ran', 'Shlomi']
print(list2)   # ['Gal', 'Ben', 'Tal', 'Ran', 'Shlomi']
