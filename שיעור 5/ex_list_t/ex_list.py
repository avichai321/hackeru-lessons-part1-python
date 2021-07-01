people =["Shaked", "Avicii" , "Or" , "Ygal" , "hila" ]
print(people)
print(type(people))
print(len(people))

print("\nget\n===========")
x = people[2]
print(x)
x = people[0:2]
print(x)

print("\nset\n===========")
people[1] = "Adi"
print(people)
people[2:4]= ["avicii" , "Or"]
print(people)

print("\nAdd\n===========")
people.append("natsu")
print(people)

print("\nDel\n===========")
del people[1]
print(people)

print("\nLoop\n===========")
for name in people:
    print(name)