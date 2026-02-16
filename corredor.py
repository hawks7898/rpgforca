import pygame 
from sons_def import *
from pygame.locals import *
from minigame import *
from time import sleep
from boneca_sumindo import *

def corredor (tamanho_tela,tela,game_variaveis):
    
    LARGURA, ALTURA = tamanho_tela
    camera_x = 0
    camera_y = 0
    fps = 30
    direcao = 'frente'
    frame = 0
    tempo = 0 
    andando = False
    velocidade = 5
    game_variaveis['x'] = 450
    game_variaveis['y'] = 250

    clock = pygame.time.Clock()
    

    game_over = pygame.image.load('imagens/game_over.png').convert()
    game_over = pygame.transform.scale(game_over, (tamanho_tela))


    fundo = pygame.image.load("imagens/corredor.png").convert()
    fundo = pygame.transform.scale(fundo,(900,1200))
    fundo_rect = fundo.get_rect()

   
   

    #vidas sprites---------------------------------------------------------------------------------------------------------

    forca1 = pygame.image.load('vidas/vida1.png').convert_alpha()
    forca1 = pygame.transform.scale(forca1,(120,150))

    forca2 = pygame.image.load('vidas/vida2.png').convert_alpha()
    forca2 = pygame.transform.scale(forca2,(120,150))

    forca3 = pygame.image.load('vidas/vida3.png').convert_alpha()
    forca3 = pygame.transform.scale(forca3,(120,150))

    forca4 = pygame.image.load('vidas/vida4.png').convert_alpha()
    forca4 = pygame.transform.scale(forca4,(120,150))

    forca5 = pygame.image.load('vidas/vida5.png').convert_alpha()
    forca5 = pygame.transform.scale(forca5,(120,150))

    forca6 = pygame.image.load('vidas/vida6.png').convert_alpha()
    forca6 = pygame.transform.scale(forca6,(120,150))


    #itens------------------------------------------------------------------------------------------------

    bara_itens = pygame.image.load('imagens/itens_local.png').convert_alpha()
    bara_itens = pygame.transform.scale(bara_itens,(380,80))

    papel = pygame.image.load('imagens/papel.png').convert_alpha()
    caneta = pygame.image.load('imagens/caneta.png').convert_alpha()
    caneta = pygame.transform.scale(caneta,(40,75))

    player_sprites = {
        "frente": [
            pygame.image.load("imagens/playerfrente0.png").convert_alpha(),
            pygame.image.load("imagens/playerfrente1.png").convert_alpha(),
            pygame.image.load("imagens/playerfrente2.png").convert_alpha()
        ],
        "tras": [
            pygame.image.load("imagens/playertras0.png").convert_alpha(),
            pygame.image.load("imagens/playertras1.png").convert_alpha(),
            pygame.image.load("imagens/playertras2.png").convert_alpha()
        ],
        "direita": [
            pygame.image.load("imagens/playerdireita0.png").convert_alpha(),
            pygame.image.load("imagens/playerdireita1.png").convert_alpha(),
            pygame.image.load("imagens/playerdireita2.png").convert_alpha()
        ],
        "esquerda": [
            pygame.image.load("imagens/playeresquerda0.png").convert_alpha(),
            pygame.image.load("imagens/playeresquerda1.png").convert_alpha(),
            pygame.image.load("imagens/playeresquerda2.png").convert_alpha()
        ]
    }

    player_deitado = pygame.image.load('imagens/playerdeitado.png').convert_alpha()
    player_deitado = pygame.transform.scale(player_deitado, (50, 30))


    player_img = player_sprites[direcao][frame]
    player_img = pygame.transform.scale(player_img, (45, 70))
    player_rect = player_img.get_rect(center=(game_variaveis['x'],game_variaveis['y']))

#paredes===========================================================================================================================
#========================================================================================================================

    parede1=pygame.image.load('imagens/parede.png').convert_alpha()
    parede1 = pygame.transform.scale(parede1,(30,1000))
    parede1_rect = parede1.get_rect(topleft = (790,150))
    
    parede2=pygame.image.load('imagens/parede.png').convert_alpha()
    parede2 = pygame.transform.scale(parede2,(600,350))
    parede2_rect = parede2.get_rect(topleft = (640,450))
#======================================================================================================================
#================================================================================================================================
    
    porta_img =pygame.image.load('imagens/porta.png').convert_alpha()
    porta_img = pygame.transform.scale(porta_img,(73,100))
    porta_quarto_rect = porta_img.get_rect(topleft = (410,110))

    colisao_corredor = [parede1_rect,parede2_rect]

    while True:
        
        game_variaveis['vida'] = max(0, min(6,game_variaveis['vida']))
        
        

        clock.tick(fps)

    #evento-------------------------------------------------------------------------------------------------------------------------------------------   
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
               

