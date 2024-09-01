import pygame
import pygame_gui
import numpy as np

# Configurações iniciais
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Desenhador de Ondas')

# Configuração do pygame_gui
manager = pygame_gui.UIManager((screen_width, screen_height))

# Criação dos controles
amplitude_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((50, 550), (200, 30)),
    start_value=100,
    value_range=(10, 200),
    manager=manager
)

frequencia_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((300, 550), (200, 30)),
    start_value=2,
    value_range=(0.1, 10),
    manager=manager
)

velocidade_slider = pygame_gui.elements.UIHorizontalSlider(
    relative_rect=pygame.Rect((550, 550), (200, 30)),
    start_value=1,
    value_range=(0.1, 5),
    manager=manager
)

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Parâmetros da onda
amplitude = amplitude_slider.get_current_value()
frequencia = frequencia_slider.get_current_value()
velocidade = velocidade_slider.get_current_value()
tempo = 0

def desenhar_ondas():
    global tempo
    comprimento = screen_width
    pontos = []
    para = 2 * np.pi * frequencia / comprimento

    for x in range(comprimento):
        y = amplitude * np.sin(para * x + tempo) + screen_height // 2
        pontos.append((x, int(y)))

    pygame.draw.lines(screen, BLUE, False, pontos, 2)

# Função principal do jogo
def game_loop():
    global amplitude, frequencia, velocidade, tempo
    clock = pygame.time.Clock()
    running = True
    while running:
        time_delta = clock.tick(60) / 1000.0  # Tempo em segundos desde o último frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            manager.process_events(event)
        
        # Atualiza os valores dos parâmetros
        amplitude = amplitude_slider.get_current_value()
        frequencia = frequencia_slider.get_current_value()
        velocidade = velocidade_slider.get_current_value()
        
        tempo += velocidade * time_delta
        
        # Atualiza a interface
        manager.update(time_delta)

        # Desenha o fundo e as ondas
        screen.fill(WHITE)
        desenhar_ondas()
        manager.draw_ui(screen)

        pygame.display.flip()
    
    pygame.quit()

game_loop()