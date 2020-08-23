import pygame, random, sys

from game import main_screen, make_grid, gamePlay
from constants import colors, GAME_STATE, PLAYERS_AND_SYMBOLS, WIN_DIM, FONT, BIG_FONT


# PYGAME CONFIG
pygame.init()
window = pygame.display.set_mode((WIN_DIM,WIN_DIM))
window.fill(colors['white'])
pygame.display.flip()


# MAIN LOOP
run = True
gameState = 'mainScreen'
clock = pygame.time.Clock()
chosenSymbol = ''
turn = 0

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
                        PLAYERS_AND_SYMBOLS[1] = 'O'
                        PLAYERS_AND_SYMBOLS[2] = 'X'
                        callFunc = True
                        print(PLAYERS_AND_SYMBOLS)


                    # for X 270 to 270 + 70
                    if 270 < event.pos[0] < 340 and 200 < event.pos[1] < 270:
                        gameState = 'gameScreen'
                        chosenSymbol = 'X'
                        PLAYERS_AND_SYMBOLS[1] = 'X'
                        PLAYERS_AND_SYMBOLS[2] = 'O'
                        callFunc = True
                        print(PLAYERS_AND_SYMBOLS)

        elif gameState == 'gameScreen':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    willIncrease = gamePlay(window, event, chosenSymbol, turn)
                    print(f'willIncrease = {willIncrease}')
                    
                    if willIncrease is not None:
                        turn  += 1

    if callFunc:
        changeGameState(gameState)
    
    callFunc = False
