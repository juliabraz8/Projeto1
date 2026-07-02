import pygame
from pygame.locals import *
from sys import exit
import constantes
from coelho import Personagem
import coletaveis
import plataforma

pygame.init()

tela = pygame.display.set_mode((constantes.largura_tela, constantes.altura_tela))
pygame.display.set_caption('A subida do coelho')

placar = 0
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("couriernew", 24)

def escrever(texto, fonte, cor_texto, x, y):
    imagem = fonte.render(texto, True, cor_texto)
    tela.blit(imagem, (x,y))

def desenhoplacar():
    pygame.draw.rect(tela, (80, 200, 230), (0,0, constantes.largura_tela, 30))
    pygame.draw.line(tela, (0,80,100), (0, 30), (constantes.largura_tela, 30 ), 3) 
    escrever('PONTUAÇÃO: ' + str(placar), fonte, (0,80,100), 10, 3) # pontuação 


planodefundo = pygame.image.load("sprites/fundo.png").convert_alpha() # imagem do background
planodefundo = pygame.transform.scale(planodefundo, (constantes.largura_tela, constantes.altura_tela)) # escala do background
    

coelho = Personagem("Coelho", constantes.x, constantes.y)

coletaveis.gerar_colet(coelho)

plat1 = plataforma.Plataformas(
    coelho.x - (constantes.largura_plat - constantes.largura_coelho) / 2,
    coelho.rect.bottom
)

plataforma.plataformas.append(plat1)
plataforma.gerar_plats_iniciais()

inicio = True
play = True

while inicio:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = True
                inicio = False

    relogio.tick(60)
    tela.fill((255, 255, 255))

    texto = fonte.render("Aperte espaço para começar!", True, (0, 0, 0))
    tela.blit(texto, (120,355))

    pygame.display.flip()

while play:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # aparecer o background 
    tela.blit(planodefundo, (0, 0))
    relogio.tick(60)

    coelho.muda_cor()
    coelho.desenhar(tela)

    for plat in plataforma.plataformas:
        plat.desenhar(tela)

    for colet in coletaveis.lista_colets:
        colet.desenhar(tela)

    coelho.mover()
    coelho.aplicar_gravidade()

    for plat in plataforma.plataformas:
        if coelho.vel_y > 0 and coelho.rect.colliderect(plat.rect):
            plat.pular(coelho)

    for colet in coletaveis.lista_colets[:]:
        if coelho.rect.colliderect(colet.rect):
            colet.aplicar_efeito(coelho)
            if colet.tipo == "Foguete":
                placar -= 100
            coelho.contagem[colet.tipo] += 1
            coletaveis.lista_colets.remove(colet)


    if coelho.y < constantes.altura_tela // 2:
        diferenca = constantes.altura_tela // 2 - coelho.y
        coelho.y = constantes.altura_tela // 2

        for plat in plataforma.plataformas:
            plat.descer(diferenca)

        plataforma.plataformas = [
            p for p in plataforma.plataformas
            if p.y < constantes.altura_tela
        ]

        for colet in coletaveis.lista_colets:
            colet.descer(diferenca)

        coletaveis.lista_colets = [
            c for c in coletaveis.lista_colets
            if c.y < constantes.altura_tela
        ]

    plataforma.gerar_plats_gerais(coelho)
    coletaveis.gerar_colet(coelho)

    if coelho.y > constantes.altura_tela or coelho.vida == 0:
        play = False
    
    if coelho.vel_y < 0 and (pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_d] ):
        placar -= coelho.vel_y
    desenhoplacar()

    pygame.display.update()

sair = False

while not sair:
    for event in pygame.event.get():
        if event.type == QUIT:
            sair = True

    tela.blit(planodefundo,(0,0))
    planodefundo = pygame.image.load("sprites/fundo.png").convert_alpha() # imagem do background
    planodefundo = pygame.transform.scale(planodefundo, (constantes.largura_tela, constantes.altura_tela)) # escala do background

    texto = fonte.render("Itens coletados:", True, (0, 0, 0))
    tela.blit(texto, (100, 240))

    for i, (tipo, qtde) in enumerate(coelho.contagem.items()):
        texto = fonte.render(f"{tipo} - {qtde}", True, (0, 0, 0))
        tela.blit(texto, (150, 280 + 40 * i))

    pygame.display.update()

pygame.quit()