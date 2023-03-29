
import pygame

def music():
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
print('')
print('')
esc = input('Você está pronta? Sim ou não? ')
print('')
print('')
if esc.upper() == 'SIM':
    print('Oi Duda, mesmo eu tendo um jeito meio estranho e estando meio mal, eu te amo muito')
    print('')
    print('')
    esc = input('Você me ama? Sim ou não? ')
    print('')
    print('')
    if esc.upper() == 'SIM':
        print('OBRIGADO POR TUDO!')
        music()
else:
    print('Vai se fuder então!')