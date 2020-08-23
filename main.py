import pygame, random, sys

from game import main_screen, make_grid, gamePlay

colors = {'white' : (220, 220, 220), 'black' : (0, 0, 0), 'green' : (0, 255, 0), 'red' : (255, 0, 0)}
GAME_STATE = {
    'mainScreen' : 0, 
    'gamePlay' : 1, 
    'gameOver' : 2
}

# PYGAME CONFIG
WIN_DIM = 500
pygame.init()
window = pygame.display.set_mode((WIN_DIM,WIN_DIM))
window.fill(colors['white'])
pygame.display.flip()

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 30)
BIG_FONT = pygame.font.SysFont("Arial", 90)


# MAIN LOOP
run = True
gameState = 'mainScreen'
clock = pygame.time.Clock()
chosenSymbol = ''
turn = 1

def changeGameState(state):
    if state == 'gameScreen':
        make_grid(window, chosenSymbol)


main_screen(window)

callFunc = False

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if gameState == 'mainScreen':

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # for O 70px wide, 102px tall
                    if 90 < event.pos[0] < 160 and 200 < event.pos[1] < 270:
                        gameState = 'gameScreen'
                        chosenSymbol = 'O'
                        callFunc = True


                    # for X 270 to 270 + 70
                    if 270 < event.pos[0] < 340 and 200 < event.pos[1] < 270:
                        gameState = 'gameScreen'
                        chosenSymbol = 'X'
                        callFunc = True

        elif gameState == 'gameScreen':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    gamePlay(window, event, chosenSymbol, turn)
                    turn += 1

    if callFunc:
        changeGameState(gameState)
    
    callFunc = False



