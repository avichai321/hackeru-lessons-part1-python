menu = ['Pizza', 'Sushi', 'Burger', 'Salad', 'ice cream']
orders = []

def get_options():
    choise = input("\nwellcome to our restaurant!\n200 - print orders\n300 - stop process\n========\n1.print menu|2.Add order|3.remove order|4.order status|5.waiting time for the order\n")
    if choise == "200":
        print_orders()
    elif choise == "300":
        return print("bye bye")
    elif choise == "1":
        print_menu()
    elif choise == "2":
        add_order()
    elif choise == "3":
        remove_order()
    elif choise == "4":
        order_status()
    elif choise == "5":
        time_order()
    else:
        print("Enter only one of the following numbers")
    get_options()

def print_menu():
    for u in range(len(menu)):
        print(str(u+1) + " - " + str(menu[u]))
    back = int(input("========\nAre want to do another thing?\npress 1 to continue \n0 to get back to the main menu"))
    if back == 0:
        get_options()
    elif back == 1:
        print_menu()


def print_orders():
    print(orders)
    back = int(input("========\nAre want to do another thing?\npress 1 to continue \n0 to get back to the main menu"))
    if back == 0:
        get_options()
    elif back == 1:
        print_orders()

def add_order():
    print_menu()
    n_num = int(input("Enter your the number of item you want to order"))
    if n_num > len(menu):
        print("the item is not in the menu")
    else:
        item = menu[n_num - 1]
        orders.append(item)
        print("your order has add successfully")
    back = int(input("========\nAre want to do another thing?\npress 1 to continue \n0 to get back to the main menu"))
    if back == 0:
        get_options()
    elif back == 1:
        add_order()


def remove_order():
    if len(orders) == 0:
        print("there are no orders in prepare")
    else:
        for item in range(len(orders)):
            print(str(item + 1) + " - " + str(orders[item]))
        clear = int(input("Enter the number of order you want to cancel :"))
        orders.pop(clear - 1)
        print("the first order has removed")
    back = int(input("========\nAre want to do another thing?\npress 1 to continue \n0 to get back to the main menu"))
    if back == 0:
        get_options()
    elif back == 1:
        remove_order()

def order_status():
    sum_num=0
    for item in menu:
        num = orders.count(item)
        print(str(num) + " - " + item)
        sum_num += num
    print("summery of the orders need to be done is: " + str(sum_num))
    back = int(input("========\nAre want to do another thing?\npress 1 to continue \n0 to get back to the main menu"))
    if back == 0:
        get_options()
    elif back == 1:
        remove_order()


def time_order():
    total_count = 0
    for item in menu:
        cont = orders.count(item)
        if cont <= 2 and cont >= 1:
            total_count += (10 * cont)
        elif cont >= 2 and cont <=4:
            total_count += (7 * cont)
        elif cont >= 4:
            total_count += (5 * cont)
    print("All orders wil be ready in " + str(total_count) + " minutes")
    employ= int(input("enter the amount of employs there are ready to work: "))
    print("each order wiil be ready in " + str(total_count/employ) + " minutes")
    back = int(input("Are want to do another thing?\npress 1 to continue \n0 to get back to the main menu"))
    if back == 0:
        get_options()
    elif back == 1:
        time_order()


get_options()
