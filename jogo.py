import pygame
from time import sleep
from funcoes import inicializacao, game_loop


estado = inicializacao()
sleep(1) #TEMPO PARA CARREGAR 
game_loop(estado)
pygame.quit()
                       



