import pygame
import numpy as np

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Evite as Ondas")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

# Parâmetros da onda
frequencia = 0.02
amplitude = 50
velocidade_onda = 2

# Parâmetros do jogador
pos_x = largura // 2
pos_y = altura - 50  # Posição inicial redefinida
velocidade_jogador = 5
raio_jogador = 15

# Pontuação e dificuldade
pontuacao = 0
nivel = 1
velocidade_onda_inicial = 2

# Loop principal do jogo
rodando = True
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        pos_x -= velocidade_jogador
    if teclas[pygame.K_RIGHT]:
        pos_x += velocidade_jogador
    if teclas[pygame.K_UP]:
        pos_y -= velocidade_jogador
    if teclas[pygame.K_DOWN]:
        pos_y += velocidade_jogador

    # Atualização da tela
    tela.fill(BRANCO)

    # Desenho das ondas e verificação de colisão
    colidiu = False
    for x in range(0, largura, 5):
        y = int(altura / 2 + amplitude * np.sin(frequencia * (x + pygame.time.get_ticks() * velocidade_onda)))
        pygame.draw.circle(tela, PRETO, (x, y), 5)
        if abs(pos_x - x) < 5 and abs(pos_y - y) < 5:
            colidiu = True

    # Verificação de colisão
    if colidiu:
        rodando = False
    else:
        pontuacao += 1
        if pontuacao % 100 == 0:
            nivel += 1
            velocidade_onda += 0.5

    # Desenho do jogador
    pygame.draw.circle(tela, VERMELHO, (pos_x, pos_y), raio_jogador)

    # Exibição da pontuação e nível
    fonte = pygame.font.SysFont(None, 36)
    texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, PRETO)
    texto_nivel = fonte.render(f'Nível: {nivel}', True, PRETO)
    tela.blit(texto_pontuacao, (10, 10))
    tela.blit(texto_nivel, (10, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# Este é um exemplo básico, mas você pode expandi-lo adicionando mais funcionalidades, como pontuação, níveis de dificuldade, e efeitos sonoros.