#movimento=============================================================================================
#======================================================================================================================================

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_x]:
            fps = 60 
        else:
            fps = 30 

        andando = False
        if game_variaveis['estado'] == 'casa':
            if  teclas[pygame.K_LEFT]:
                player_rect.x -= velocidade
                direcao = 'esquerda'
                andando = True
                for obj in colisao_corredor:
                    if player_rect.colliderect(obj):
                        player_rect.left = obj.right
                
                    
                    
            if  teclas[pygame.K_RIGHT]:
                player_rect.x += velocidade
                direcao = 'direita'
                andando = True
                for obj in colisao_corredor:
                    if player_rect.colliderect(obj):
                        player_rect.right = obj.left

            
            if  teclas[pygame.K_UP]:
                player_rect.y -= velocidade
                direcao = 'tras'
                andando = True
                for obj in colisao_corredor:
                    if player_rect.colliderect(obj):
                        player_rect.top = obj.bottom 


            if  teclas[pygame.K_DOWN]:
                player_rect.y += velocidade 
                direcao = 'frente'
                andando = True
                for obj in colisao_corredor:
                    if player_rect.colliderect(obj):
                        player_rect.bottom = obj.top     
            camera_x = player_rect.centerx - LARGURA // 2
            camera_y = player_rect.centery - ALTURA // 2
    #animação do player-------------------------------------------------------------------------------------------------

        if andando:
            tempo += 1
            if tempo >= 8:
                frame += 1 
                if frame > 2:
                    frame = 1 
                tempo = 0 
        else: 
            frame = 0    

        player_img = player_sprites[direcao][frame] 
        
        if direcao == "direita":
            player_img = pygame.transform.scale(player_img, (33, 65))    
        elif andando == False and direcao == "esquerda":
            player_img = pygame.transform.scale(player_img, (33, 65))   
        elif andando == True and direcao == "esquerda":
            player_img = pygame.transform.scale(player_img, (35, 65))                  
        else:    
            player_img = pygame.transform.scale(player_img, (42, 65))    
        
        camera_x = max(0, min(camera_x, fundo_rect.width - LARGURA))
        camera_y = max(0, min(camera_y, fundo_rect.height - ALTURA))

#=========================================================================================================================================
#======================================================================================================================================

        if player_rect.colliderect(porta_quarto_rect) and teclas[pygame.K_z]:
            return('quarto')
            break

   #inventario===============================================================
        if teclas[pygame.K_c] and game_variaveis['estado'] == 'casa':
            game_variaveis['estado'] = 'inventario'
        if teclas[pygame.K_x] and game_variaveis['estado'] == 'inventario':
            game_variaveis['estado'] = 'casa'    


          


    

        if game_variaveis['estado'] == 'casa':
            tela.blit(fundo, (-camera_x, -camera_y))
            tela.blit(porta_img,(porta_quarto_rect.x-camera_x,porta_quarto_rect.y-camera_y))
            #tela.blit(parede2,(parede2_rect.x-camera_x, parede2_rect.y-camera_y))
            tela.blit(player_img, (player_rect.x - camera_x, player_rect.y - camera_y))
                

    #inventario------------------------------------------------------------------------------------------------------

        elif teclas [pygame.K_c] and game_variaveis['estado'] == 'inventario':
            tela.blit(papel,(0,100)) 
            tela.blit(bara_itens,(200,300))
            if game_variaveis['item_caneta'] >= 1:
                tela.blit(caneta,(290,300))
           

    #-----------------------------------------------------------------------
        if game_variaveis['vida'] == 0:
            game_variaveis['estado'] = 'game over'
            tela.fill((0, 0, 0))
            game_variaveis['fundo_atual'] = game_over
            tela.blit(game_variaveis['fundo_atual'],(0, 0))

    #vidas na tela --------------------------------------------------------------------------------------------------------
        if game_variaveis['vida'] == 5: 
            tela.blit(forca1,(0,0))
        if game_variaveis['vida'] == 4: 
            tela.blit(forca2,(0,0))
        if game_variaveis['vida'] == 3: 
            tela.blit(forca3,(0,0))
        if game_variaveis['vida'] == 2: 
            tela.blit(forca4,(0,0))
        if game_variaveis['vida'] == 1: 
            tela.blit(forca5,(0,0))  
        if game_variaveis['vida'] == 0: 
            tela.blit(forca6,(0,0))            
                

        pygame.display.update()
