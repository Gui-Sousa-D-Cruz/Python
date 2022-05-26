import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init() 

largura = 640
altura = 480

x = largura / 2 - 20
y = altura / 2 - 25

x_azul = randint(40, 600)
y_azul = randint(50, 430)

fonte = pygame.font.SysFont('Arial', 40, True, False)
pontos = 0

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Olá mundo!') 
relogio = pygame.time.Clock()

while True: 

    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (253, 58, 208))
    for event in pygame.event.get(): 
        if event.type == QUIT:
            pygame.quit()     
            exit()
        
    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20
            
    ret_ver = pygame.draw.rect(tela, (255,0,0), (x, y, 40, 50)) 
    ret_azu = pygame.draw.rect(tela, (0, 200, 200), (x_azul,y_azul,40,50))

    if ret_ver.colliderect(ret_azu):
       x_azul = randint(40, 600)
       y_azul = randint(50, 430)
       pontos = pontos + 1
 


    tela.blit(texto_formatado, (430, 40))
    pygame.display.update() 