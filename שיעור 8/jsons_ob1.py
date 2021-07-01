import json

json_ob = '["bamba", "avicii", "vcb"]'
print(json_ob)
print(type(json_ob))

python_list = json.loads(json_ob)
print(python_list)
print(type(python_list))

list1 = ["bamba", "avicii", "vcb"]
ob_json = json.dumps(list1)
print(type(ob_json))
print(ob_json)