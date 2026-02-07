def forca (tela,fundo_atual,tamanho_tela):
    import pygame 
    from shlex import join 
    from pygame import KEYDOWN
    from time import sleep 

    

    forca1 = pygame.image.load('imagens/forca1.png').convert_alpha()
    forca2 = pygame.image.load('imagens/cabeca.png').convert_alpha()
    forca3 = pygame.image.load('imagens/Corpinho.png').convert_alpha()
    forca5 = pygame.image.load('imagens/bracinho_2.png').convert_alpha()
    forca4 = pygame.image.load('imagens/Bracinho.png').convert_alpha()
    forca6 = pygame.image.load('imagens/perna.png').convert_alpha()
    forca7 = pygame.image.load('imagens/aaaaaaaaaaa.png').convert_alpha()
   

    fase = forca1
    

    fonte = pygame.font.Font('fontes/Dogica.ttf',32)
    palavra = 'maldiçao'
    letras = ['_'] * len (palavra)
    letras_usadas = []
    tentativas = 6

    liga = True
    while liga:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                #if event.key == pygame.K_ESCAPE:
                    #liga = False  
                if event.unicode.isalpha():
                    letra = event.unicode.lower()

                    if letra in palavra:
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    
                        for i in range(len(palavra)):
                            if palavra[i] == letra:
                                letras[i]=letra
                    elif letra not in letras_usadas:
                        tentativas -= 1
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    



        

        if tentativas == 6:
            fase = forca1
        elif tentativas == 5:
            fase = forca2    
        elif tentativas == 4:
            fase = forca3
        elif tentativas == 3:
            fase = forca4      
        elif tentativas == 2:
            fase = forca5
        elif tentativas == 1:
            fase = forca6          
        elif tentativas == 0:
            fase = forca7  
              

        tela.blit(fundo_atual,(0, 0))
        
        
        texto = fonte.render(''.join(letras),True,(0,0,0)) 
        tela.blit(fase,(90,100))
        tela.blit(texto,(400,360)) 

       # usadas = fonte.render('usadas:'+','.join(letras_usadas),True,(0,0,0))
      #  tela.blit(usadas,(250,180))

        pygame.display.update()      

        if '_' not in letras:
            tela.blit(fundo_atual,(0, 0))
        
            texto = fonte.render(''.join(letras),True,(0,0,0)) 
            tela.blit(fase,(90,100))
            tela.blit(texto,(400,360)) 
            pygame.display.update()    
            sleep(2)
            return('venceu')
            break

        if tentativas == 0:
            sleep(3)
            susto = pygame.image.load('susto.png').convert()
            susto = pygame.transform.scale(susto, (tamanho_tela))

            fundo_atual = susto
            tela.blit(fundo_atual,(0, 0))
            pygame.display.update()
            sleep(1)
            return('perdeu')
            break   

        
#=================================================================================================================================
#        

def forca_criado(tela,fundo_atual,tamanho_tela):
    import pygame 
    from shlex import join 
    from pygame import KEYDOWN
    from time import sleep 
   


    forca1 = pygame.image.load('imagens/forca1.png').convert_alpha()
    forca2 = pygame.image.load('imagens/cabeca.png').convert_alpha()
    forca3 = pygame.image.load('imagens/Corpinho.png').convert_alpha()
    forca5 = pygame.image.load('imagens/bracinho_2.png').convert_alpha()
    forca4 = pygame.image.load('imagens/Bracinho.png').convert_alpha()
    forca6 = pygame.image.load('imagens/perna.png').convert_alpha()
    forca7 = pygame.image.load('imagens/aaaaaaaaaaa.png').convert_alpha()
   

    fase = forca1
    

    fonte = pygame.font.Font('fontes/Dogica.ttf',32)
    palavra = 'destrua'
    letras = ['_'] * len (palavra)
    letras_usadas = []
    tentativas = 6

    liga = True
    while liga:
        for event in pygame.event.get():
           if event.type == KEYDOWN:
            #    if event.key == pygame.K_ESCAPE:
                    #liga = False  
                if event.unicode.isalpha():
                    letra = event.unicode.lower()

                    if letra in palavra:
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    
                        for i in range(len(palavra)):
                            if palavra[i] == letra:
                                letras[i]=letra
                    elif letra not in letras_usadas:
                        tentativas -= 1
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    



        

        if tentativas == 6:
            fase = forca1
        elif tentativas == 5:
            fase = forca2    
        elif tentativas == 4:
            fase = forca3
        elif tentativas == 3:
            fase = forca4      
        elif tentativas == 2:
            fase = forca5
        elif tentativas == 1:
            fase = forca6          
        elif tentativas == 0:
            fase = forca7  
              

        tela.blit(fundo_atual,(0, 0))
        
        
        texto = fonte.render(''.join(letras),True,(0,0,0)) 
        tela.blit(fase,(0,200))
        tela.blit(texto,(300,460)) 

       # usadas = fonte.render('usadas:'+','.join(letras_usadas),True,(0,0,0))
      #  tela.blit(usadas,(250,180))

        pygame.display.update()      

        if '_' not in letras:
            texto = fonte.render(''.join(letras),True,(0,0,0)) 
            tela.blit(fase,(0,200))
            tela.blit(texto,(300,460)) 
            pygame.display.update()   
            sleep(2)
            return('venceu')
            break

        if tentativas == 0:
            sleep(2)
            return('perdeu')
            break 

