import game_oron_math
import game_x_or_o

def play():
    op = input('****** Games Option ****** \n'
               '0   - Stop \n'
               '1   - Game oron math \n'
               '2   - Game X or O \n'
               '100 - info \n'
               '>>>')
    if op == '0':
        return
    elif op == '1':
        game_oron_math.play()
    elif op == '2':
        game_x_or_o.play()
    elif op == '100':
        info()
    play()

play()