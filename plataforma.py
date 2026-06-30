import pygame
import random

# Configurações das Plataformas

plataformas = [pygame.Rect(150, 500, 100, 20)]

# Gerar algumas plataformas iniciais
for i in range(1, 5):
    inicial_x = random.randint(0, largura - 100)
    inicial_y = 500 - (i * 70)
    plataformas.append(pygame.Rect(inicial_x, inicial_y, 100, 20))

# Loop
rodando = True
while rodando:
    relogio.tick(60)
    tela.fill((255, 255, 255))

    # Gravidade
    personagem.vel_y += personagem.gravidade
    personagem.y += personagem.vel_y
    personagem.rect = pygame.Rect(personagem.x, personagem.y, 40, 40)

    # Colisão
    if personagem.vel_y > 0:
        for plat in plataformas:
            if personagem.rect.colliderect(plat):
                if personagem.rect.bottom < plat.rect.centery:
                    personagem.rect.bottom = plat.rect.top #Coelho está no topo da plataforma
                    personagem.vel_y = personagem.forca_pulo
                    break 

    # 5. Efeito de Câmera Infinito
    if personagem.y < altura / 2:
        deslocamento = (altura / 2) - personagem.y
        personagem.y = altura / 2 
        
        # Desce as plataformas
        for plat in plataformas:
            plat.y += deslocamento
            
    # 6. Gerador Infinito de Plataformas
    plataformas = [p for p in plataformas if p.y < altura]
    
    # Criação de plataformas
    while len(plataformas) < 5:
        ultimo_y = plataformas[-1].y
        plataformas_x = random.randint(0, largura - 100)
        plataformas_y = ultimo_y - random.randint(60, 100)
        plataformas.append(pygame.Rect(plataformas_x, plataformas_y, 100, 20))

    # 7. Desenho das Plataformas
    for plat in plataformas:
        pygame.draw.rect(tela, (0, 255, 0), plat) 
        

    pygame.display.update()

pygame.quit()

class Plataformas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cor = (128, 128, 128)
    
    def pular(self, vel_y):
        if personagem.rect.bottom < plat.rect.centery:
            personagem.rect.bottom = plat.rect.top #Coelho está no topo da plataforma
            personagem.vel_y = personagem.forca_pulo
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, plat)

def gerar_plat():
    inicial_x = random.randint(0, largura - 100)
    inicial_y = 500 - (i * 70)
    plataformas.append(pygame.Rect(inicial_x, inicial_y, 100, 20))