#=================================================================================================================================3

def forca_cama(tela,fundo_atual,tamanho_tela):
    import pygame 
    from shlex import join 
    from pygame import KEYDOWN
    from time import sleep 

    player_deitado = pygame.image.load('imagens/playerdeitado.png').convert_alpha()
    player_deitado = pygame.transform.scale(player_deitado, (50, 30))    


    forca1 = pygame.image.load('imagens/forca1.png').convert_alpha()
    forca2 = pygame.image.load('imagens/cabeca.png').convert_alpha()
    forca3 = pygame.image.load('imagens/Corpinho.png').convert_alpha()
    forca5 = pygame.image.load('imagens/bracinho_2.png').convert_alpha()
    forca4 = pygame.image.load('imagens/Bracinho.png').convert_alpha()
    forca6 = pygame.image.load('imagens/perna.png').convert_alpha()
    forca7 = pygame.image.load('imagens/aaaaaaaaaaa.png').convert_alpha()
   

    fase = forca1
    

    fonte = pygame.font.Font('fontes/Dogica.ttf',32)
    palavra = 'liberte'
    letras = ['_'] * len (palavra)
    letras_usadas = []
    tentativas = 6

    liga = True
    while liga:
        for event in pygame.event.get():
           if event.type == KEYDOWN:
            #    if event.key == pygame.K_ESCAPE:
                    #liga = False  
                if event.unicode.isalpha():
                    letra = event.unicode.lower()

                    if letra in palavra:
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    
                        for i in range(len(palavra)):
                            if palavra[i] == letra:
                                letras[i]=letra
                    elif letra not in letras_usadas:
                        tentativas -= 1
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    



        

        if tentativas == 6:
            fase = forca1
        elif tentativas == 5:
            fase = forca2    
        elif tentativas == 4:
            fase = forca3
        elif tentativas == 3:
            fase = forca4      
        elif tentativas == 2:
            fase = forca5
        elif tentativas == 1:
            fase = forca6          
        elif tentativas == 0:
            fase = forca7  
              

        tela.blit(fundo_atual,(0, 0))
        
        
        texto = fonte.render(''.join(letras),True,(0,0,0)) 
        tela.blit(player_deitado,(580,220))
        tela.blit(fase,(0,200))
        tela.blit(texto,(300,460)) 

       # usadas = fonte.render('usadas:'+','.join(letras_usadas),True,(0,0,0))
      #  tela.blit(usadas,(250,180))

        pygame.display.update()   

        if '_' not in letras :
            tela.blit(fundo_atual,(0, 0))
            
            texto = fonte.render(''.join(letras),True,(0,0,0)) 
            tela.blit(player_deitado,(580,220))
            tela.blit(fase,(0,200))
            tela.blit(texto,(300,460)) 
            pygame.display.update()   
            sleep(2)
            return('venceu')
            break

        if tentativas == 0:
            sleep(2)
            return('perdeu')
            break           

#===================================================================================================

