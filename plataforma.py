import pygame
import random
import constantes

plataformas = []


class Plataformas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.largura = constantes.largura_plat
        self.altura = constantes.altura_plat

        self.sprite = pygame.image.load(
            "sprites/nuvem_pixelizada.png"
        ).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.sprite,
            (self.largura, self.altura)
        )

    def pular(self, personagem):
        personagem.vel_y = personagem.forca_pulo

    def desenhar(self, tela):
        tela.blit(self.sprite, (self.x, self.y))

    def descer(self, vel_scroll):
        self.y += vel_scroll

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)


def gerar_plats_iniciais():
    for i in range(1, 7):
        inicial_x = random.randint(0, constantes.largura_tela - constantes.largura_plat)
        inicial_y = 650 - (i * 70)
        plataformas.append(Plataformas(inicial_x, inicial_y))


def gerar_plats_gerais(personagem):
    while plataformas[-1].y > (personagem.y - constantes.altura_tela):
        ultimo_y = plataformas[-1].y
        plataformas_y = ultimo_y - random.randint(90, 140)
        plataformas_x = random.randint(0, constantes.largura_tela - constantes.largura_plat)
        plataformas.append(Plataformas(plataformas_x, plataformas_y))