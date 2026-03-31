import math

# Create board
board = [" " for _ in range(9)]

# Display board with positions
def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}      1 | 2 | 3")
    print("--+---+--     --+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}      4 | 5 | 6")
    print("--+---+--     --+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}      7 | 8 | 9")
    print()

# Check winner
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Check draw
def is_draw():
    return " " not in board

# Player move using input()
def player_move():
    while True:
        move = input("Enter your move (1-9): ")

        if not move.isdigit():
            print("Please enter a number between 1 and 9.")
            continue

        move = int(move)

        if move < 1 or move > 9:
            print("Number must be between 1 and 9.")
            continue

        if board[move - 1] != " ":
            print("That position is already taken.")
            continue

        board[move - 1] = "X"
        break

# AI move
def ai_move():
    best_score = -math.inf
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

# Main game loop
def main():
    print("Tic Tac Toe (You = X, AI = O)")
    
    while True:
        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("You win!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        print("AI is thinking...\n")
        ai_move()

        if check_winner("O"):
            print_board()
            print("AI wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

# Run game
main()