# 02_keyboard.py
# Move a shape around with the arrow keys!

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move with Arrow Keys")

clock = pygame.time.Clock()

# Player square
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_size = 50
player_color = pygame.Color("deepskyblue")
SPEED = 5

BG = pygame.Color("midnightblue")

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Read which keys are held down
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= SPEED
    if keys[pygame.K_RIGHT]:
        player_x += SPEED
    if keys[pygame.K_UP]:
        player_y -= SPEED
    if keys[pygame.K_DOWN]:
        player_y += SPEED

    # Keep player inside the window
    player_x = max(0, min(WIDTH - player_size, player_x))
    player_y = max(0, min(HEIGHT - player_size, player_y))

    screen.fill(BG)
    pygame.draw.rect(screen, player_color,
                     (player_x, player_y, player_size, player_size),
                     border_radius=8)
    pygame.display.flip()

pygame.quit()
