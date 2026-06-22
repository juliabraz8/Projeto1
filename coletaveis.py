from constantes import subida_foguete, max_vida

class Coletáveis:
    def __init__(self, x, y, largura, altura, tuplaCor): #x e y são as coordenadas iniciais do coletável
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.coletado = False
        self.cor = tuplaCor
    
class Cura(Coletáveis):
    def aplicar_efeito(self, personagem):
        if personagem.vida < max_vida:
            personagem.vida += 1

class Foguete(Coletáveis):
    def aplicar_efeito(self, personagem):
        personagem.vel = subida_foguete

class Cenoura_Envenenada(Coletáveis):
    def aplicar_efeito(self, personagem):
        personagem.vida -= 1