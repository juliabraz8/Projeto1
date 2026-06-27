import constantes
import pygame
import random

tipos_colets = ['Cura', 'Foguete', 'Veneno']
lista_colets = []

class Coletáveis:
    def __init__(self, tupla_coord): #tupla_coord tem as coordenadas iniciais do coletável
        self.x = tupla_coord[0]
        self.y = tupla_coord[1]
        self.largura = constantes.largura_colet
        self.altura = constantes.altura_colet

    def aplicar_efeito(self, personagem):
        pass #função vazia -> existe uma dessa em cada subclasse

    def descer(self, vel_scroll):
        self.y += vel_scroll

    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura)) #por enquanto, desenhar só um retângulo 

    @property #permite chamar essa função sem os ()
    def rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
    
class Cura(Coletáveis):
    def __init__(self, tupla_coord):
        super().__init__(tupla_coord)
        self.cor = (255, 255, 255) #definir cor pra cada subclasse -> temporário enqt nn tem imagem
        self.tipo = "Cura"

    def aplicar_efeito(self, personagem):
        if personagem.vida < constantes.max_vida:
            personagem.vida += 1

class Foguete(Coletáveis):
    def __init__(self, tupla_coord):
        super().__init__(tupla_coord)
        self.cor = (0, 0, 255)
        self.tipo = "Foguete"

    def aplicar_efeito(self, personagem):
        personagem.vel = constantes.subida_foguete

class Veneno(Coletáveis):
    def __init__(self, tupla_coord):
        super().__init__(tupla_coord)
        self.cor = (0, 255, 0)
        self.tipo = "Veneno"

    def aplicar_efeito(self, personagem):
        personagem.vida -= 1

def gerar_colet():
    qtde = random.randint(1, 2)
    for i in range(qtde):
        coord_x = random.randint(0, constantes.largura_tela)
        coord_y = random.randint(0, constantes.altura_tela//2)
        tupla_coord = (coord_x, coord_y)
        tipo = random.choice(tipos_colets)
        if tipo == "Cura":
            colet = Cura(tupla_coord)
        elif tipo == "Veneno":
            colet = Veneno(tupla_coord)
        elif tipo == "Foguete":
            colet = Foguete(tupla_coord)
        lista_colets.append(colet)