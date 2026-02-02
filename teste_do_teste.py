import pygame
from boneca_sumindo import *

pygame.init()

tamanho_tela = (800,700)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('casa das palavras')

fundo_quarto = pygame.image.load('imagens/quarto.png').convert()
fundo_quarto = pygame.transform.scale(fundo_quarto, (tamanho_tela))

clock = pygame.time.Clock()
rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.blit(fundo_quarto,(0,0))

    b_pentagrama(tela, (300, 200))

    pygame.display.flip()
    clock.tick(60)
