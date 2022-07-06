#battleship program

from random import randint

battleship_board = []

for i in range(0,5):
    battleship_board.append(["O"]*5)

def print_battle_ship_board(battleship_board):
    for i in battleship_board:
        print((" ").join(i))

print_battle_ship_board(battleship_board)
# Add your code below

def battleship_row(battleship_board):
    return (randint(0, len(battleship_board)-1))

def battleship_column(battleship_column):
    return (randint(0, len(battleship_board)-1))

ship_row = battleship_row(battleship_board)
ship_col = battleship_column(battleship_board)
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess row :"))
    guess_col = int(input("Guess column :"))

    print(ship_row)
    print(ship_col)

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations you have successfully sunk the battleship")
        break
    else:
        if guess_row > 5 or guess_col > 5:
            print("It is not even in the ocean")
        elif battleship_board[guess_row][guess_col] == "X":
            print("You guessed that already")
        else:
            print("You missed my battleship")
            battleship_board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game over")
        print_battle_ship_board(battleship_board)
