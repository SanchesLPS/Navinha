import pygame
from constantes import *


def inicilizacao():
    pygame.init()
    window = pygame.display.set_mode((640,480))
    titulo = 'Navinha'
    pygame.display.set_caption(titulo)

    return window

def desenha(window : pygame.Surface):
    window.fill(PRETO)
    pygame.display.update()



def recebe_eventos():
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            return False

    return True



def game_loop(window : pygame.Surface):
    while True:
        if not recebe_eventos():
            return

        desenha(window)

window = inicilizacao()

game_loop(window)

                       



