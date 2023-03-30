import pygame
from time import sleep

def music():
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('exerciciospython/ex046.mp3')
    pygame.mixer.music.play(loops=0, start=0.0)
    pygame.event.wait()
print('-='*10)
print('CONTAGEM REGRESSIVA')
print('-='*10)
for c in range(10,-1,-1):
    sleep(1)
    print(c)
    
print('FELIZ ANO NOVO!!!')
music()


