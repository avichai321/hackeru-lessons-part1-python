from time import sleep

dic_bored = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}

def pr_bored(dic_bored):
    print("The bored now:")
    print(dic_bored["7"] + '|' + dic_bored["8"] + '|' + dic_bored["9"])
    print('-+-+-')
    print(dic_bored["4"] + '|' + dic_bored["5"] + '|' + dic_bored["6"])
    print('-+-+-')
    print(dic_bored["1"] + '|' + dic_bored["2"] + '|' + dic_bored["3"])

def pr_bored_number():
    print("The place enter a move:")
    print(str(7) + '|' + str(8) + '|' + str(9))
    print('-+-+-')
    print(str(4) + '|' + str(5) + '|' + str(6))
    print('-+-+-')
    print(str(1) + '|' + str(2) + '|' + str(3))
sum_points = 0
def game(player1 ,player2):
    global sum_points
    count = 0
    play = player1
    turn = "x"
    for i in range(10):
        pr_bored(dic_bored)
        pr_bored_number()
        print("its your turn: " + play + " " + "role: " + turn + " enter your move: ")
        move = int(input())
        if dic_bored[str(move)] == " ":
            dic_bored[str(move)] = turn
            count += 1
            print(count)
        else:
            print("This cube already filled\nchoose other cube!")
            sleep(1.5)
            continue

        if count >= 5:
            #row
            if (dic_bored["1"] == dic_bored["2"] == dic_bored["3"] != " ") or (dic_bored["4"] == dic_bored["5"] == dic_bored["6"] != " ") or (dic_bored["7"] == dic_bored["8"] == dic_bored["9"] != " "):
                pr_bored(dic_bored)
                print("End of the game.")
                print(turn + " has won.")
                sum_points += 10
                break
            #column
            elif (dic_bored["1"] == dic_bored["4"] == dic_bored["7"] != " ") or (dic_bored["2"] == dic_bored["5"] == dic_bored["8"] != " ") or (dic_bored["3"] == dic_bored["6"] == dic_bored["9"] != " "):
                pr_bored(dic_bored)
                print("End of the game.")
                print(play + " has won.")
                sum_points += 10
                break
            #slant
            elif(dic_bored["1"] == dic_bored["5"] == dic_bored["9"] != " ") or (dic_bored["3"] == dic_bored["5"] == dic_bored["7"] != " "):
                pr_bored(dic_bored)
                print("End of the game")
                print(play + " has won.")
                sum_points += 10
                break

        if count == 9:
            pr_bored(dic_bored)
            print("End of the game")
            print(play + " has won.")

        if turn == "x":
            turn = "o"
            play = player2
        else:
            turn = "x"
            play = player1

    print("Congratulation " + play + "the points you've earned: " + str(sum_points) +"  we will update the points in your play center user\n\n")
    return play
