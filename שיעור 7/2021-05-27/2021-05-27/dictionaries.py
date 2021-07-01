print("into dictionaries.py ")


dict1 = {}  # create
print(type(dict1))  # <class 'dict'>

# create
user = {
    "user_name": "gallavi",
    "password": "gal123",
    "age": 32,
    "isLogin": True
}
print("******************")

print(user)
print(type(user))  # <class 'dict'>
print(len(user))  # 4

x = user["user_name"]  # get
print(x)  # "gallavi"

y = "password" in user  # search
print(y)  # True

user["city"] = "Tel-Aviv"  # add
print(user)

user["age"] = 34  # set
print(user)

del user["city"]  # remove
print(user)

for key in user:  # loop
    print(user[key])


'''
dictionary is key:value collection collection (allow duplicate values but NOT keys)

create - YES - dict1 = {"first":"Gal","age":10}
get    - YES - dict1[key]  / .get(key) / keys() / values()
search - YES - name in names 
add    - YES - dict1[key] = x
set    - YES - dict1[key] = x
remove - YES - use .pop() / .popitem() / del / .clear()
loop   - YES - for i in dict1

join   - YES - use .update()
method - .values() / .keys() / .items() / .copy()

'''