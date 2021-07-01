citys =["Safed", "Tel Aviv" , "haifa" , "Afula" , "Natzrat" , "Eilat" , "Beer Sheva" , "Ramat Gan"]
print(citys)
print(type(citys))
print(len(citys))

print("\nget\n===========")
x = citys[1]
print(x)
x = citys[2:5]
print(x)

print("\nset\n===========")
citys[1] = "Jerusalem"
print(citys)
citys[3:6]= ["Ashdod" , "Ashkelon" , "Sderot"]
print(citys)

print("\nAdd\n===========")
citys.append("Petah Tikva")
print(citys)

print("\nDel\n===========")
del citys[3]
print(citys)

print("\nLoop\n===========")
for name in citys:
    print(name)