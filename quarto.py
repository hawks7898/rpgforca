import pygame 
from sons_def import *
from pygame.locals import *
from minigame import *
from time import sleep
from boneca_sumindo import *

def quarto (tamanho_tela,tela,game_variaveis):
    
    
    colisao = []
    fps = 30
    direcao = 'esquerda'
    frame = 0
    tempo = 0 
    andando = False
    velocidade = 5
    


    #variaveis-----------------------------------------------------------------------------------------------------------

    clock = pygame.time.Clock()


    #variaveis dos itens -----------------
    item_caneta = 0
    item_boneca = 0
    item_chave_boneca = 0
    item_chave_saida = 1
    pegou_c_s = False
    pegou_c_b = False




    #quarto jogo da forca-------------------------------------------------------------------------------- 

    papel_de_parede = pygame.image.load('parede_jogo/papel_de_parede.png').convert_alpha()
    #papel_de_parede = pygame.transform.scale(papel_de_parede,(100,100))
    papel_de_parede_int = papel_de_parede.get_rect(topleft=(690,115))


    teia = pygame.image.load('imagens/teia.png').convert_alpha()
    teia_int = teia.get_rect(topleft=(70,130))

    #biletes -----------------------------0--------------------

    bilete_ritual = pygame.image.load('biletes/papel.png').convert_alpha()

    bilete_forca = pygame.image.load('biletes/papel dobrado.png').convert_alpha()
    bilete_forca_int = bilete_forca.get_rect(topleft=(350,400))

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


    #fundos-------------------------------------------------------------------------------------------

    criado_fundo_fec_jogo = pygame.image.load('armario_selo/criado_fec.png').convert()
    criado_fundo_fec_jogo = pygame.transform.scale(criado_fundo_fec_jogo, (tamanho_tela))

    criado_fundo_aber_jogo = pygame.image.load('armario_selo/criado_aber.png').convert()
    criado_fundo_aber_jogo = pygame.transform.scale(criado_fundo_aber_jogo, (tamanho_tela))

    #------------------------------------------

    criado_fundo_fec = pygame.image.load('armario_selo/criado_fec.png').convert()
    criado_fundo_fec = pygame.transform.scale(criado_fundo_fec, (tamanho_tela))

    criado_fundo_aber = pygame.image.load('armario_selo/criado_tuto.png').convert()
    criado_fundo_aber = pygame.transform.scale(criado_fundo_aber, (tamanho_tela))

    #---------------------------------------------

    game_over = pygame.image.load('imagens/game_over.png').convert()
    game_over = pygame.transform.scale(game_over, (tamanho_tela))

    fundo_quarto = pygame.image.load('imagens/quarto.png').convert()
    fundo_quarto = pygame.transform.scale(fundo_quarto, (tamanho_tela))


    fundo_guardaroupa_bau = pygame.image.load('armario_selo/bau aberto.png').convert()
    fundo_guardaroupa_bau = pygame.transform.scale(fundo_guardaroupa_bau,(tamanho_tela))

    fundo_guardaroupa = pygame.image.load('imagens/guardaroupa2.png').convert()
    fundo_guardaroupa = pygame.transform.scale(fundo_guardaroupa,(tamanho_tela))

    fundo_guardaroupa_fechado = pygame.image.load('imagens/armario_fechado.png').convert()
    fundo_guardaroupa_fechado = pygame.transform.scale(fundo_guardaroupa_fechado,(tamanho_tela))

    #itens------------------------------------------------------------------------------------------------

    bara_itens = pygame.image.load('imagens/itens_local.png').convert_alpha()
    bara_itens = pygame.transform.scale(bara_itens,(380,80))

    papel = pygame.image.load('imagens/papel.png').convert_alpha()

    boneca1 = pygame.image.load('imagens/boneca.png').convert_alpha()
    boneca1 = pygame.transform.scale(boneca1,(54,54))
    boneca2 = pygame.image.load('imagens/boneca_item.png').convert_alpha()
    boneca2 = pygame.transform.scale(boneca2,(40,54))
    boneca2_int = boneca2.get_rect(topleft=(350,420))

    #boneca3 = pygame.image.load('imagens/boneca.png').convert_alpha()
    #boneca4 = pygame.image.load('imagens/boneca.png').convert_alpha()
    #boneca5 = pygame.image.load('imagens/boneca.png').convert_alpha()

    caneta = pygame.image.load('imagens/caneta.png').convert_alpha()
    caneta = pygame.transform.scale(caneta,(40,75))

    caneta_criado = pygame.image.load('imagens/caneta_criado.png').convert_alpha()
    caneta_criado = pygame.transform.scale(caneta_criado,(25,105))
    caneta_int = caneta_criado.get_rect(topleft=(450,325))

    chave_criado =  pygame.image.load('imagens/chave_boneca.png').convert_alpha()
    chave_criado = pygame.transform.scale(chave_criado,(54,54))

    papel_dobrado = pygame.image.load('biletes/papel_dobrad.png').convert_alpha()
    papel_dobrado_int = papel_dobrado.get_rect(topleft=(300,350))

    #pentagramas-----------------------------------------------------------------------------------------------------------
    pentagrama = pygame.image.load('pentagrama/pentagrama_vazio.png').convert_alpha()
    pentagrama = pygame.transform.scale(pentagrama,(90,100))
    pentagrama_interagir = pentagrama.get_rect(topleft=(350,350))

    #armario selos -----------------------------------------------------------------------------------------------------------------

    selo4 = pygame.image.load('armario_selo/todos.png').convert_alpha()
    selo4 = pygame.transform.scale(selo4,(77,100))

    selo3 = pygame.image.load('armario_selo/3.png').convert_alpha()
    selo3 = pygame.transform.scale(selo3,(77,100))

    selo2 = pygame.image.load('armario_selo/2.png').convert_alpha()
    selo2 = pygame.transform.scale(selo2,(77,100))

    selo1 = pygame.image.load('armario_selo/1.png').convert_alpha()
    selo1 = pygame.transform.scale(selo1,(77,100))

    armario_aberto = pygame.image.load('armario_selo/abrir.png').convert_alpha()
    armario_aberto = pygame.transform.scale(armario_aberto,(77,100))



    #colisoes e interações---------------------------------------------------------------------------------------------------------------------------------


    tabua = pygame.image.load('imagens/parede.png').convert_alpha()
    tabua = pygame.transform.scale(tabua,(60,30))
    tabua_inter = tabua.get_rect (topleft=(580,420))

    cama  = pygame.image.load('imagens/parede.png').convert_alpha()
    cama = pygame.transform.scale(tabua,(30,20))
    cama_inter = cama.get_rect (topleft=(600,230))

    criado_jogo = pygame.image.load('imagens/armariosinhodireita.png').convert_alpha()
    criado_jogo = pygame.transform.scale(criado_jogo,(48,40))
    criado_interasao_jogo = criado_jogo.get_rect(topleft = (528,140))


    armariro_img = pygame.image.load('imagens/armario.png').convert_alpha()
    armariro_img = pygame.transform.scale(armariro_img,(77,100))
    armariro_rect = armariro_img.get_rect (topleft=(435,96))

    bau_img = pygame.image.load('imagens/bauamaldiçoado.png').convert()
    bau_img = pygame.transform.scale(bau_img,(100,100))
    bau_rect = bau_img.get_rect(topleft = (315,420))

    cama_esqueda_img = pygame.image.load('imagens/camaesquerda.png').convert_alpha()
    cama_esqueda_img = pygame.transform.scale(cama_esqueda_img,(48,40))
    cama_esqueda_colisao = cama_esqueda_img.get_rect(topleft = (155,146))

    cama_direita_img = pygame.image.load('imagens/camadireita.png').convert_alpha()
    cama_direita_img = pygame.transform.scale(cama_direita_img,(48,40))
    cama_direita_colisao = cama_direita_img.get_rect(topleft = (600,146))

    armariosinho_img = pygame.image.load('imagens/armariosinhodireita.png').convert_alpha()
    armariosinho_img = pygame.transform.scale(armariosinho_img,(48,40))
    armariosinho_colisao = armariosinho_img.get_rect(topleft = (530,120))

    armariosinho_img2 = pygame.image.load('imagens/armariosinhodireita.png').convert_alpha()
    armariosinho_img2 = pygame.transform.scale(armariosinho_img2,(48,40))
    armariosinho_colisao2 = armariosinho_img2.get_rect(topleft = (218,120))

    criado = pygame.image.load('imagens/armariosinhodireita.png').convert_alpha()
    criado = pygame.transform.scale(criado,(48,40))
    criado_interasao = criado.get_rect(topleft = (218,140))

    armariro_img2 = pygame.image.load('imagens/armario.png').convert_alpha()
    armariro_img2 = pygame.transform.scale(armariro_img2,(77,100))
    armariro_rect2 = armariro_img2.get_rect (topleft=(445,60))


    #------------------------------------------------------------------------------------


    abrir = pygame.image.load('imagens/parede.png').convert_alpha()
    abrir = pygame.transform.scale(abrir,(250,400))
    abrir_colisao = abrir.get_rect(topleft = (260,120))

    abrir_criado = pygame.image.load('imagens/parede.png').convert_alpha()
    abrir_criado = pygame.transform.scale(abrir_criado,(50,50))
    abrir_criado_col = abrir_criado.get_rect(topleft = (380,380))

    abrir_criado_jogo = pygame.image.load('imagens/parede.png').convert_alpha()
    abrir_criado_jogo = pygame.transform.scale(abrir_criado_jogo,(360,140))
    abrir_criado_col_jogo = abrir_criado_jogo.get_rect(topleft = (230,300))



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

    player_rect = player_img.get_rect (topleft=(game_variaveis['x'],game_variaveis['y']))

    #parede---------------------------------------------------------------------------------------------------------------------

    parede_img = pygame.image.load('imagens/parede.png').convert_alpha()
    parede_img = pygame.transform.scale(parede_img,(30,900))
    parede_rect = parede_img.get_rect(topleft = (53,0))

    parede_img2 = pygame.image.load('imagens/parede.png').convert_alpha()
    parede_img2 = pygame.transform.scale(parede_img2,(30,900))
    parede2_rect = parede_img2.get_rect(topleft = (730,0))

    parede_img3 = pygame.image.load('imagens/parede.png').convert_alpha()
    parede_img3 = pygame.transform.scale(parede_img3,(900,30))
    parede3_rect = parede_img3.get_rect(topleft = (0,545))

    parede_img4 = pygame.image.load('imagens/parede.png').convert_alpha()
    parede_img4 = pygame.transform.scale(parede_img4,(900,85))
    parede4_rect = parede_img4.get_rect(topleft = (0,30))#cima

    porta_img =pygame.image.load('imagens/porta.png').convert_alpha()
    porta_img = pygame.transform.scale(porta_img,(73,100))
    porta_rect = porta_img.get_rect(topleft = (320,50))
    
    #------------------------------------------------------------------------------------------------------------------------

    quarto_colisoes = [parede2_rect,parede3_rect,parede4_rect,parede_rect,cama_esqueda_colisao,cama_direita_colisao,armariosinho_colisao,armariosinho_colisao2,armariro_rect2]

    inicio = pygame.time.get_ticks()
    fundo()
    while True:

        
        

        game_variaveis['vida'] = max(0, min(6,game_variaveis['vida']))
        game_variaveis['selos_quebrados'] = max(0, min(4,game_variaveis['selos_quebrados']))

        tempo_inicio = pygame.time.get_ticks()
        

        clock.tick(fps)

    #evento-------------------------------------------------------------------------------------------------------------------------------------------   
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    if bau_rect.collidepoint(mouse_pos) and game_variaveis['sala'] == 'guardaroupa'and item_caneta == 1 and not game_variaveis['jogou'] :
                        game_variaveis['estado'] = 'forca'
                        teste = forca(tela,game_variaveis['fundo_atual'],tamanho_tela)
                        game_variaveis['estado'] = 'casa'    
                        if teste == 'perdeu':
                            game_variaveis['vida'] -= 1

                        elif teste == 'venceu':
                            game_variaveis['jogou'] = True
                            game_variaveis['sala'] = 'quarto'
                            game_variaveis['bau'] = 'aberto'
                            interaçao()

                if abrir_colisao.collidepoint(mouse_pos) and game_variaveis['sala'] == 'guarda roupa fechado':
                    game_variaveis['sala'] = 'guardaroupa'
                    game_variaveis['armario'] = 'aberto'

                if abrir_criado_col.collidepoint(mouse_pos) and game_variaveis['sala'] == 'criado fechado':
                    game_variaveis['criado_ab'] = 'aberto'
                    game_variaveis['sala'] = 'criado aberto'

                if abrir_criado_col_jogo.collidepoint(mouse_pos) and game_variaveis['sala'] == 'criado jogo fechado' and item_chave_boneca >= 1:
                    item_chave_boneca = 0 
                    game_variaveis['criado_ab_jogo'] = 'aberto'
                    game_variaveis['sala'] = 'criado jogo aberto'   


                if boneca2_int.collidepoint(mouse_pos) and game_variaveis['sala'] == 'bau aberto':
                    item_boneca = 1  
                    
                if caneta_int.collidepoint(mouse_pos)  and game_variaveis['sala'] == 'criado aberto':
                    
                    item_caneta = 1     

                if papel_dobrado_int.collidepoint(mouse_pos) and game_variaveis['sala'] == 'bau aberto' :
                    game_variaveis['sala'] = 'bilete ritual'    

                if bilete_forca_int.collidepoint(mouse_pos) and game_variaveis['sala'] == 'criado jogo aberto':
                    if not game_variaveis['jogou_criado'] and item_caneta == 1:
                        jogo_criado = forca_criado(tela, game_variaveis['fundo_atual'],tamanho_tela)
                        if jogo_criado == 'perdeu':
                            game_variaveis['vida'] -= 1
                        elif jogo_criado == 'venceu':
                            game_variaveis['selos_quebrados'] += 1
                            game_variaveis['jogou_criado'] = True   
                
    #itens---------------------------------

        if player_rect.colliderect(tabua_inter) and teclas[pygame.K_z] :
            if not pegou_c_b:
                item_chave_boneca = 1
                pegou_c_b = True            

    #movimento-------------------------------------------------------------------------------------------------------------------------

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_x]:
            fps = 60 
        else:
            fps = 30 
        
        if game_variaveis['sala'] == 'quarto':
            colisao = quarto_colisoes   

        andando = False
        if game_variaveis['estado'] == 'casa':
            if  teclas[pygame.K_LEFT]:
                player_rect.x -= velocidade
                direcao = 'esquerda'
                andando = True
                for obj in colisao:
                    if player_rect.colliderect(obj):
                        player_rect.left = obj.right
                
                    
                    
            if  teclas[pygame.K_RIGHT]:
                player_rect.x += velocidade
                direcao = 'direita'
                andando = True
                for obj in colisao:
                    if player_rect.colliderect(obj):
                        player_rect.right = obj.left

            
            if  teclas[pygame.K_UP]:
                player_rect.y -= velocidade
                direcao = 'tras'
                andando = True
                for obj in colisao:
                    if player_rect.colliderect(obj):
                        player_rect.top = obj.bottom 


            if  teclas[pygame.K_DOWN]:
                player_rect.y += velocidade 
                direcao = 'frente'
                andando = True
                for obj in colisao:
                    if player_rect.colliderect(obj):
                        player_rect.bottom = obj.top     

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

        if player_rect.colliderect(cama_inter) and teclas[pygame.K_z]:
            player_rect.x,player_rect.y = 580,220
            player_img = player_deitado              

            if not game_variaveis['jogou_cama'] and item_caneta == 1:   
                player_img = player_deitado   
                forcama = forca_cama(tela,game_variaveis['fundo_atual'],tamanho_tela)

                if forcama == 'venceu':
                    game_variaveis['jogou_cama'] = True
                    game_variaveis['selos_quebrados'] += 1
                elif forcama == 'perdeu':
                    game_variaveis['vida'] -= 1     

    #guardaroupa e corredor-----------------------------------------------------------------------------------------------------------------

        if player_rect.colliderect(porta_rect) and teclas[pygame.K_z] and item_chave_saida >= 1 or player_rect.colliderect(porta_rect) and teclas[pygame.K_z] and game_variaveis['fase1'] or player_rect.colliderect(porta_rect) and teclas[pygame.K_z] and pegou_c_s :
            porta()
            
            item_chave_saida = 0
            pegou_c_s = True
            
        elif player_rect.colliderect(porta_rect) and teclas[pygame.K_z] and item_chave_saida == 0:
            trancado()
            
            
                

        if player_rect.colliderect(armariro_rect) and teclas[pygame.K_z] and game_variaveis['selos_quebrados'] == 4:
            if game_variaveis['armario'] == 'aberto':
                if game_variaveis['bau'] == 'aberto':
                    game_variaveis['sala'] = 'bau aberto'
                elif game_variaveis['bau'] == 'fechado':
                    game_variaveis['sala'] = 'guardaroupa'
            elif game_variaveis['armario'] == 'fechado':
                game_variaveis['sala'] = 'guarda roupa fechado'

        if game_variaveis['sala'] == 'guardaroupa' and teclas[pygame.K_x]:
            game_variaveis['sala'] = 'quarto'    
        if game_variaveis['sala'] == 'guarda roupa fechado' and teclas[pygame.K_x] or game_variaveis['sala'] == 'bau aberto' and teclas[pygame.K_x]:
            game_variaveis['sala'] = 'quarto' 
        elif game_variaveis['sala'] == 'guardaroupa' and teclas[pygame.K_2]:
            game_variaveis['armario'] = 'fechado'
            game_variaveis['sala'] = 'guarda roupa fechado'       
                
    #criado interaçao-----------------------------------------------------------------------------------------------------------------------


        if player_rect.colliderect(criado_interasao) and teclas[pygame.K_z]:
            game_variaveis['estado'] = 'criado'
            if game_variaveis['criado_ab'] == 'fechado':
                game_variaveis['sala'] = 'criado fechado'
            elif game_variaveis['criado_ab'] == 'aberto':
                game_variaveis['sala'] = 'criado aberto'

            
        if teclas[pygame.K_x] and game_variaveis['estado'] == 'criado':
            game_variaveis['sala'] = 'quarto'
            game_variaveis['estado'] = 'casa'

        if player_rect.colliderect(criado_interasao_jogo) and teclas[pygame.K_z]:
            game_variaveis['estado'] = 'criado jogo'
            if game_variaveis['criado_ab_jogo'] == 'fechado':
                game_variaveis['sala'] = 'criado jogo fechado'
            elif game_variaveis['criado_ab_jogo'] == 'aberto':
                game_variaveis['sala'] = 'criado jogo aberto'

            
        if teclas[pygame.K_x] and game_variaveis['estado'] == 'criado jogo':
            game_variaveis['sala'] = 'quarto'
            game_variaveis['estado'] = 'casa'

    #====================================================================================================================================================
        if player_rect.colliderect(papel_de_parede_int) and game_variaveis['selos_quebrados'] == 3 and item_caneta == 1 and teclas[pygame.K_z] and not game_variaveis['jogou_parede'] :
            v_d = ultimo(tela,game_variaveis['fundo_atual'],tamanho_tela)
            if v_d == 'perdeu':
                game_variaveis['vida'] -= 1 
            elif v_d == 'venceu':
                game_variaveis['selos_quebrados'] += 1
                game_variaveis['jogou_parede'] = True

        if player_rect.colliderect(teia_int) and item_caneta == 1 and teclas[pygame.K_z] and not game_variaveis['jogou_teia']:
            vit_der = teia_jogo(tela,game_variaveis['fundo_atual'],tamanho_tela)
            if vit_der == 'perdeu':
                game_variaveis['vida'] -= 1 
            if vit_der == 'venceu':
                game_variaveis['jogou_teia'] = True
                game_variaveis['selos_quebrados'] += 1 


            
        


    #salas---------------------------------------------------------------------------------------------------------------------    
        if game_variaveis['sala'] == 'quarto':
            game_variaveis['fundo_atual'] = fundo_quarto 


        elif game_variaveis['sala'] == 'guardaroupa':   
            game_variaveis['fundo_atual'] = fundo_guardaroupa 

        elif game_variaveis['sala'] == 'guarda roupa fechado':
            game_variaveis['fundo_atual'] = fundo_guardaroupa_fechado   


        elif game_variaveis['sala'] == 'bau aberto':
            game_variaveis['fundo_atual'] = fundo_guardaroupa_bau    


        elif game_variaveis['sala']    == 'criado fechado':
            game_variaveis['fundo_atual'] = criado_fundo_fec


        elif game_variaveis['sala']    == 'criado aberto':
            game_variaveis['fundo_atual'] = criado_fundo_aber


        elif game_variaveis['sala'] == 'bilete ritual':
            game_variaveis['fundo_atual'] = bilete_ritual    


        elif game_variaveis['sala'] == 'criado jogo fechado':
            game_variaveis['fundo_atual'] = criado_fundo_fec_jogo   


        elif game_variaveis['sala'] == 'criado jogo aberto':
            game_variaveis['fundo_atual'] = criado_fundo_aber_jogo   
        

        #inventario----------------------------------------------------------------------------------------------------------


        if teclas[pygame.K_c] and game_variaveis['estado'] == 'casa':
            game_variaveis['estado'] = 'inventario'
        if teclas[pygame.K_x] and game_variaveis['estado'] == 'inventario':
            game_variaveis['estado'] = 'casa'    


    #pentagrma-----------------------------------------------------------------------------------------------------------------------------

        if player_rect.colliderect(pentagrama_interagir)  and item_boneca == 1 and teclas[pygame.K_z]:
            game_variaveis['estado'] = 'invocacao'
            item_boneca -=1
            agora = pygame.time.get_ticks()   
            


    #desenhar na tela -------------------------------------------------------------------------------------------------------------

        if game_variaveis['estado'] == 'casa':

                
    #quarto--------------------------------------------------------------------------------------------------------------------------
            if game_variaveis['sala'] == 'quarto':
                tela.blit(parede_img4,parede4_rect)
                tela.blit(parede_img3,parede3_rect)
                tela.blit(parede_img2,parede2_rect)
                tela.blit(parede_img,parede_rect)
                tela.blit(cama_esqueda_img,cama_esqueda_colisao)
                tela.blit(cama_direita_img,cama_direita_colisao)
                tela.blit(armariosinho_img,armariosinho_colisao)
                tela.blit(armariro_img2,armariro_rect2)
                tela.blit(armariosinho_img2,armariosinho_colisao2)
                tela.blit(porta_img, porta_rect)
                tela.blit(armariro_img, armariro_rect)
                tela.blit(criado,criado_interasao)
                tela.blit(tabua,tabua_inter)
                tela.blit(cama,cama_inter)
                tela.blit(criado_jogo,criado_interasao_jogo)
                #oque vai aparecer -----------------
                
                tela.blit(game_variaveis['fundo_atual'],(0, 0))
                tela.blit(teia,teia_int)
                if game_variaveis['selos_quebrados'] == 3:
                    tela.blit(papel_de_parede,papel_de_parede_int)

                if game_variaveis['selos_quebrados'] == 0:
                    tela.blit(selo4,(435,96))
                elif game_variaveis['selos_quebrados'] == 1:
                    tela.blit(selo3,(435,96))    
                elif game_variaveis['selos_quebrados'] == 2:
                    tela.blit(selo2,(435,96))
                elif game_variaveis['selos_quebrados'] == 3:
                    tela.blit(selo1,(435,96))     
                if game_variaveis['armario'] == 'aberto':
                    tela.blit(armario_aberto,(435,96))

                    
                if item_boneca >=1:
                    tela.blit(pentagrama,pentagrama_interagir)
                tela.blit(player_img, player_rect) 
                
    #------------------------------------------------------------------
            elif game_variaveis['sala'] == 'guardaroupa':
                tela.blit(bau_img,bau_rect)
                tela.blit(game_variaveis['fundo_atual'],(0,0))
                
    #--------------------------------------------------
            elif game_variaveis['sala'] == 'guarda roupa fechado':
                tela.blit(abrir,abrir_colisao)
                tela.blit(game_variaveis['fundo_atual'],(0,0))       
    #--------------------------------------------------        
            elif game_variaveis['sala'] == 'bau aberto':
                tela.blit(game_variaveis['fundo_atual'],(0,0))  
                tela.blit(papel_dobrado,papel_dobrado_int)
                if item_boneca == 0 and not game_variaveis['ritual']:
                    tela.blit(boneca2,boneca2_int)

            elif game_variaveis['sala'] == 'bilete ritual':
                tela.blit(game_variaveis['fundo_atual'],(0,0))        
                if teclas[pygame.K_x]:
                    sleep(0.5)
                    game_variaveis['sala'] = 'bau aberto'
    #inventario------------------------------------------------------------------------------------------------------

        elif teclas [pygame.K_c] and game_variaveis['estado'] == 'inventario':
            tela.blit(papel,(0,100)) 
            tela.blit(bara_itens,(200,300))
            if item_boneca >= 1:
                tela.blit(boneca1,(210,315))
            if item_caneta >= 1:
                tela.blit(caneta,(290,300))    
            if item_chave_boneca == 1:
                tela.blit(chave_criado,(364,312))    


    #invocaçao----------------------------------------------------------------------------------------------------------------------
        elif game_variaveis['estado'] == 'invocacao':
            tela.blit(game_variaveis['fundo_atual'],(0,0))
            
            

            if player_rect.colliderect(pentagrama_interagir)  and game_variaveis['estado'] == 'invocacao':    
                b_pentagrama(tela,(350,350))
            
                if tempo_inicio - agora  >= 6000:
                    game_variaveis['ritual'] = True
                    game_variaveis['estado'] = 'casa'  
                    item_chave_saida = 1
            tela.blit(player_img, player_rect)    
    #-----------------------------------------------------------------------
        if game_variaveis['vida'] == 0:
            game_variaveis['estado'] = 'game over'
            tela.fill((0, 0, 0))
            game_variaveis['fundo_atual'] = game_over
            tela.blit(game_variaveis['fundo_atual'],(0, 0))
    #--------------------------------------------------------------------------
        elif game_variaveis['estado'] == 'criado':
            tela.blit(abrir_criado,abrir_criado_col)
            tela.blit(game_variaveis['fundo_atual'],(0,0)) 
            if item_caneta == 0 and game_variaveis['criado_ab'] == 'aberto':
                    tela.blit(caneta_criado,caneta_int) 
            
        elif game_variaveis['estado'] == 'criado jogo':
            tela.blit(game_variaveis['fundo_atual'],(0,0)) 

            if game_variaveis['sala'] == 'criado jogo aberto':
                tela.blit(bilete_forca,bilete_forca_int)


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
