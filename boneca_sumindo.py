import pygame
import os

def b_pentagrama(tela, posicao,tamanho_tela):
    escuro = pygame.Surface((tamanho_tela[0], tamanho_tela[1]), pygame.SRCALPHA)
    escuro.fill((0, 0, 0, 0)) 
    

    if not hasattr(b_pentagrama, "frames"):
        b_pentagrama.frames = []
        for i in range(1, 32):
            caminho = os.path.join("pentagrama", f"b{i}.png")
            img = pygame.image.load(caminho).convert_alpha()
            img = pygame.transform.scale(img,(90,100))
            b_pentagrama.frames.append(img)

        b_pentagrama.frame_atual = 0
        b_pentagrama.contador = 0
        b_pentagrama.finalizou = False

    if b_pentagrama.finalizou:
        tela.blit(
            b_pentagrama.frames[-1],
            posicao
        )
        return

    b_pentagrama.contador += 1
    if b_pentagrama.contador >= 5: 
        b_pentagrama.contador = 0
        b_pentagrama.frame_atual += 1

        if b_pentagrama.frame_atual >= len(b_pentagrama.frames):
            b_pentagrama.frame_atual = len(b_pentagrama.frames) - 1
            b_pentagrama.finalizou = True


    
    tela.blit(
        b_pentagrama.frames[b_pentagrama.frame_atual],
        posicao
    )
    tela.blit(escuro,(0,0))