from random import randint

## Create Board ##
def create_board():
    board = []
    for x in range(0, 9):
        board.append(["O"] * 9)
    return board

def print_board(board):
    for row in board:
        print " ".join(row)
    return board

board = create_board()
print_board(board)
## End Board Creation ##


## Create and Place Ships ##
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ships = {'battleship': [], 'cruiser': []}
def ship_placement(ships):
    for ship in ships:
        ships[ship] = (random_row(board), random_col(board))
    return len(ships)

ship_placement(ships)
## End Ship Placement ##
print ships['cruiser']
def play_game(turn):
    while turn:
        print "Turns left: ", turn - 1
        guess_row = int(raw_input("Guess Row: "))
        guess_col = int(raw_input("Guess Col: "))
        guess = [guess_row, guess_col]
        print guess
        if guess == ships['battleship']:
            ships_exist -= 1
            board[guess_row][guess_col] = "X"
            print "You sunk my battleship!"
            if ships_exist == 0:
                return "Congratulations! You sank all my ships!"
            else:
                print_board(board)
        elif guess == ships['cruiser']:
            ships_exist -= 1
            board[guess_row][guess_col] = "X"
            print "You sunk my cruiser"
            if ships_exist == 0:
                return "Congratulations! You sank all my ships!"
            else:
                print_board(board)
        else:
            if guess_row not in range(9) or \
                guess_col not in range(9):
                print "Oops, that's not even in the ocean."
            elif board[guess_row][guess_col] == "-":
                print( "You guessed that one already." )
                print_board(board)
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "-"
                print_board(board)
        turn -= 1
        if turn == 0:
            return "Game Over"
print play_game(3)
