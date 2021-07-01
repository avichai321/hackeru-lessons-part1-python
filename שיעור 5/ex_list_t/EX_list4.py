Animes =["Naruto", "One Piece" , "Dragon Ball" , "Black Clover" , "AOT" , "Bleach" , "Fairy Tail" , "HxH"]
print(Animes)
print(type(Animes))
print(len(Animes))

print("\nget\n===========")
x = Animes[1]
print(x)
x = Animes[2:6]
print(x)

print("\nset\n===========")
Animes[1] = "Jujutsu Kaisen"
print(Animes)
Animes[3:6]= ["7ds" , "Dr Stone" , "Demon slayer"]
print(Animes)

print("\nAdd\n===========")
Animes.append("My Hero Academy")
print(Animes)

print("\nDel\n===========")
del Animes[3]
print(Animes)

print("\nLoop\n===========")
for name in Animes:
    print(name)

print(Animes.sort())
