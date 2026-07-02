import pygame
from pygame.locals import *
import constantes

# molde do objeto
class Personagem:
    def __init__(self, nome, x, y):

        self.nome = nome
        self.vida = 3
        self.x = x
        self.y = y
        self.largura = constantes.largura_coelho
        self.altura = constantes.altura_coelho

        # CARREGAR IMAGENS
        self.sprite_branco = pygame.image.load(
            "sprites/coelho_branco_semfundo.png"
        ).convert_alpha()

        self.sprite_verde_claro = pygame.image.load(
            "sprites/coelho_verde_claro_semfundo.png"
        ).convert_alpha()

        self.sprite_verde_escuro = pygame.image.load(
            "sprites/coelho_verde_escuro_semfundo.png"
        ).convert_alpha()
        
        self.sprite_morto = pygame.image.load(
            "sprites/coelho_verde_escuro_olhosx_semfundo.png"
        ).convert_alpha()


        # Ajustar tamanho das imagens
        self.sprite_branco = pygame.transform.scale(
            self.sprite_branco,
            (self.largura, self.altura)
        )

        self.sprite_verde_claro = pygame.transform.scale(
            self.sprite_verde_claro,
            (self.largura, self.altura)
        )

        self.sprite_verde_escuro = pygame.transform.scale(
            self.sprite_verde_escuro,
            (self.largura, self.altura)
        )

        self.sprite_morto = pygame.transform.scale(
            self.sprite_morto,
            (self.largura, self.altura)
        )


        # Começa branco
        self.sprite_atual = self.sprite_branco

        self.vel_y = 0
        self.gravidade = 0.5
        self.forca_pulo = -12

        self.contagem = {
            "Foguete": 0,
            "Cura": 0,
            "Cenoura Envenenada": 0
        }

    def muda_cor(self):

        if self.vida == 3:
            self.sprite_atual = self.sprite_branco

        elif self.vida == 2:
            self.sprite_atual = self.sprite_verde_claro

        elif self.vida == 1:
            self.sprite_atual = self.sprite_verde_escuro

        else:  # vida = 0
            self.sprite_atual = self.sprite_morto

    def mover(self):

        if pygame.key.get_pressed()[K_a]:
            self.x -= 10

        if pygame.key.get_pressed()[K_d]:
            self.x += 10

        # Limites da tela
        if self.rect.left < 0:
            self.x = 0

        if self.rect.right > constantes.largura_tela:
            self.x = constantes.largura_tela - self.largura

    def desenhar(self, tela):

        tela.blit(self.sprite_atual, (self.x, self.y))

    def aplicar_gravidade(self):

        self.vel_y += self.gravidade

        if self.vel_y > 10:
            self.vel_y = 10

        self.y += self.vel_y

    @property
    def rect(self):

        return pygame.Rect(
            self.x,
            self.y,
            self.largura,
            self.altura
        )