def ultimo (tela,fundo_atual,tamanho_tela):
    import pygame 
    from shlex import join 
    from pygame import KEYDOWN
    from time import sleep   

    pdc_forca = pygame.image.load('parede_jogo/pdp_forca.png').convert_alpha()
    forca1 = pygame.image.load('parede_jogo/1.png').convert_alpha()
    forca2 = pygame.image.load('parede_jogo/2.png').convert_alpha()
    forca3 = pygame.image.load('parede_jogo/3.png').convert_alpha()
    forca4 = pygame.image.load('parede_jogo/4.png').convert_alpha()
    forca5 = pygame.image.load('parede_jogo/5.png').convert_alpha()
    forca6 = pygame.image.load('parede_jogo/6.png').convert_alpha()
    forca7 = pygame.image.load('parede_jogo/7.png').convert_alpha()
   

    fase = forca1
    

    fonte = pygame.font.Font('fontes/Dogica.ttf',32)
    palavra = 'shizuka'
    letras = ['_'] * len (palavra)
    letras_usadas = []
    tentativas = 6

    liga = True
    while liga:
        for event in pygame.event.get():
           if event.type == KEYDOWN:
            #    if event.key == pygame.K_ESCAPE:
                    #liga = False  
                if event.unicode.isalpha():
                    letra = event.unicode.lower()

                    if letra in palavra:
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    
                        for i in range(len(palavra)):
                            if palavra[i] == letra:
                                letras[i]=letra
                    elif letra not in letras_usadas:
                        tentativas -= 1
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    



        

        if tentativas == 6:
            fase = forca1
        elif tentativas == 5:
            fase = forca2    
        elif tentativas == 4:
            fase = forca3
        elif tentativas == 3:
            fase = forca4      
        elif tentativas == 2:
            fase = forca5
        elif tentativas == 1:
            fase = forca6          
        elif tentativas == 0:
            fase = forca7  
              

        #tela.blit(fundo_atual,(0, 0))
        tela.blit(pdc_forca,(0,0))
        
        texto = fonte.render(''.join(letras),True,(0,0,0)) 
        tela.blit(fase,(0,0))
        tela.blit(texto,(400,400)) 

       # usadas = fonte.render('usadas:'+','.join(letras_usadas),True,(0,0,0))
      #  tela.blit(usadas,(250,180))

        pygame.display.update()   

        if '_' not in letras :
            tela.blit(pdc_forca,(0,0))
        
            texto = fonte.render(''.join(letras),True,(0,0,0)) 
            tela.blit(fase,(0,0))
            tela.blit(texto,(400,400))
            pygame.display.update()   
            sleep(2)
            return('venceu')
            break

        if tentativas == 0:
            sleep(2)
            return('perdeu')
            break         

#===================================================================================================================

def teia_jogo(tela,fundo_atual,tamanho_tela):
            
    import pygame 
    from shlex import join 
    from pygame import KEYDOWN
    from time import sleep   

  
    forca1 = pygame.image.load('parede_jogo/aranha_1.png').convert_alpha()
    forca1 = pygame.transform.scale(forca1,tamanho_tela)

    forca2 = pygame.image.load('parede_jogo/aranha_2.png').convert_alpha()
    forca2 = pygame.transform.scale(forca2,tamanho_tela)

    forca3 = pygame.image.load('parede_jogo/aranha_3.png').convert_alpha()
    forca3 = pygame.transform.scale(forca3,tamanho_tela)

    forca4 = pygame.image.load('parede_jogo/aranha_4.png').convert_alpha()
    forca4 = pygame.transform.scale(forca4,tamanho_tela)

    forca5 = pygame.image.load('parede_jogo/aranha_5.png').convert_alpha()
    forca5 = pygame.transform.scale(forca5,tamanho_tela)

    forca6 = pygame.image.load('parede_jogo/aranha_6.png').convert_alpha()
    forca6 = pygame.transform.scale(forca6,tamanho_tela)

    forca7 = pygame.image.load('parede_jogo/aranha_7.png').convert_alpha()
    forca7 = pygame.transform.scale(forca7,tamanho_tela)
   

    fase = forca1
    

    fonte = pygame.font.Font('fontes/Dogica.ttf',32)
    palavra = 'terubozu'
    letras = ['_'] * len (palavra)
    letras_usadas = []
    tentativas = 6

    liga = True
    while liga:
        for event in pygame.event.get():
           if event.type == KEYDOWN:
            #    if event.key == pygame.K_ESCAPE:
                    #liga = False  
                if event.unicode.isalpha():
                    letra = event.unicode.lower()

                    if letra in palavra:
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    
                        for i in range(len(palavra)):
                            if palavra[i] == letra:
                                letras[i]=letra
                    elif letra not in letras_usadas:
                        tentativas -= 1
                        if letra not in letras_usadas:
                            letras_usadas.append(letra)    



        

        if tentativas == 6:
            fase = forca1
        elif tentativas == 5:
            fase = forca2    
        elif tentativas == 4:
            fase = forca3
        elif tentativas == 3:
            fase = forca4      
        elif tentativas == 2:
            fase = forca5
        elif tentativas == 1:
            fase = forca6          
        elif tentativas == 0:
            fase = forca7  
              

        #tela.blit(fundo_atual,(0, 0))
        
        
        texto = fonte.render(''.join(letras),True,(0,0,0)) 
        tela.blit(fase,(0,0))
        tela.blit(texto,(350,400)) 

       # usadas = fonte.render('usadas:'+','.join(letras_usadas),True,(0,0,0))
      #  tela.blit(usadas,(250,180))

        pygame.display.update()   

        if '_' not in letras :
            
        
            texto = fonte.render(''.join(letras),True,(0,0,0)) 
            tela.blit(fase,(0,0))
            tela.blit(texto,(350,400))
            pygame.display.update()   
            sleep(2)
            return('venceu')
            break

        if tentativas == 0:
            sleep(2)
            return('perdeu')
            break                    