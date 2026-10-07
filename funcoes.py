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
    def carrega_assets() -> dict[str , pygame.Surface]:
        nave = pygame.image.load('assets/img/playerShip1_orange.png')
        nave = pygame.transform.scale(nave, (60,60))

        image_fundo = pygame.image.load('assets/img/starfield.png')
        image_fundo = pygame.transform.scale(image_fundo, TAMANHO_TELA)

        fonte = pygame.font.Font('assets/font/PressStart2P.ttf', 12)
        return {
            'nave' : nave,
            'fundo' : image_fundo,
            'fonte' : fonte

        }

    assets = carrega_assets()

    # POSICAO INICIAL DA NAVE
    pos_nave = [TAMANHO_TELA[0]//2 - assets['nave'].get_width()//2,
                    TAMANHO_TELA[1] - assets['nave'].get_height()]

    # QUANTIDADE INICIAL DE VIDA
    vidas = 3

    # ESTADO
    return {
        'window' : window,
        'assets' : assets,
        'estrelas' : estrelas,
        'pos_nave' : pos_nave,
        'vidas' : vidas
        
    }

def desenha(estado):
    # NOMEIA AS VARIAVEIS
    window : pygame.Surface = estado['window']
    assets : dict[str, pygame.Surface | pygame.font.Font]= estado['assets']
    estrelas : tuple[ dict[str, tuple[int] | int ] ] = estado['estrelas']
    pos_nave = estado['pos_nave']
    
    # PRIMEIRO DESENHA O FUNDO
    window.blit(assets['fundo'], (0,0))

    # DESENHA ESTRELAS
    for estrela in estrelas:
        pygame.draw.circle(window, estrela['cor'], estrela['pos_circulo'], estrela['raio'])

    # DESENHA FPS
    fps = pygame.time.Clock().get_fps()
    fps = assets['fonte'].render(f'FPS {fps}', True, VERMELHO)
    window.blit(fps, (TAMANHO_TELA[0]-100, TAMANHO_TELA[1]-30))

    # DESENHA JOGADOR
    window.blit(assets['nave'], pos_nave)

    # DESENHA CORACOES
    coracoes = assets['fonte'].render(chr(9829) * estado['vidas'], True, VERMELHO )
    window.blit(coracoes, (0,0))

    pygame.display.update()

def atualiza_estado(estado):
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_a]:
        print("esquerda")

    if teclas[pygame.K_d]:
        print("direita")

    if teclas[pygame.K_w]:
        print("cima")

    if teclas[pygame.K_s]:
        print("baixo")

def recebe_eventos():
    for event in pygame.event.get():
        # SE SAIR DO JOGO OU APERTAR Q
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            return False
        

    return True



def game_loop(estado):
    clock = pygame.time.Clock()
    while recebe_eventos():
        atualiza_estado(estado)
        desenha(estado)
        clock.tick(60)