from random import randint

## Create Board ##
board = []
for x in range(0, 9):
  board.append(["O"] * 9)
def print_board(board):
  for row in board:
    print " ".join(row)
print_board(board)
## End Board Creation ##

## Ship Placement ##
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) - 1)

ships = {'battleship' : [], 'cruiser' : []}
def ship_placement(ships):
    for ship in ships:
        ships[ship].insert(0, random_col(board))
    return len(ships)
## End Ship Placement ##

def turns(turn):
    ship_placement(ships)
    ships_exist = ship_placement(ships)
    print ships_exist
    print ships['battleship']
    print ships['cruiser']
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
print turns(3)
