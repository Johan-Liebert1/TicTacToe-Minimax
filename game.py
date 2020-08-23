import pygame, random
from termcolor import colored
from constants import colors, GAME_STATE, PLAYERS_AND_SYMBOLS, FONT, BIG_FONT, WIN_DIM


gameBoard = [[0]*3 for _ in range(3)]
ox = ['O', 'X']

def main_screen(window):
    text = FONT.render("Choose your Symbol", 1, colors['black'])
    textWidth = text.get_width()
    window.blit(text, ( (WIN_DIM - textWidth) // 2, 0) )

    pygame.draw.rect(window, colors['black'], (0, 200, WIN_DIM, 100))

    zero = BIG_FONT.render("O", 1, colors['green'])
    cross = BIG_FONT.render("X", 1, colors['red'])

    # print(f'zero = {zero.get_width(), zero.get_height()}')

    window.blit(zero, ( ( 90, 200 )) )
    window.blit(cross, ( ( 270, 200 ) ))

    pygame.display.update()


def make_grid(window, chosenSymbol):
    window.fill(colors['white'])

    p1 = chosenSymbol
    p2 = 'X' if p1 == 'O' else 'O'

    p1Text = FONT.render(f"Player 1 : {p1}", 1, colors['green'] if p1 == 'O' else colors['red'])
    p2Text = FONT.render(f"Player 2 : {p2}", 1, colors['green'] if p2 == 'O' else colors['red'])

    totalWidth = p1Text.get_width() + p2Text.get_width()

    window.blit(p1Text, ( (WIN_DIM - totalWidth) // 2 , 0))
    window.blit(p2Text, ( p1Text.get_width() + (WIN_DIM - totalWidth) // 2 + 10, 0 ))

    # draw a 3x3 grid of 300 x 300 pixels
    # got 200 pixels left on either side, start from 100, 100
    pygame.display.flip()

    for i in range(0, 4):
        pygame.draw.line(window, colors['black'], ( 100, (i + 1) * 100 ), ( 400, (i + 1) * 100 ))

        for j in range(0, 4):
            pygame.draw.line(window, colors['black'], ( (j + 1) * 100, 100 ), ( (j + 1) * 100, 400 ))

    pygame.display.update()


def placeSymbols(window):
    downBy = 100

    for row in range(len(gameBoard)):
        downBy = 100 * row + 100 
        for col in range(len(gameBoard)):

            if gameBoard[row][col] != 0:

                sym = gameBoard[row][col]
                color = colors['green'] if sym == 'O' else colors['red']

                text = BIG_FONT.render(sym, 1, color)

                window.blit(
                    text, 
                    ( 
                        (100 + col * 100) + (100 - text.get_width() ) // 2, downBy 
                    )
                )

    pygame.display.update()


def show_end_screen(window, winner):

    window.fill(colors['white'])

    t = f'{winner} wins'
    text = FONT.render(t, 1, colors['green'] if winner == 'O' else colors['red'])

    window.blit(text, 
        (( WIN_DIM - text.get_width() )//2, 10)
        )
    
    pygame.display.update()


def isGameOver(symbol, row, column):
    strikeRow = strikeCol = strikeMajorDiag = strikeMinorDiag = True

    for col in range(len(gameBoard)):
        if gameBoard[row][col] != symbol:
            strikeRow = False

    for row in range(len(gameBoard)):
        if gameBoard[row][column] != symbol:
            strikeCol = False

    # major diagonal
    i = j = 0
    while 0 <= i < len(gameBoard) and 0 <= j < len(gameBoard):
        if gameBoard[i][j] != symbol:
            strikeMajorDiag = False
        i += 1
        j += 1

    i = 0
    j = len(gameBoard) - 1
    while 0 <= i < len(gameBoard) and 0 <= j < len(gameBoard):
        if gameBoard[i][j] != symbol:
            strikeMinorDiag = False
        i += 1
        j -= 1

    return strikeRow or strikeCol or strikeMajorDiag or strikeMinorDiag


def getRandomNumbers():
    return random.randrange(3), random.randrange(3)


def gamePlay(window, event, playerSymbol, turn):
    # O always goes first, fix that
    symbol = PLAYERS_AND_SYMBOLS[(turn % 2) + 1]

    if (turn % 2) + 1 == 1:
        
        if 100 < event.pos[0] < 400 and 100 < event.pos[1] < 400:

            xPos = event.pos[1] // 100 - 1
            yPos = event.pos[0] // 100 - 1

            if gameBoard[xPos][yPos] != 0:
                return None

            gameBoard[xPos][yPos] = symbol

    else:
        xPos, yPos = getRandomNumbers()

        while gameBoard[xPos][yPos] != 0:
            xPos, yPos = getRandomNumbers()

        gameBoard[xPos][yPos] = symbol


    if isGameOver(symbol, xPos, yPos):
        show_end_screen(window, symbol)
        print(f"{symbol} wins")

    placeSymbols(window)

    return True


def print_board():
    string = ''
    for i in range(3):
        string += '\n'
        for j in range(3):
            x = gameBoard[i][j]
            if x == 0:
                string += str(x) + "  "

            if x == 'O':
                string += colored(x, 'green') + '  '

            if x == 'X':
                string += colored(x, 'red') + '  '

    print(string + "\n\n")
