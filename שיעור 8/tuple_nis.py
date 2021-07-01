tuple1 = ()
print(type(tuple1))

straw_hat = ("luffy", "zoro", "nami", "usoop", "sanji")

print(straw_hat)
print(straw_hat)
print(type(straw_hat)) # <class 'tuple'>
print(len(straw_hat)) # 6

x = straw_hat[1] # get
print(x)

x = "sanji" in straw_hat # search
print(x)


for i in straw_hat: # loop
    print(i)