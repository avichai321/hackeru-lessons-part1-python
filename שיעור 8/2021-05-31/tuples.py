print("into tuples.py ")
'''
tuple is ordered and unchangeable collection (allow duplicate values)

create - YES - tuple1 = ("Gal",10)
get    - YES - tuple1[0]
search - YES - .index()
add    - NOT - unchangeable
set    - NOT - unindexed
remove - NOT - unchangeable
join   - NOT - but we can casting the tuple to list
loop   - YES - for i in tuple1:
 
'''


tuple1 = () # create
print(type(tuple1)) # <class 'tuple'>

print("********** Example **********")
colors = ("Red","Green","Blue","Pink","silver","Gold") # create
print(colors)
print(type(colors)) # <class 'tuple'>
print(len(colors)) # 6

x = colors[2] # get
print(x)

x = "Blue" in colors # search
print(x)


for i in colors: # loop
    print(i)