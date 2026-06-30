import pygame
from pygame.locals import *
import constantes

#molde do objeto 
class Personagem:
    def __init__(self, nome, x, y, largura_coelho, altura_coelho):
        self.cor = (255, 255, 255)
        self.nome = nome
        self.vida = 3
        self.x = x
        self.y = y
        self.largura = largura_coelho
        self.altura = altura_coelho
        self.rect = pygame.Rect(0, 0, self.largura_coelho, self.altura_coelho) #Entorno do coelho 
        self.rect.center = (self.x, self.y) #Centralizando
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
            self.cor = (0, 0, 0)#Coelho morre(muda de skin)

    def ganha_vida(self): #Coleta uma poção da cura
        if self.rect.colliderect(cura.rect):
            self.muda_cor()

    def perde_vida(self): #Coleta uma cenoura envenenada
        if self.rect.colliderect(veneno.rect):
            self.muda_cor()
        if self.vida == 0:
             

    def mover(self):
        if pygame.key.get_pressed()[K_a]: #Se o jogador clicar na tecla "A"
         self.x = self.x - 10 #10 pixels para esquerda
        if pygame.key.get_pressed()[K_d]: #Se o jogador clicar na tecla "D"
            self.x = self.x + 10 #10 pixels para direita
        
        #Para que o personagem não consiga ir além da borda da janela do jogo
        if self.rect.left + x < 0: #Lado esquerdo
            x -= self.rect.left 
        if self.rect.right + x > constantes.largura_tela: #Lado direito
            x = constantes.largura_tela - self.rect.right 


    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura_coelho, self.altura_coelho)) #enquanto não temos a imagem do coelho, usaremos um retângulo 

    @property #permite chamar essa função sem os ()
    def rect(self):
        return pygame.Rect(self.x, self.y, self.largura_coelho, self.altura_coelho)
personagem = Personagem('coelho', constantes.x, constantes.y , 30, 50)