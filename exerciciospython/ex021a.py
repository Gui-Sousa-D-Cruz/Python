'''import random
import playsound

lista = ['ex021a.mp3', 'ex021b.mp3', 'ex021c.mp3' ]
musica = random.choice(lista)
playsound.playsound(musica)'''

import pygame
from pygame.locals import *
import random

pygame.init()
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Olá mundo!') 
musica = pygame.mixer.music.load('exerciciospython\ex021a.mp3')
pygame.mixer.music.play(-1)



