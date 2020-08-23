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