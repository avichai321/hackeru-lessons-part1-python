print("into sets.py ")
'''
set is unordered and unindexed collection (NOT allow duplicate values)

create - YES - set1 = {"Gal",10}
get    - NOT - unindexed
search - YES - name in names 
add    - YES - use add() to add one value / update() to add collections 
set    - NOT - unindexed
remove - YES - use .pop() / .discard() / .remove()
loop   - YES - for i in set1:

join   - YES - use .update()
method - .union() / .intersection_update() / .symmetric_difference_update()

'''

print("********** Example **********")
names = {"Gal", "Ben", "Ran", "Yam"} # create
print(names)
print(type(names)) # <class 'set'>
print(len(names)) # 4

x = "Gal" in names # search
print(x)

names.add("Ram") # add
print(names)

names.remove("Ran") # remove
print(names)

for i in names: # loop
    print(i)