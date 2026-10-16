
## INICIANDO O JOGO
def inicializacao():

    pygame.init()

    `WINDOW E CLOCK`
    window = pygame.display.set_mode(TAMANHO_TELA)
    titulo = 'Navinha'
    pygame.display.set_caption(titulo)
    

## LOADING DE IMAGES
imagem = pygame.image.load('caminho')
image_transformada = pygame.transform.scale(image, TAMANHO)

## FONTES E TEXTO
fonte = pygame.font.Font('caminho, 12) ou  fonte = pygame.font.SysFont(None, TAMANHO) `None é para usar a fonte padrao`

## SONS E MUSICA
### Sons podem ser tocados ao mesmo tempo, músicas não, pois so existe uma principal
som_tiro = pygame.mixer.Sound('caminho') `carrega som`

pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg') `Carrega musica`
pygame.mixer.music.play()

## PARA DESENHAR NA TELA
window : pygame.Surface = estado['window'] `setando a window`
window.blit(image, posicao) `desenha uma imagem em cima de outra imagem

`Para desenhar varias imagens`
window.blits( (image, posicao)for posicao in posicoes )


## SETANDO FPS
fonte = pygame.font.SysFont(None, TAMANHO)
fps = int(estado['clock'].get_fps())
fps = fonte.render(f'FPS {fps}', True, VERMELHO)
window.blit(fps, posicao)

## ATUALIZA ESTADO

    def atualiza_eventos(estado):
        for event in pygame.event.get():
            # SE SAIR DO JOGO OU APERTAR Q
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    estado['assets']['som_tiro'].play()

        return True

## GAME LOOP
    def game_loop(estado):
        clock = estado['clock']
        while atualiza_eventos(estado):
            desenha(estado)
            clock.tick(60)

## CLASSES
    import pygame

    class Circulo(pygame.sprite.Sprite):
        def __init__(self, cor_inicial, x, y, raio, cor_real):
            super().__init__()

            # SPRITE PRECISA DE self.image e self.rect
    metodo update serve para usar o Group.update
    
    ### METODOS IMPORTANTES DO SPRITE
        self.image = pygame.Surface(posicao, cor)
        self.rect = self.image.get_rect() `ṕode se passar parametros de rect`

        pygame.Surface().get_rect
        pygame.Surface().get_mask
        pygame.Surface().get_height
        pygame.Surface().get_width

        circulo.rect.collidepoint(event.pos) -> bool
        pygame.Rect().collidepoint -> bool
        pygame.Rect().colliderect -> bool

        colisoes = pygame.sprite.spritecollide(sprite, spriteGroup, dokill=False)


    

