
def say_hola():
    name = input('Enter name')
    print('Hola ' + name)

def plus2():
    num = int(input('Enter number'))
    print(num + num)

def info():
    pass

def play():
    op = input('****** Enter Option ****** \n 0 - Stop | 1 - say_hola | 2 - plus2 | 100 - info \n >>>')
    if op == '0':
        return
    elif op == '1':
        say_hola()
    elif op == '2':
        plus2()
    elif op == '100':
        info()
    play()

play()




