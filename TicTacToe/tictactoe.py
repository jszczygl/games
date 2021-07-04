X= "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Display game instructions"""
    print(
    """
    You will make you move known by entering a number 0-8. The number 
    will correspond to the board position as illustrated:
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
    """
    )

def ask_yes_no(question):
    """Ask and yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    """Determine if the computer or human goes first"""
    go_first = ask_yes_no("Do you wan to start? (y/n):")
    if go_first == "y":
        print("Human go first, you piece is X")
        human = X
        computer = O
    else:
        print("Computer goes first, your piece is O")
        computer = X
        human = O
    return computer, human

def new_board():
    """Create new board"""
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Displaying board on the screen"""
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def legal_moves(board):
    """Creates a list of legal moves"""
    moves = []
    for i in range(NUM_SQUARES):
        if board[i] == EMPTY:
            moves.append(i)
    return moves

def winner(board):
    """Determines who win"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None

def human_move(board):
    """Get human move"""
    move = None
    legal = legal_moves(board)
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8)", 0, NUM_SQUARES)
        if move not in legal:
            print("pick up empty field on the board")
    return move

def computer_move(board, computer, human):
    """Make computer move"""
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    # if computer can win, make that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this
        board[move] = EMPTY

    # if human can win, block that move
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checking this
        board[move] = EMPTY

    # no one can win so take the best move
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def congrat_winner(the_winner):
    if the_winner != TIE:
        print(f"{the_winner} won!")
    else:
        print("It's a TIE")

def next_turn(turn):
    """Switch turns"""
    if turn == X:
        return O
    else:
        return X

def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner)

main()
input("\n\nPress the enter key to quit.")


