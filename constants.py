import pygame

colors = {'white' : (220, 220, 220), 'black' : (0, 0, 0), 'green' : (0, 255, 0), 'red' : (255, 0, 0)}

GAME_STATE = {
    'mainScreen' : 0, 
    'gamePlay' : 1, 
    'gameOver' : 2
}

PLAYERS_AND_SYMBOLS = {1 : None, 2 : None}

WIN_DIM = 500

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 30)
BIG_FONT = pygame.font.SysFont("Arial", 90)

def find_empty(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                count += 1

    return count

def equals3(a, b, c): 
  return a == b and b == c and a != 0


def checkWinner(board): 
    winner = None

    # horizontal
    for i in range(3): 
        if (equals3(board[i][0], board[i][1], board[i][2])) :
            winner = board[i][0]
        
    

    # Vertical
    for i in range(3):
        if (equals3(board[0][i], board[1][i], board[2][i])) :
            winner = board[0][i]
        
    

    # Diagonal
    if (equals3(board[0][0], board[1][1], board[2][2])) :
        winner = board[0][0]
    
    if (equals3(board[2][0], board[1][1], board[0][2])) :
        winner = board[2][0]
    

    openSpots = find_empty(board)

    if (winner == None and openSpots == 0) :
        return 'Draw'

    else :
        return winner
  
  