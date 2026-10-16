import pygame
from time import sleep
class Circulo(pygame.sprite.Sprite):
    def __init__(self, cor_inicial, x, y, raio, cor_real):
        super().__init__()
        self.cor_inicial = cor_inicial
        self.raio = raio
        self.cor_real = cor_real
        self.revelado = False
        diametro = raio * 2

        self.image = pygame.Surface((diametro, diametro), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.desenha()

    def desenha(self):
        cor = self.cor_real if not self.revelado else self.cor_inicial
        self.image.fill((0, 0, 0, 0))  # Limpa a surface com transparência
        pygame.draw.circle(self.image, cor, (self.raio, self.raio), self.raio)

    def update(self):
        self.revelado = not self.revelado

        

