import pygame
from random import randint
from constantes import *

def inicializacao():
    pygame.init()

    # WINDOW
    
    window = pygame.display.set_mode(TAMANHO_TELA)
    titulo = 'Navinha'
    pygame.display.set_caption(titulo)

    # CARREGA ESTRELAS 
    def carrega_estrelas() -> tuple[ dict[str, tuple[int] | int ] ]:
        qtd_circulos = 20
        cor_circulo = BRANCO

        # GERA POSICOES ALEATORIAS
        pos_circulos = tuple( 
            (randint(0, TAMANHO_TELA[0]), randint(0, TAMANHO_TELA[1])) for _ in range(qtd_circulos)
        )

        # GERA RAIOS ALEATÓRIOS DE 1 À 4
        raio_circulos =  tuple( randint(1,4) for _ in range(qtd_circulos))
        return tuple({'cor' : cor_circulo, 'pos_circulo' : pos_circulo, 'raio' : raio_circulo} for pos_circulo, raio_circulo in zip(pos_circulos, raio_circulos))

    estrelas = carrega_estrelas()

    # CARREGA AS IMAGENS
    def carrega_imagens() -> dict[str , pygame.Surface]:
        nave = pygame.image.load('assets/img/playerShip1_orange.png')
        nave = pygame.transform.scale(nave, (60,60))
        image_fundo = pygame.image.load('assets/img/starfield.png')
        image_fundo = pygame.transform.scale(image_fundo, TAMANHO_TELA)
        return {
            'nave' : nave,
            'fundo' : image_fundo
        }

    assets = carrega_imagens()

    return {
        'window' : window,
        'assets' : assets,
        'estrelas' : estrelas
        
    }

def desenha(estado):
    # NOMEIA AS VARIAVEIS
    window = estado['window']
    assets = estado['assets']
    estrelas : tuple[ dict[str, tuple[int] | int ] ] = estado['estrelas']
    
    # PRIMEIRO DESENHA O FUNDO
    window.blit(assets['fundo'], (0,0))

    # DESENHA ESTRELAS
    for estrela in estrelas:
        pygame.draw.circle(window, estrela['cor'], estrela['pos_circulo'], estrela['raio'])

    pos_nave = (window.get_width()//2 - assets['nave'].get_width()//2,
                window.get_height() - assets['nave'].get_height())
    window.blit(assets['nave'], pos_nave)

    pygame.display.update()



def recebe_eventos():
    for event in pygame.event.get():
        
        # ----- Verifica consequências
        if event.type == pygame.QUIT or event.type == 769:
            return False

    return True



def game_loop(estado):
    while True:
        if not recebe_eventos():
            return

        desenha(estado)