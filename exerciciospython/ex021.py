
import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

#Carregando a música
pygame.mixer.music.load('exerciciospython/ex021a.mp3')

#Configurando como a música vai ser executada
pygame.mixer.music.play(loops=0, start=56.0)

#Espera a música acabar pra fechar o programa
pygame.event.wait()


