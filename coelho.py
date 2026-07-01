import pygame
from pygame.locals import *
import constantes

#molde do objeto 
class Personagem:
    def __init__(self, nome, x, y):
        self.cor = (255, 255, 255)
        self.nome = nome
        self.vida = 3
        self.x = x
        self.y = y
        self.largura = constantes.largura_coelho
        self.altura = constantes.altura_coelho
        # self.rect = pygame.Rect(0, 0, self.largura, self.altura) #Entorno do coelho 
        # self.rect.center = (self.x, self.y) #Centralizando
        self.vel_y = 0 #Velocidade do eixo y
        self.gravidade = 0.5
        self.forca_pulo = -12

    def muda_cor(self):
        if self.vida == 1:
            self.cor = (0, 255, 0)#Coelho muda para cor 3
        elif self.vida == 2:
            self.cor = (150, 255, 150)#Coelho muda para cor 2
        elif self.vida == 3:
            self.cor = (255, 255, 255)#Coelho volta ao normal
        else: #vida = 0
            self.cor = (0, 255, 255)#Coelho morre(muda de skin)
             
    def mover(self):
        if pygame.key.get_pressed()[K_a]: #Se o jogador clicar na tecla "A"
         self.x = self.x - 10 #10 pixels para esquerda
        if pygame.key.get_pressed()[K_d]: #Se o jogador clicar na tecla "D"
            self.x = self.x + 10 #10 pixels para direita
        
        #Para que o personagem não consiga ir além da borda da janela do jogo
        if self.rect.left < 0: #Lado esquerdo
            self.x = 0
        if self.rect.right > constantes.largura_tela: #Lado direito
            self.x = constantes.largura_tela - self.largura


    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura)) #enquanto não temos a imagem do coelho, usaremos um retângulo 

    def aplicar_gravidade(self):
        self.vel_y += self.gravidade
        if self.vel_y > 10:
            self.vel_y = 10
        self.y += self.vel_y

    @property #permite chamar essa função sem os ()
    def rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)