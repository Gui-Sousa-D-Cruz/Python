import pygame
from pygame.locals import *
from sys import exit

#Inicia o pygame
pygame.init() 
largura = 640
altura = 480
#define a tela do pygame
tela = pygame.display.set_mode((largura, altura))
#define o nome da tela
pygame.display.set_caption('Olá mundo!') 

x = largura / 2 - 20
y = largura / 2 - 25


while True: #loop principal do jogo
    
    for event in pygame.event.get(): #loop para checar se algum evento ocorreu
        if event.type == QUIT:
            pygame.quit()     #evento para sair do jogo
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_s:
                y = y + 20
            if event.key == K_w:
                y = y - 20
                   #onde   cor(r,g,b)  (x,y,larg,altura)
    pygame.draw.rect(tela, (255,0,0), (200,300,40,50)) #desenha um retangulo
                    #onde     cor(r,g,b)   (x,y)   (raio)
    pygame.draw.circle(tela, (0,120,120), (200, 230) , 40)

                 #onde   cor(r,g,b)  1(x,y)  2(x,y) (espessura)
    pygame.draw.line(tela, (120,120,0), (320,0), (320,600), 5)

    
    pygame.display.update() #A cada intereção no loop principal ela atualiza a tela do jogo