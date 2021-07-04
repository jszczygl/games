X = "X"
O = "O"
EMPTY = "_"
TIE = "TIE"
NUM_SQUARES = 9
computer = 'X'
human = 'O'
WAYS_TO_WIN = ((0, 1, 2),
                (3, 4, 5),
                (6, 7, 8),
                (0, 3, 6),
                (1, 4, 7),
                (2, 5, 8),
                (0, 4, 8),
                (2, 4, 6))

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
        print("Human go first, you piece is O")
        return human
    else:
        print("Computer goes first, your piece is O")
        return computer

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


def is_moves_left(board):
    for i in range(NUM_SQUARES):
        if board[i] == '_':
            return True
    return False

def evaluate(board):
    # Checking for Rows for X or O victory.
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] and board[row[1]] == board[row[2]]:
            if board[row[0]] == computer:
                return 10
            elif board[row[0]] == human:
                return -10
    return 0


# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax):
    score = evaluate(board)

    # If Maximizer has won the game return his/her
    # evaluated score
    if score == 10:
        return score

    # If Minimizer has won the game return his/her
    # evaluated score
    if score == -10:
        return score

    # If there are no more moves and no winner then
    # it is a tie
    if is_moves_left(board) == False:
        return 0

    # If this maximizer's move
    if isMax:
        best = -1000

        # Traverse all cells
        for i in range(NUM_SQUARES):
            # Check if cell is empty
            if board[i] == '_':
                # Make the move
                board[i] = computer

                # Call minimax recursively and choose
                # the maximum value
                best = max(best, minimax(board, depth + 1, not isMax))

                # Undo the move
                board[i] = '_'
        return best

    # If this minimizer's move
    else:
        best = 1000

        # Traverse all cells
        for i in range(NUM_SQUARES):

            # Check if cell is empty
            if board[i] == '_':
                # Make the move
                board[i] = human

                # Call minimax recursively and choose
                # the minimum value
                best = min(best, minimax(board, depth + 1, not isMax))

                # Undo the move
                board[i] = '_'
        return best


# This will return the best possible move for the computer
def find_best_move(board):
    best_val = -1000
    best_move = -1

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(NUM_SQUARES):
        # Check if cell is empty
        if board[i] == '_':

            # Make the move
            board[i] = computer

            # compute evaluation function for this
            # move.
            move_val = minimax(board, 0, False)

            # Undo the move
            board[i] = '_'

            # If the value of the current move is
            # more than the best value, then update
            # best
            if move_val > best_val:
                best_move = i
                best_val = move_val

    print("The value of the best AI Move is :", best_move)
    return best_move


def congrat_winner(the_winner):
    if the_winner != TIE:
        print(f"{the_winner} won!")
    else:
        print("It's a TIE")

def next_turn(turn):
    """Switch turns"""
    if turn == computer:
        return human
    else:
        return computer

def main():
    display_instruct()
    turn = pieces()
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = find_best_move(board)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner)

main()
input("\n\nPress the enter key to quit.")


