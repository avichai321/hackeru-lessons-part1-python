fruit =["Watermelon", "Grapes" , "Peach" , "Banana" , "Apple" , "Pineapple" , "Starwberry"]
print(fruit)
print(type(fruit))
print(len(fruit))

print("\nget\n===========")
x = fruit[3]
print(x)
x = fruit[2:5]
print(x)

print("\nset\n===========")
fruit[5] = "Orange"
print(fruit)
fruit[2:5]= ["mango" , "blueberry" , "kiwi"]
print(fruit)

print("\nAdd\n===========")
fruit.append("Pear")
print(fruit)

print("\nDel\n===========")
del fruit[2]
print(fruit)

print("\nLoop\n===========")
for name in fruit:
    print(name)