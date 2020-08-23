import pygame, random, sys

colors = {'white' : (220, 220, 220), 'black' : (0, 0, 0), 'green' : (0, 255, 0), 'red' : (255, 0, 0)}
GAME_STATE = {
    'mainScreen' : 0, 
    'gamePlay' : 1, 
    'gameOver' : 2
}

def make_board():
    return [[0]*3 for _ in range(3)]

main_board = make_board()

# PYGAME CONFIG
WIN_DIM = 500
pygame.init()
window = pygame.display.set_mode((WIN_DIM,WIN_DIM))
window.fill(colors['white'])
pygame.display.flip()

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 30)
BIG_FONT = pygame.font.SysFont("Arial", 90)


def main_screen():
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


def game_screen():
    # draw a 3x3 grid of 300 x 300 pixels
    # got 200 pixels left on either side, start from 100, 100
    window.fill(colors['white'])
    pygame.display.flip()

    for i in range(1, 5):
        pygame.draw.line(window, colors['black'], ( 100, i * 100 ), ( 400, i * 100 ))

        for j in range(1, 5):
            pygame.draw.line(window, colors['black'], ( j* 100, 100 ), ( j * 100, 400 ))

    pygame.display.update()



# MAIN LOOP
run = True
gameState = 'mainScreen'
clock = pygame.time.Clock()
chosenSymbol = ''

def changeGameState(state):
    if state == 'gameScreen':
        game_screen()


main_screen()

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

    if callFunc:
        changeGameState(gameState)
    
    callFunc = False



