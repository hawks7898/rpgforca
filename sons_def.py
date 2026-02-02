
def fundo ():
    import pygame

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load('sons/fundosom.ogg')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)

def porta():
    import pygame

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load('sons/Porta.ogg')
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(1.0)

def interaçao():
    import pygame

    pygame.init()
    pygame.mixer.init()

    pygame.mixer.music.load('sons/sla.ogg')
    pygame.mixer.music.play(1)    
        