import pygame 
from quarto import quarto
from corredor import corredor

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
    #itens========================
    'item_caneta': 0,
    'item_boneca': 0,
    'item_chave_boneca': 0,
    'item_chave_saida': 0,
    'pegou_c_s': False,
    'pegou_c_b': False,
}

#====================================================================================================================================

pygame.init()
pygame.mixer.init()

onde = ''

tamanho_tela = (800,700)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption('casa das palavras')
while True:

    if not game_variaveis['fase1'] or onde == 'quarto': 
        onde = quarto(tamanho_tela, tela,game_variaveis)
    if onde == 'corredor':
        onde = corredor(tamanho_tela, tela,game_variaveis)


