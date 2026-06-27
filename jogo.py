import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

#Criar o plano de fundo
altura = 720 
largura = 480
tela = pygame.display.set_mode((largura,altura))#Formatação

pygame.display.set_caption('A subida do coelho')#Nome da aba
relogio = pygame.time.Clock()

#Posição do coelho
x = 240 #abscissa 
y = 720 #ordenada 

while True:
    relogio.tick(60)
    for event in pygame.event.get:
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]: 
        x = x + 20
    
    pygame.draw.rect(tela, (0,255,0), (x,y,40,50))
    pygame.display.update()