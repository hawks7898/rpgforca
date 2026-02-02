import pygame 
from sons_def import *
from pygame.locals import *
from minigame import forca
from time import sleep
from boneca_sumindo import*

pygame.init()

tamanho_tela = (800,700)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('casa das palavras')


#variaveis-----------------------------------------------------------------------------------------------------------



x = 500
y = 166
velocidade = 5
clock = pygame.time.Clock()
fundo_atual = ''
sala ='quarto'
estado = 'casa'
colisao = []
chave = 0
vida = 6
fps = 30
direcao = 'esquerda'
frame = 0
tempo = 0 
andando = False
armario = 'fechado'
item_boneca = 0
item_caneta = 0
jogou = True
criado_ab = 'fechado'



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

game_over = pygame.image.load('imagens/game_over.png').convert()
game_over = pygame.transform.scale(game_over, (tamanho_tela))

fundo_quarto = pygame.image.load('imagens/quarto.png').convert()
fundo_quarto = pygame.transform.scale(fundo_quarto, (tamanho_tela))
fundo_corredor = pygame.image.load('imagens/corredor.png').convert()
fundo_corredor = pygame.transform.scale(fundo_corredor,(tamanho_tela))


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
#boneca2 = pygame.image.load('imagens/boneca.png').convert_alpha()
#boneca3 = pygame.image.load('imagens/boneca.png').convert_alpha()
#boneca4 = pygame.image.load('imagens/boneca.png').convert_alpha()
#boneca5 = pygame.image.load('imagens/boneca.png').convert_alpha()

caneta = pygame.image.load('imagens/caneta.png').convert_alpha()
caneta = pygame.transform.scale(caneta,(40,75))

#pentagramas-----------------------------------------------------------------------------------------------------------
pentagrama = pygame.image.load('pentagrama/pentagrama_vazio.png').convert_alpha()
pentagrama = pygame.transform.scale(pentagrama,(90,100))
pentagrama_interagir = pentagrama.get_rect(topleft=(350,350))


#colisoes e interações---------------------------------------------------------------------------------------------------------------------------------




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

abrir = pygame.image.load('imagens/parede.png').convert_alpha()
abrir = pygame.transform.scale(abrir,(250,400))
abrir_colisao = abrir.get_rect(topleft = (260,120))


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



player_img = player_sprites[direcao][frame]
player_img = pygame.transform.scale(player_img, (45, 70))

player_rect = player_img.get_rect (topleft=(x,y))

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
corredor_colisoes = []



fundo()
while True:
    tela.fill((0, 0, 0))

    vida = max(0, min(6,vida))

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
                if bau_rect.collidepoint(mouse_pos) and sala == 'guardaroupa' and jogou:
                    estado = 'forca'
                    teste = forca(tela,fundo_atual,tamanho_tela)
                    estado = 'casa'    
                    if teste == 'perdeu':
                        vida -= 1 
                        if vida == 0:
                            fundo_atual = game_over
                            tela.blit(fundo_atual,(0, 0))
                            pygame.display.update()
                            sleep(10)
                            break

                    elif teste == 'venceu':
                        jogou = False
                        item_boneca = 1
                        interaçao()

            if abrir_colisao.collidepoint(mouse_pos) and sala == 'guarda roupa fechado':
                        sala = 'guardaroupa'
                        armario = 'aberto'

#movimento-------------------------------------------------------------------------------------------------------------------------

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_x]:
        fps = 60 
    else:
        fps = 30 

    if sala == 'quarto':
        colisao = quarto_colisoes   

    andando = False
    if estado == 'casa':
        if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
            player_rect.x -= velocidade
            direcao = 'esquerda'
            andando = True
            for obj in colisao:
                if player_rect.colliderect(obj):
                    player_rect.left = obj.right
            
                
                
        if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
            player_rect.x += velocidade
            direcao = 'direita'
            andando = True
            for obj in colisao:
                if player_rect.colliderect(obj):
                    player_rect.right = obj.left

        
        if teclas[pygame.K_w] or teclas[pygame.K_UP]:
            player_rect.y -= velocidade
            direcao = 'tras'
            andando = True
            for obj in colisao:
                if player_rect.colliderect(obj):
                    player_rect.top = obj.bottom 

        if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
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

