from constants import PLAYERS_AND_SYMBOLS
from constants import find_empty, checkWinner

# considering AI to always be the maximizing player
def setVars():
    global scores, maxPlayer, minPlayer

    if PLAYERS_AND_SYMBOLS[1] == 'O': # ie, X is AI
        scores = {
            'X' : 10,
            'O' : -10,
            'Draw' : 0
        }

        maxPlayer = 'X'
        minPlayer = 'O'

    else: # ie, O is AI
        scores = {
            'X' : -10,
            'O' : 10,
            'Draw' : 0
        }

        maxPlayer = 'O'
        minPlayer = 'X'


def minimax(board, depth, maximizingPlayer):
    setVars()
    result = checkWinner(board)

    # print(f'x = {x}, y = {y}, result = {result}, depth = {depth}, maximizingPlayer = {maximizingPlayer}')
        
    if result is not None:
        return scores[result]

    if maximizingPlayer: # ie, AI is playing
        bestScore = -1000

        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
        
                    board[row][col] = maxPlayer

                    score = minimax(board, depth + 1, False)

                    board[row][col] = 0

                    bestScore = max(score, bestScore)
                    # print(f'maximizingPlayerScore = {bestScore}')
        return bestScore

    else:
        bestScore = 1000

        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    
                    board[row][col] = minPlayer

                    score = minimax(board, depth + 1, True)

                    board[row][col] = 0

                    bestScore = min(bestScore, score)
                    # print(f'minimizingPlayerScore = {bestScore}')

        return bestScore


    


