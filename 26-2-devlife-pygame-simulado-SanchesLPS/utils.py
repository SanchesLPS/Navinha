import random


# Você não precisa entender o que está acontecendo aqui
def hsv2rgb(h, s, v):
    '''
    Converte uma cor no formato HSV (Hue, Saturation, Value) 
    para RGB (Red, Green, Blue).
    '''
    M = 255 * v
    m = M * (1 - s)
    z = (M - m) * (1 - abs((h / 60) % 2 - 1))

    if 0 <= h < 60:
        r = M
        g = z + m
        b = m
    elif 60 <= h < 120:
        r = z + m
        g = M
        b = m
    elif 120 <= h < 180:
        r = m
        g = M
        b = z + m
    elif 180 <= h < 240:
        r = m
        g = z + m
        b = M
    elif 240 <= h < 300:
        r = z + m
        g = m
        b = M
    elif 300 <= h < 360:
        r = M
        g = m
        b = z + m
    
    return int(r), int(g), int(b)


# Você não precisa entender o que está acontecendo aqui
def cria_tabuleiro(n=2):
    '''
    Cria um tabuleiro de jogo da memória com n linhas e n colunas.
    Cada elemento do tabuleiro é uma tupla de 3 inteiros que representam
    uma cor no formato RGB (Red, Green, Blue).

    As cores são geradas aleatoriamente, mas garantindo que cada cor
    aparece exatamente duas vezes no tabuleiro.

    RESTRIÇÃO: n deve ser par.

    Exemplos: 
    
    cria_tabuleiro(2) -> [
        [(255, 0, 0), (0, 255, 0)], 
        [(0, 255, 0), (255, 0, 0)],
    ]

    cria_tabuleiro(4) -> [
        [(40, 204, 81), (122, 40, 204), (204, 40, 40), (40, 204, 204)], 
        [(40, 204, 81), (40, 81, 204), (204, 163, 40), (204, 40, 163)], 
        [(204, 40, 163), (40, 204, 204), (122, 204, 40), (40, 81, 204)], 
        [(204, 40, 40), (204, 163, 40), (122, 40, 204), (122, 204, 40)],
    ]
    '''
    if n % 2 == 1:
        raise RuntimeError('n deve ser par')
    
    total_cores = n ** 2 // 2
    cores = [hsv2rgb(360 / total_cores * i, 0.8, 0.8) for i in range(total_cores)]
    cores = cores + cores
    random.shuffle(cores)

    tabuleiro = [cores[n*i:n*(i+1)] for i in range(n)]
    return tabuleiro
