print("into jsons_ob.py")
import json

print("********** JSON >> dictionary **********")
# JSON Object:
json_ob = '{ "first":"Gal", "age":32, "city":"Tel-Aviv"}'
print(json_ob)
print(type(json_ob))  # <class 'str'>

# parse/casting/convert JSON object to Python dictionary:
python_dict = json.loads(json_ob)
print(python_dict)

# now we cen use like dictionary python:
print(python_dict["age"])

print("********** dictionary >> JSON **********")

# Python dictionary:
user = {
    "user_name": "gallavi",
    "password": "gal123",
    "age": 32,
    "isLogin": True
}

# dumps/casting/convert Python dictionary to JOSN object:
ob_json = json.dumps(user)

print(ob_json)
print(type(ob_json))


