#!/home/cassius/anaconda3/bin/python3.4

def startgame():
    global theBoard, x_score, o_score
    theBoard = {'top-L':'   ', 'top-M':'   ', 'top-R':'   ',
        'mid-L':'   ', 'mid-M':'   ', 'mid-R':'   ',
        'low-L':'   ', 'low-M':'   ', 'low-R':'   '}
    x_score = []
    o_score = []
    print("To play, choose a row: top, mid, or low. Then use a dash and choose (L)eft, (R)ight, or (M)iddle. Example: low-R for the lower right square.\n") 
    gameplay()

theBoard = {'top-L':'   ', 'top-M':'   ', 'top-R':'   ',
        'mid-L':'   ', 'mid-M':'   ', 'mid-R':'   ',
        'low-L':'   ', 'low-M':'   ', 'low-R':'   '}
score_dict = {'top-L':1, 'top-M':2, 'top-R':3,
        'mid-L':4, 'mid-M':5, 'mid-R':6,
        'low-L':7, 'low-M':8, 'low-R':9}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('---+---+---')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('---+---+---')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
print('')
 
def o_wins():
    print()
    printBoard(theBoard)
    print()
    print('Player O Wins!')
    print()
    choice = input('Play Again? (y/n): ')
    choice = choice.lower()
    if choice == 'y':
        print()
        startgame()
    else:
        print('See ya!')
        print()
        exit()
 
def x_wins():
    print()
    printBoard(theBoard)
    print()
    print('Player X Wins!')
    print()
    choice = input('Play Again? (y/n): ')
    choice = choice.lower()
    if choice == 'y':
        print()
        startgame()
    else:
        print('See ya!')
        print()
        exit()

x_score = []
o_score = []


def gameplay():
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print('')
        move = input('Turn for ' + turn + '. Move on which space?: ')
        print()
        turn_value = str(' '+ turn +' ')
        theBoard[move] = turn_value
        if turn == 'X':
            turn = 'O'
            x_score.append(score_dict.get(move))
            if 1 in x_score and 2 in x_score and 3 in x_score:
                x_wins()
            else:
                pass
            if 4 in x_score and 5 in x_score and 6 in x_score:
                x_wins()
            else:
                pass
            if 7 in x_score and 8 in x_score and 9 in x_score:
                x_wins()
            else:
                pass
            if 1 in x_score and 4 in x_score and 7 in x_score:
                x_wins()
            else:
                pass
            if 2 in x_score and 5 in x_score and 8 in x_score:
                x_wins()
            else:
                pass
            if 3 in x_score and 6 in x_score and 9 in x_score:
                x_wins()
            else:
                pass
            if 1 in x_score and 5 in x_score and 9 in x_score:
                x_wins()
            else:
                pass
            if 7 in x_score and 5 in x_score and 3 in x_score:
                x_wins()
            else:
                pass
        else:
            turn = 'X'
            o_score.append(score_dict.get(move))
            if 1 in o_score and 2 in o_score and 3 in o_score:
                o_wins()
            else:
                pass
            if 4 in o_score and 5 in o_score and 6 in o_score:
                o_wins()
            else:
                pass
            if 7 in o_score and 8 in o_score and 9 in o_score:
                o_wins()
            else:
                pass
            if 1 in o_score and 4 in o_score and 7 in o_score:
                o_wins()
            else:
                pass
            if 2 in o_score and 5 in o_score and 8 in o_score:
                o_wins()
            else:
                pass
            if 3 in o_score and 6 in o_score and 9 in o_score:
                o_wins()
            else:
                pass
            if 1 in o_score and 5 in o_score and 9 in o_score:
                o_wins()
            else:
                pass
            if 7 in o_score and 5 in o_score and 3 in o_score:
                o_wins()
            else:
                pass
startgame()
