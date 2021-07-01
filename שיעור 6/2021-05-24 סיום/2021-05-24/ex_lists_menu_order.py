print('into ex_lists_menu_order.py')

menu = ['Pizza', 'Sushi', 'Burger', 'Salad', 'ice cream']
orders = ['Pizza','ice cream','Pizza','Burger', 'ice cream', 'Pizza','Burger', 'Salad', 'ice cream']


def print_menu():
    num = 1
    for item in menu:
        print(str(num) + " - " + item)
        num += 1

def add_order():
    print_menu()
    num_item_menu = int(input("What do you like to order"))
    item = menu[num_item_menu-1]
    orders.append(item)

def remove_order():
    if len(orders) == 0 :
        return False
    else:
        orders.pop(0)
        return True



def status_orders():
    pass

def print_menu_orders():
    for item in menu:
        num = orders.count(item)
        print( str(num) + " - " + item)

def time_order():
    total_time = 0
    for item in menu:
        x = orders.count(item)
        if x <= 2:
            total_time += (x * 10)
        elif x <= 4:
            total_time += (x * 7)
        if x > 4:
            total_time += (x * 5)
    print('total: ', total_time)

def info():
   print(menu)
   print(orders)


def play():
    op = input('****** Enter Option ****** \n'
               '0 - Stop | '
               '1 - print_menu | '
               '2 - add_order | '
               '3 - remove_order | '
               '4 - status_orders | '
               '5 - print_menu_orders | '
               '6 - time_order | '
               '100 - Info | '
               '\n >>>')
    if op == '0':
        return
    elif op == '1':
        print_menu()
    elif op == '2':
        add_order()
    elif op == '3':
        remove_order()
    elif op == '4':
        status_orders()
    elif op == '5':
        print_menu_orders()
    elif op == '6':
        time_order()
    elif op == '100':
        info()
    play()

play()

