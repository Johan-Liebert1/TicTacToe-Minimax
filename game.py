import pygame

gameBoard = [[0]*3 for _ in range(3)]

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 30)
BIG_FONT = pygame.font.SysFont("Arial", 90)
WIN_DIM = 500

colors = {'white' : (220, 220, 220), 'black' : (0, 0, 0), 'green' : (0, 255, 0), 'red' : (255, 0, 0)}

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


def make_grid(window):
    # draw a 3x3 grid of 300 x 300 pixels
    # got 200 pixels left on either side, start from 100, 100
    window.fill(colors['white'])
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

                window.blit(text, ( (100 + col * 100) + (100 - text.get_width() ) // 2, downBy ))

    pygame.display.update()


def gamePlay(window, event, playerSymbol):
    if 100 < event.pos[0] < 400 and 100 < event.pos[1] < 400:

        xPos = event.pos[1] // 100 - 1
        yPos = event.pos[0] // 100 - 1

        print(xPos, yPos)

        gameBoard[xPos][yPos] = playerSymbol

        # print(gameBoard)

        placeSymbols(window)



