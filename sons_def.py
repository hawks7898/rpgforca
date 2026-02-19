import pygame
def fundo ():
    import pygame

    pygame.mixer.music.load('sons/fundosom.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

def porta():
    import pygame

    pygame.mixer.music.load('sons/Porta.ogg')
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(1.0)

def interaçao():
    import pygame



    pygame.mixer.music.load('sons/sla.ogg')
    pygame.mixer.music.play(1)    

def trancado():    
   som_trancado = pygame.mixer.Sound('sons/trancado.ogg')
   som_trancado.play()

def criado_trancado():    
   som_trancado2 = pygame.mixer.Sound('sons/Criado_trancado.ogg')
   som_trancado2.play()   