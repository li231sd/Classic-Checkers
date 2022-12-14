import pygame

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
BACKGROUND = (255, 0, 0)
RED = (255, 100, 100)
WHITE = (255, 255, 255)
BLACK = (24, 24, 24)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
