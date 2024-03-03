#tictactoe project

# USER INTERFACE
first_turn = 1
winner_first_player = 0
X = 'X'
O = 'O'

row1 = ['1','2','3']
row2 = ['4','5','6']
row3 = ['7','8','9']

def print_board(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
    pass

# FIRST PLAYER MOVE
def x_placement(first_player):
    if row1[0] != O and first_player == '1':
        row1[0] = X
    elif row1[1] != O and first_player == '2':
        row1[1] = X
    elif row1[2] != O and first_player == '3':
        row1[2] = X
    elif row2[0] != O and first_player == '4':
        row2[0] = X
    elif row2[1] != O and first_player == '5':
        row2[1] = X
    elif row2[2] != O and first_player == '6':
        row2[2] = X
    elif row3[0] != O and first_player == '7':
        row3[0] = X
    elif row3[1] != O and first_player == '8':
        row3[1] = X
    elif row3[2] != O and first_player == '9':
        row3[2] = X
    else:
        print('you lose a turn for being stupid')
        
        
        
        
begin_game = input('Hello! would you like to play a game of tic tac toe? (Y/N) ')

if begin_game == 'Y':
    if first_turn == 1:
        print("lets go!")
        first_turn = 0
    while winner_first_player == 0:
        print_board(row1,row2,row3)
        first_player = input('First Player; Pick a space: ')
        print(first_player)
        x_placement(first_player)
        
elif begin_game == 'N':
    print('k bye')
else:
    print('Try again')

