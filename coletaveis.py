import constantes
import pygame
import random


tipos_colets = ['Cura', 'Foguete', 'Cenoura Envenenada']
lista_colets = []


class Coletáveis:
    def __init__(self, tupla_coord):
        self.x = tupla_coord[0]
        self.y = tupla_coord[1]
        self.largura = constantes.largura_colet
        self.altura = constantes.altura_colet
        self.sprite = None

    def aplicar_efeito(self, personagem):
        pass

    def descer(self, vel_scroll):
        self.y += vel_scroll

    def desenhar(self, tela):
        tela.blit(self.sprite, (self.x, self.y))

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)


class Cura(Coletáveis):
    def __init__(self, tupla_coord):
        super().__init__(tupla_coord)
        self.tipo = "Cura"

        self.sprite = pygame.image.load(
            "sprites/cenoura_pixelizada_semfundo.png"
        ).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.sprite,
            (self.largura, self.altura)
        )

    def aplicar_efeito(self, personagem):
        if self.rect.colliderect(personagem.rect):
            if personagem.vida < constantes.max_vida:
                personagem.vida += 1


class Foguete(Coletáveis):
    def __init__(self, tupla_coord):
        super().__init__(tupla_coord)
        self.tipo = "Foguete"

        self.sprite = pygame.image.load(
            "sprites/mochila_a_jato_pixel_semfundo.png"
        ).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.sprite,
            (self.largura, self.altura)
        )

    def aplicar_efeito(self, personagem):
        personagem.vel_y = constantes.subida_foguete

class Cenoura_Envenenada(Coletáveis):
    def __init__(self, tupla_coord):
        super().__init__(tupla_coord)
        self.tipo = "Cenoura Envenenada"

        self.sprite = pygame.image.load(
            "sprites/cenoura_podre_semfundo.png"
        ).convert_alpha()

        self.sprite = pygame.transform.scale(
            self.sprite,
            (self.largura, self.altura)
        )

    def aplicar_efeito(self, personagem):
        personagem.vida -= 1


def gerar_colet(personagem):
    if len(lista_colets) < 4:
        qtde = random.randint(0, 2)

        for _ in range(qtde):
            coord_x = random.randint(0, constantes.largura_tela - constantes.largura_colet)
            coord_y = random.uniform(
                -constantes.altura_colet,
                personagem.y - constantes.altura_tela
            )

            tupla_coord = (coord_x, coord_y)
            tipo = random.choice(tipos_colets)

            if tipo == "Cura":
                colet = Cura(tupla_coord)

            elif tipo == "Cenoura Envenenada":
                colet = Cenoura_Envenenada(tupla_coord)

            elif tipo == "Foguete":
                colet = Foguete(tupla_coord)

            lista_colets.append(colet)