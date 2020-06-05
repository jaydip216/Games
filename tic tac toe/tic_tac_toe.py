from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])
    
def player_input():
    marker=' '
    while marker!='x' and marker!='o':
        marker=input('player 1: choose x or o:')

    '''
    return type : (player 1, player 2)
    '''
                     
    if marker=='x':
        return ('x','o')
    else:
        return ('o','x')

def place_marker(board,marker,position):
    board[position]=marker
    
def win_check(board,mark):
    return ((board[1]==mark and board[2]==mark and board[3]==mark) or (board[4]==mark and board[5]==mark and board[6]==mark) or 
            (board[7]==mark and board[8]==mark and board[9]==mark) or (board[9]==mark and board[6]==mark and board[3]==mark) or
           (board[8]==mark and board[5]==mark and board[2]==mark) or (board[7]==mark and board[4]==mark and board[1]==mark) or 
           (board[1]==mark and board[5]==mark and board[9]==mark) or (board[7]==mark and board[5]==mark and board[3]==mark))
    
import random

def choose():
    
    flip=random.randint(0,1)
    if flip==0:
        return 'player 1'
    else:
        return 'player 2'
    
def check_space(board,position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if check_space(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not  check_space(board,position):
        position=int(input('enter the position :'))
    return position
    
def replay():
    ch=input('want to play again? y or n: ').upper()
    return ch=='Y'

print('welcom in game')

print('position format\n\n1|2|3\n4|5|6\n7|8|9\n\n')

while True:
    
    the_board=[' ']*10
    player1,player2=player_input()
    
    turn=choose()
    print(turn + ' will go first')
    
    play_game=input('ready to play y or n: ')
    if play_game=='y':
        gameon=True
    else:
        gameon=False
    
    while gameon:
        if turn == 'player 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player1,position)
            
            if win_check(the_board,player1):
                display_board(the_board)
                print('player 1 has won...')
                gameon=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game...')
                    gameon=False
                else:
                    turn='player 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board,player2,position)
            
            if win_check(the_board,player2):
                display_board(the_board)
                print('player 2 has won...')
                gameon=False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game...')
                    gameon=False
                else:
                    turn='player 1'
     
    if not replay():
        break
