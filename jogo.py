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

play = False
while not play:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = True 

while True:
    relogio.tick(60)
    tela.fill((255, 255, 255))
    for event in pygame.event.get:
        if event.type == QUIT:
            pygame.quit()
            exit() 
    
    pygame.draw.rect(tela, (0,255,0), (x,y,40,50))
    pygame.display.update()