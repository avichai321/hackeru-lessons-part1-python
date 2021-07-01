user = {
    "first_name": "Gal",
    "last_name": "Lavi",
    "user_name": "gallavi",
    "password": "gal123",
    "age": 32,
    "isLogin": True
}
print(user)


# keys() - return list of dictionary keys  (TYPE: dict_keys)
x = user.keys()
print(x)  # x byReference to dictionary keys


# values() - return list of dictionary values  (TYPE: dict_values)
y = user.values()
print(y)  # y byReference to dictionary values


# popitem() - remove the last key+value, return key+value (TYPE: tuple)
b = user.popitem()
print(b)
print(user)


# pop(key) - gat key, remove key+value, return value (must to call method with key)
b = user.pop('last_name')
print(b)
print(user)


# update() - gat dict(keys+values), add the keys+values to end
user.update({'points': 25, 'login_status': False})
print(user)


# copy() - return copy of dict ( NOT By Reference )
new_user = user.copy()
new_user['new'] = 'item'
print(new_user)
print(user)


# clear() - delete all keys+values, the dict will stay empty
user.clear()
print(user)