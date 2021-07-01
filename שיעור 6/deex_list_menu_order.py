menu = ['Pizza', 'Sushi', 'Burger', 'Salad', 'ice cream']
orders = ['Pizza', 'Pizza', 'Burger'] #1
def print_menu():
    count = 1
    for i in menu:
        print(str(count) + "." + i)
        count += 1
#2
def add_():
    index_order = '1'
    while  index_order != '0':
        index_order = input("Enter index of food  or press 0 to end ")
        if int(index_order) > 0:
            if int(index_order) > len(menu):
                print("This food dosent in the menu\n")
            else:
                orders.append(menu[int(index_order) - 1])
    print(orders)
#add_()
def add_2():
    index_order = input("Enter index of food  or press 0 to end ")
    while  index_order != '0':
        if int(index_order) > len(menu):
            print("This food dosent in the menu\n")
        else:
            orders.append(menu[int(index_order) - 1])
        index_order = input("Enter index of food  or press 0 to end ")
    print(orders)
    print("the order succeeded")
add_2()
#3
def remove_order():
    food = input("which food you want to delete from the order ")
    for i in orders:
        if i == food:
            orders.remove(food)

    print(orders)
#remove_order()
#4,5
total = 0
def order_time(count):
    global  total
    if 1 <= count <= 2:
        total += 10 * count

    elif 2 < count <= 4:
        total += 7 * count

    else:
        total += 4 * count

def print_order():
    global total
    total = 0
    for i in menu:
        count = orders.count(i)
        if count > 0:
            order_time(count)
            print(str(count)+' '+i)
    workers = input('Enter how many workers')
    print(' the order will be ready in '+str(total/workers)+' min')

print_order()