#guardaroupa e corredor-----------------------------------------------------------------------------------------------------------------

    if player_rect.colliderect(porta_rect) and teclas[pygame.K_z] and chave >= 1:
        porta()
        sleep(0.1)
        sala = 'corredor'  
    if player_rect.colliderect(armariro_rect) and teclas[pygame.K_z]:
        if armario == 'aberto':
            sala = 'guardaroupa'
        elif armario == 'fechado':
            sala = 'guarda roupa fechado'
    if sala == 'guardaroupa' and teclas[pygame.K_x]:
        sala = 'quarto'    
    if sala == 'guarda roupa fechado' and teclas[pygame.K_x]:
        sala = 'quarto' 
    elif sala == 'guardaroupa' and teclas[pygame.K_2]:
        armario = 'fechado'
        sala = 'guarda roupa fechado'       
            
#criado interaçao-----------------------------------------------------------------------------------------------------------------------

    if player_rect.colliderect(criado_interasao) and criado_ab == 'fechado'and teclas[pygame.K_z]:
        sala = 'criado fechado'
    if player_rect.colliderect(criado_interasao) and criado_ab == 'aberto' and teclas[pygame.K_zp]:
        sala = 'criado aberto'    


#salas---------------------------------------------------------------------------------------------------------------------    
    if sala == 'quarto':
        fundo_atual = fundo_quarto 
    elif sala == 'corredor':
        fundo_atual = fundo_corredor
    elif sala == 'guardaroupa':   
        fundo_atual = fundo_guardaroupa 
    elif sala == 'guarda roupa fechado':
        fundo_atual = fundo_guardaroupa_fechado    
    

    #inventario----------------------------------------------------------------------------------------------------------


    if teclas[pygame.K_c] and estado == 'casa':
        estado = 'inventario'
    if teclas[pygame.K_x] and estado == 'inventario':
        estado = 'casa'    


#pentagrma-----------------------------------------------------------------------------------------------------------------------------

    if player_rect.colliderect(pentagrama_interagir)  and item_boneca == 1 and teclas[pygame.K_z]:
        estado = 'invocacao'
        item_boneca -=1
        agora = pygame.time.get_ticks()   
        


#desenhar na tela -------------------------------------------------------------------------------------------------------------

    if estado == 'casa':

             
#quarto--------------------------------------------------------------------------------------------------------------------------
        if sala == 'quarto':
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
            tela.blit(fundo_atual,(0, 0))
            tela.blit(criado,criado_interasao)
            
                    
                
            if item_boneca >=1:
                tela.blit(pentagrama,pentagrama_interagir)
            tela.blit(player_img, player_rect) 
            

        elif sala == 'guardaroupa':
            tela.blit(bau_img,bau_rect)
            tela.blit(fundo_atual,(0,0))
            
        elif sala == 'corredor':
            tela.blit(fundo_atual,(0,0))
            tela.blit(player_img, player_rect) #mmmmmm   

        elif sala == 'guarda roupa fechado':
            tela.blit(abrir,abrir_colisao)
            tela.blit(fundo_atual,(0,0))       

#vidas desnhos na tela--------------------------------------------------------------------------------------------------------
        if vida == 5: 
            tela.blit(forca1,(0,0))
        if vida == 4: 
            tela.blit(forca2,(0,0))
        if vida == 3: 
            tela.blit(forca3,(0,0))
        if vida == 2: 
            tela.blit(forca4,(0,0))
        if vida == 1: 
            tela.blit(forca5,(0,0))  
        if vida == 0: 
            tela.blit(forca6,(0,0))                     
                  

#inventario------------------------------------------------------------------------------------------------------

    elif teclas [pygame.K_c] and estado == 'inventario':
        tela.blit(papel,(0,100)) 
        tela.blit(bara_itens,(200,300))
        if item_boneca >= 1:
            tela.blit(boneca1,(210,315))
        if item_caneta >= 1:
            tela.blit(caneta,(290,300))    


#invocaçao----------------------------------------------------------------------------------------------------------------------
    elif estado == 'invocacao':
        tela.blit(fundo_atual,(0,0))
        
        

        if player_rect.colliderect(pentagrama_interagir)  and estado == 'invocacao':    
            b_pentagrama(tela,(350,350))
           
            if tempo_inicio - agora  >= 6000:
                estado = 'casa'    
        tela.blit(player_img, player_rect)         
            



    pygame.display.update()
