import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ejemplo de Pygame")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Configuración inicial del círculo
circle_x, circle_y = WIDTH // 2, HEIGHT // 2
circle_radius = 30
circle_speed = 5

# Reloj para controlar la tasa de fotogramas
clock = pygame.time.Clock()

# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        circle_y -= circle_speed
    if keys[pygame.K_DOWN]:
        circle_y += circle_speed
    if keys[pygame.K_LEFT]:
        circle_x -= circle_speed
    if keys[pygame.K_RIGHT]:
        circle_x += circle_speed

    # Lógica para evitar que el círculo salga de la pantalla
    circle_x = max(circle_radius, min(WIDTH - circle_radius, circle_x))
    circle_y = max(circle_radius, min(HEIGHT - circle_radius, circle_y))

    # Dibujar todo
    screen.fill(WHITE)  # Fondo blanco
    pygame.draw.circle(screen, RED, (circle_x, circle_y), circle_radius)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la tasa de fotogramas
    clock.tick(60)
