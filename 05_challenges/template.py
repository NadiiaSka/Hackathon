# template.py
# Blank pygame template — start your project here!

import pygame

# ---- SETUP ----
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")   # Give your game a name!

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# ---- COLORS ----
BG     = pygame.Color("midnightblue")
WHITE  = pygame.Color("white")
RED    = pygame.Color("crimson")
GREEN  = pygame.Color("limegreen")
BLUE   = pygame.Color("royalblue")
YELLOW = pygame.Color("gold")

# ---- YOUR VARIABLES ----
# Add your game variables here, for example:
# player_x = WIDTH // 2
# player_y = HEIGHT // 2
# score = 0

# ---- MAIN GAME LOOP ----
running = True
while running:
    clock.tick(60)   # 60 frames per second

    # -- EVENTS --
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add keyboard/mouse events here

    # -- UPDATE --
    # Move things, check collisions, update score, etc.

    # -- DRAW --
    screen.fill(BG)
    # Draw your stuff here

    pygame.display.flip()

pygame.quit()
