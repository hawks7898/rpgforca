import pygame 
from quarto import quarto

pygame.init()
pygame.display.set_caption('casa das palavras')

#========================================================================================================================================
game_variaveis ={
    'x': 500,
    'y': 166,
    'fundo_atual': '',
    'sala': 'quarto',
    'estado':  'casa',
    'vida': 6,
    'armario': 'fechado',
    'bau': 'fechado',
    'jogou': False,
    'criado_ab': 'fechado',
    'criado_ab_jogo': 'fechado',
    'ritual': False,
    'jogou_cama': False,
    'jogou_criado': False,
    'jogou_parede': False,
    'jogou_teia': False,
    'selos_quebrados': 0,
    'fase1': False,
}

#====================================================================================================================================

tamanho_tela = (800,700)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('casa das palavras')

quarto(tamanho_tela, tela,game_variaveis)

