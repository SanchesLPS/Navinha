import pygame
from constantes import *


def inicializacao():
    pygame.init()

    tamanho_tela = (900,600)
    window = pygame.display.set_mode(tamanho_tela)
    titulo = 'Navinha'
    pygame.display.set_caption(titulo)

    # CARREGA AS IMAGENS
    nave = pygame.image.load('assets/img/playerShip1_orange.png')
    nave = pygame.transform.scale(nave, (60,60))
    image_fundo = pygame.image.load('assets/img/starfield.png')
    image_fundo = pygame.transform.scale(image_fundo, tamanho_tela)

    imagens = {'nave' : nave,
               'fundo' : image_fundo
               }
    

    return window, imagens

def desenha(window : pygame.Surface, imagens : dict[str, pygame.Surface]):
    window.blit(imagens['fundo'], (0,0))

    pos_nave = (window.get_width()//2 - imagens['nave'].get_width()//2,
                window.get_height() - imagens['nave'].get_height())
    window.blit(imagens['nave'], pos_nave)

    pygame.display.update()



def recebe_eventos():
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            return False

    return True



def game_loop(window : pygame.Surface, imagens : dict[str, pygame.Surface]):
    while True:
        if not recebe_eventos():
            return

        desenha(window, imagens)

window, imagens = inicializacao()

game_loop(window, imagens)
pygame.quit()
                       



