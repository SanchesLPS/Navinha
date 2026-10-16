import pygame
from random import randint
import math
from time import sleep

from utils import cria_tabuleiro
from classes import Circulo

def cria_circulos(window):
  tabuleiro = cria_tabuleiro(4)
  circulos = pygame.sprite.Group()

  raio = 40
  espacamento = 30
  cor_inicial = (128, 128, 128)

  largura_tela = window.get_width()
  altura_tela = window.get_height()

  n_linhas = len(tabuleiro)
  n_colunas = len(tabuleiro[0])

  diametro = raio * 2

  largura_total = (n_colunas * diametro) + ((n_colunas - 1) * espacamento)
  altura_total = (n_linhas * diametro) + ((n_linhas - 1) * espacamento)

  inicio_x = (largura_tela - largura_total) // 2
  inicio_y = (altura_tela - altura_total) // 2

  for i in range(n_linhas):
    for j in range(n_colunas):
      x = inicio_x + j * (diametro + espacamento)
      y = inicio_y + i * (diametro + espacamento)
      circulos.add(
          Circulo(cor_inicial, x, y, raio, tabuleiro[i][j])
      )
  return circulos

def inicializacao():
    pygame.init()
    window = pygame.display.set_mode((1024,720))

    # CRIA TABULEIRO
    circulos = cria_circulos(window)

    return {
        'clock': pygame.Clock(),
        'window': window,
        'circulos': circulos,
        "primeira_selecao": None,
        "venceu": False
        }

def desenha(estado):
  # NOMEIA AS VARIAVEIS
  window: pygame.Surface = estado["window"]

  # PRIMEIRO DESENHA O FUNDO
  window.fill((0, 0, 0))

  circulos: pygame.sprite.Group = estado["circulos"]
  circulos.draw(window)

  if estado["venceu"]:
    fonte = pygame.font.SysFont(None, 64)
    texto = fonte.render("VOCE GANHOU!", True, (0, 255, 0))
    # Centraliza o texto na tela
    texto_rect = texto.get_rect(
        center=(window.get_width() // 2, window.get_height() // 2)
    )
    window.blit(texto, texto_rect)

  pygame.display.update()

def atualiza_eventos(estado):
    circulos: pygame.sprite.Group = estado["circulos"]
    if len(circulos) == 0:
        estado["venceu"] = True
        
    for event in pygame.event.get():
        # SE SAIR DO JOGO OU APERTAR Q
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            return False

        if event.type == pygame.MOUSEBUTTONDOWN:
            

            for circulo in circulos:
              # Só permite clicar se a peça estiver escondida (não revelada)
              if (
                  circulo.rect.collidepoint(event.pos)
                  and not circulo.revelado
                  and math.dist(event.pos, circulo.rect.center) <= circulo.raio
              ):

                # Revela a peça clicada
                circulo.revelado = True
                circulo.desenha()

                # Se for a PRIMEIRA peça da jogada
                if estado["primeira_selecao"] is None:
                  estado["primeira_selecao"] = circulo

                # Se for a SEGUNDA peça da jogada
                else:
                  primeira = estado["primeira_selecao"]
                  segunda = circulo

                  # Verifica se as cores são iguais
                  if primeira.cor_real == segunda.cor_real:
                    # Remove ambas do grupo para desaparecerem
                    primeira.kill()
                    segunda.kill()
                  else:
                    # Se forem diferentes, esconde ambas novamente
                    segunda.revelado = True
                    segunda.desenha()
                    pygame.display.update()  # Garante que a tela mostra a segunda peça revelada
                    sleep(1)

                    primeira.revelado = False
                    primeira.desenha()
                    segunda.revelado = False
                    segunda.desenha()
                  # Reseta a seleção para a próxima rodada
                  estado["primeira_selecao"] = None

        
    return True


def game_loop(estado):
    clock = estado['clock']
    while atualiza_eventos(estado):
        desenha(estado)
        clock.tick(60)