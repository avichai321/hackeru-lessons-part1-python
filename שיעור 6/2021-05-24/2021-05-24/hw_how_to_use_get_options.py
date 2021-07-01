
def add():
    print('add')

def login():
    print('login')

def info():
    pass

def play():
    op = input('****** Enter Option ****** \n 0 - Stop | 1 - Add | 2 - login \n >>>')
    if op == '0':
        return
    elif op == '1':
        add()
    elif op == '2':
        login()
    elif op == '100':
        info()
    play()

play()




