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
pos_onda = 0  # Posição inicial da onda

# Parâmetros do jogador
pos_x = largura // 2
pos_y = altura - 50
velocidade_jogador = 5
raio_jogador = 15
pulo = False
tempo_pulo = 0

# Pontuação e dificuldade
pontuacao = 0
nivel = 1

# Configurações do pulo
altura_pulo = 100
velocidade_pulo = 10
gravidade = 2

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
    if teclas[pygame.K_UP] and not pulo:
        pulo = True
        tempo_pulo = 0

    # Atualização da posição do pulo
    if pulo:
        pos_y -= velocidade_pulo
        tempo_pulo += 1
        if tempo_pulo > 2 * altura_pulo / velocidade_pulo:
            pulo = False
    else:
        if pos_y < altura - 50:
            pos_y += gravidade

    # Atualização da tela
    tela.fill(BRANCO)

    # Atualizar a posição da onda
    pos_onda += velocidade_onda
    if pos_onda > altura:
        pos_onda = -amplitude  # Reseta a posição da onda quando ela sai da tela

    # Desenho das ondas e verificação de colisão
    colidiu = False
    brecha = largura // 2  # Define a brecha no meio da tela
    for x in range(0, largura, 5):
        y = int(pos_onda + amplitude * np.sin(frequencia * x))
        pygame.draw.circle(tela, PRETO, (x, y), 5)
        if abs(pos_x - x) < 5 and abs(pos_y - y) < 5 and x != brecha:
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