board = [" " for _ in range(9)]

def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def player_input(player):
    while True:
        try:
            position = int(input(f"Player {player}, enter your position (1-9): ")) - 1
            if 0 <= position <= 8 and board[position] == " ":
                return position
            else:
                print("Invalid position. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def check_win():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False

def play():
    current_player = "X"
    for _ in range(9):
        display_board()
        position = player_input(current_player)
        board[position] = current_player

        if check_win():
            display_board()
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    display_board()
    print("It's a tie!")

play()