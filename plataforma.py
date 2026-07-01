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
        self.cor = (128, 128, 128)
    
    def pular(self, personagem):
        personagem.rect.bottom = self.rect.top #Coelho está no topo da plataforma
        personagem.vel_y = personagem.forca_pulo
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))
    
    def descer(self, vel_scroll):
        self.y += vel_scroll
    
    @property #permite chamar essa função sem os ()
    def rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

def gerar_plats_iniciais():
    for i in range(1, 7):
        inicial_x = random.randint(0, constantes.largura_tela - 100)
        inicial_y = 650 - (i * 70)
        plataformas.append(Plataformas(inicial_x, inicial_y))

def gerar_plats_gerais(personagem):
    # while len(plataformas) < 6:
    while plataformas[-1].y > (personagem.y - constantes.altura_tela):
        ultimo_y = plataformas[-1].y
        plataformas_y = ultimo_y - random.randint(90, 140)
        plataformas_x = random.randint(0, constantes.largura_tela - 100)
        plataformas.append(Plataformas(plataformas_x, plataformas_y))