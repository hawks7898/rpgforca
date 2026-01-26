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
    palavra = 'MARTELO'
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
                    letra = event.unicode.upper()
                    if letra not in letras_usadas:
                        letras_usadas.append(letra)    
                    if letra in palavra:
                        for i in range(len(palavra)):
                            if palavra[i] == letra:
                                letras[i]=letra
                    else:
                        tentativas -= 1 


        

        if '_' not in letras:
            return('venceu')
            break

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
        
        #pygame.draw.line(tela,(0,0,0), (100,100), (100,300), 4)
        #pygame.draw.line(tela,(0,0,0), (100,100), (200,100), 4)
        texto = fonte.render(''.join(letras),True,(0,0,0)) 
        tela.blit(fase,(90,100))
        tela.blit(texto,(400,360)) 

       # usadas = fonte.render('usadas:'+','.join(letras_usadas),True,(0,0,0))
        #tela.blit(usadas,(250,180))

        pygame.display.update()      
        if tentativas == 0:
            sleep(5)
            susto = pygame.image.load('susto.png').convert()
            susto = pygame.transform.scale(susto, (tamanho_tela))

            fundo_atual = susto
            tela.blit(fundo_atual,(0, 0))
            pygame.display.update()
            sleep(1)
            return('perdeu')
            break   
        

                                        

