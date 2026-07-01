import pygame
from pygame.locals import *
from sys import exit
import constantes
from coelho import Personagem
import coletaveis
import plataforma

pygame.init()

#Criar o plano de fundo
tela = pygame.display.set_mode((constantes.largura_tela,constantes.altura_tela))#Formatação

pygame.display.set_caption('A subida do coelho')#Nome da aba
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("arial", 24)

coelho = Personagem("Coelho", constantes.x, constantes.y)
coletaveis.gerar_colet(coelho) #gerar coletáveis iniciais
plat1 = plataforma.Plataformas(coelho.x-(constantes.largura_plat-constantes.largura_coelho)/2, coelho.rect.bottom) #gerar uma plataforma inicial que fica centralizada e abaixo da tela 'segurando' o coelho
plataforma.plataformas.append(plat1)
plataforma.gerar_plats_iniciais() #gerar plataformas iniciais


inicio = True
play = True
while inicio: #tela de menu
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit() 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = True #começar quando apertar espaço
                inicio = False
    
    relogio.tick(60)
    tela.fill((255, 255, 255)) #tela branca (enqto nn tem imagem)
    texto = fonte.render("Aperte espaço para começar!", True, (0, 0, 0))
    tela.blit(texto, (145, 355))
    pygame.display.flip()

while play == True: #jogo de fato
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit() 

    tela.fill((0, 0, 0))
    relogio.tick(60)
    coelho.muda_cor()
    coelho.desenhar(tela)
    for plat in plataforma.plataformas:
        plat.desenhar(tela)
    for colet in coletaveis.lista_colets:
        colet.desenhar(tela)

    coelho.mover()
    coelho.aplicar_gravidade()

    #analisar colisão:
    for plat in plataforma.plataformas:
        if coelho.vel_y > 0 and coelho.rect.colliderect(plat.rect):
            # if coelho.rect.bottom < plat.rect.centery: 
                plat.pular(coelho)
    for colet in coletaveis.lista_colets[:]:
        if coelho.rect.colliderect(colet.rect):
            colet.aplicar_efeito(coelho)
            coelho.contagem[colet.tipo] += 1
            coletaveis.lista_colets.remove(colet)

    #fazer a tela acompanhar o coelho:
    if coelho.y < constantes.altura_tela//2:
        diferenca = constantes.altura_tela//2 - coelho.y #quanto a tela vai "subir"
        coelho.y = constantes.altura_tela//2
        for plat in plataforma.plataformas:
            plat.descer(diferenca)
        plataforma.plataformas = [p for p in plataforma.plataformas if p.y < constantes.altura_tela]
        for colet in coletaveis.lista_colets:
            colet.descer(diferenca)
        coletaveis.lista_colets = [c for c in coletaveis.lista_colets if c.y < constantes.altura_tela]
    
    plataforma.gerar_plats_gerais(coelho)
    coletaveis.gerar_colet(coelho)

    if coelho.y > constantes.altura_tela or coelho.vida == 0: #morreu
        play = False

    pygame.display.update()

else:
    sair = False
    while sair == False: #tela final 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit() 
        
        tela.fill((255, 0, 0))
        texto = fonte.render("Itens coletados:", True, (0, 0, 0))
        tela.blit(texto, (100, 240))
        for i, (tipo, qtde) in enumerate(coelho.contagem.items()):
            texto = fonte.render(f"{tipo} - {qtde}", True, (0, 0, 0))
            tela.blit(texto, (150, 280+40*i))
        pygame.display.update()

pygame.quit()