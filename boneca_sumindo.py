def b_pentagrama(tela, posicao):
    import pygame
    import os

    # carregar imagens (só na primeira vez)
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

    # se já terminou, só desenha o último frame
    if b_pentagrama.finalizou:
        tela.blit(
            b_pentagrama.frames[-1],
            posicao
        )
        return

    # controle da animação
    b_pentagrama.contador += 1
    if b_pentagrama.contador >= 5:  # velocidade
        b_pentagrama.contador = 0
        b_pentagrama.frame_atual += 1

        if b_pentagrama.frame_atual >= len(b_pentagrama.frames):
            b_pentagrama.frame_atual = len(b_pentagrama.frames) - 1
            b_pentagrama.finalizou = True

    # desenha
    tela.blit(
        b_pentagrama.frames[b_pentagrama.frame_atual],
        posicao
    )
