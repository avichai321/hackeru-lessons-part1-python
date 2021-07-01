dict1 = {}
print(type(dict1))

user = {
    "user_name": "gallavi",
    "password": "gal123",
    "age": 32,
    "islogin": True
}

print(user)
print(type(user))
print(len(user))
print("=========")

x = user["user_name"]
print(x)
print("=========")


y = "password" in user
print(y)
print("=========")

user["city"] = "Tel-Aviv"
print(user)
print("=========")

user["age"] = 34
print(user)
print("=========")

del user["city"]
print(user)
print("=========")

for i in user:
    print(user[i])
print("=========")

