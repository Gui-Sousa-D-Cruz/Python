import pygame
from pygame.locals import *
from sys import exit

pygame.init()

x = 564
y = 730

tela = pygame.display.set_mode((x, y))
pygame.display.set_caption('Game')



bg = pygame.image.load('mapa1.jpg').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

char = pygame.image.load('mage.png').convert_alpha()
char = pygame.transform.scale(char, (32, 32))

char_posx = 3
char_posy = y - 28


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
    tela.blit(bg, (0, 0))
    tela.blit(char, (char_posx, char_posy))    
    pygame.display.update()