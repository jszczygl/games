# Python3 program to find the next optimal move for a computer
computer = 'X'
human = 'O'
NUM_SQUARES = 9

# This function returns true if there are moves
# remcomputerning on the board. It returns false if
# there are no moves left to play.
def is_moves_left(board):
    for i in range(NUM_SQUARES):
        if board[i] == '_':
            return True
    return False

def evaluate(board):
    # Checking for Rows for X or O victory.
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
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

    print("The value of the best Move is :", best_val)

    print()
    return best_move


# Driver code
board = [
    'X', '_', '_',
    '_', '_', '_',
    '_', '_', 'O'
]

computer_move = find_best_move(board)
print(f"The Optimal Move is : {computer_move}")

