import pygame
from random import randint
from constantes import *

def inicializacao():
    pygame.init()

    # WINDOW E CLOCK
    window = pygame.display.set_mode(TAMANHO_TELA)
    titulo = 'Navinha'
    pygame.display.set_caption(titulo)
    clock = pygame.time.Clock()


    # CARREGA ESTRELAS 
    def carrega_estrelas() :
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
    def carrega_assets() -> dict[str , pygame.Surface | pygame.font.Font]:
        nave = pygame.image.load('assets/img/playerShip1_orange.png')
        nave = pygame.transform.scale(nave, TAMANHO_NAVE)

        image_fundo = pygame.image.load('assets/img/starfield.png')
        image_fundo = pygame.transform.scale(image_fundo, TAMANHO_TELA)

        fonte = pygame.font.Font('assets/font/PressStart2P.ttf', 12)
        return {
            'nave' : nave,
            'fundo' : image_fundo,
            'fonte' : fonte

        }

    assets = carrega_assets()

    # POSICAO INICIAL DA NAVE E VELOCIDADE DA NAVE
    pos_nave = [TAMANHO_TELA[0]//2 - TAMANHO_NAVE[0],
                    TAMANHO_TELA[1] - TAMANHO_NAVE[1]]
    print(assets['nave'].get_width())

    velocidade_nave = [0,0]

    # QUANTIDADE INICIAL DE VIDA
    vidas = 3

    # MOVIMENTOS POSSIVEIS
    movimentos = (pygame.K_w, pygame.K_UP , pygame.K_d, pygame.K_RIGHT, pygame.K_s, pygame.K_DOWN , pygame.K_a, pygame.K_LEFT )


    # ESTADO
    return {
        'window' : window,
        'assets' : assets,
        'estrelas' : estrelas,
        'pos_nave' : pos_nave,
        'velocidade_nave' : velocidade_nave,
        'vidas' : vidas,
        'clock' : clock,
        'movimentos' : movimentos
        
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
    fps = int(estado['clock'].get_fps())
    fps = assets['fonte'].render(f'FPS {fps}', True, VERMELHO)
    window.blit(fps, (TAMANHO_TELA[0]-100, TAMANHO_TELA[1]-30))

    # DESENHA JOGADOR
    window.blit(assets['nave'], pos_nave)

    # DESENHA CORACOES
    coracoes = assets['fonte'].render(chr(9829) * estado['vidas'], True, VERMELHO )
    window.blit(coracoes, (0,0))

    pygame.display.update()


def atualiza_posicao(estado):
    teclas = pygame.key.get_pressed()
    velocidade = 4 
    dx, dy = 0, 0

    if teclas[pygame.K_w] or teclas[pygame.K_UP]:
        dy = -velocidade
    if teclas[pygame.K_s] or teclas[pygame.K_DOWN]:
        dy = velocidade
    if teclas[pygame.K_a] or teclas[pygame.K_LEFT]:
        dx = -velocidade
    if teclas[pygame.K_d] or teclas[pygame.K_RIGHT]:
        dx = velocidade

    novo_x = estado['pos_nave'][0] + dx
    novo_y = estado['pos_nave'][1] + dy

    if novo_x < 0:
        novo_x = 0
    elif novo_x > TAMANHO_TELA[0] - TAMANHO_NAVE[0]:
        novo_x = TAMANHO_TELA[0] - TAMANHO_NAVE[0]

    if novo_y < 0:
        novo_y = 0
    elif novo_y > TAMANHO_TELA[1] - TAMANHO_NAVE[1]:
        novo_y = TAMANHO_TELA[1] - TAMANHO_NAVE[1]

    estado['pos_nave'][0] = novo_x
    estado['pos_nave'][1] = novo_y
    
def atualiza_estado(estado):
        atualiza_posicao(estado)
        # atualiza_posicao_meteoros(estado)

        # 2. Checagem de "Eventos de Jogo" (Colisões afins)
        # if nave_colidiu_com_meteoro(estado):
        #     estado['vidas'] -= 1
        #     if estado['vidas'] <= 0:
        #         estado['tela_atual'] = 'GAME_OVER' # Mutação do estado lógico

    # elif estado['tela_atual'] == 'GAME_OVER':
        # Congela a física da nave. 
        # Aqui pode entrar lógica de contagem de tempo para voltar ao menu.
        pass

def atualiza_eventos(estado):
    for event in pygame.event.get():
        # SE SAIR DO JOGO OU APERTAR Q
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            return False



    return True



def game_loop(estado):
    clock = estado['clock']
    while atualiza_eventos(estado):
        atualiza_estado(estado)
        desenha(estado)
        clock.tick(90)