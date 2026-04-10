# 02_dodge.py
# Dodge the falling objects!
# Move left/right with arrow keys. Don't get hit!

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge!")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Colors
BG      = pygame.Color("midnightblue")
PLAYER_C= pygame.Color("deepskyblue")
ENEMY_C = pygame.Color("tomato")
WHITE   = pygame.Color("white")
RED     = pygame.Color("red")

# Player
pl_w, pl_h = 50, 50
pl_x = WIDTH // 2 - pl_w // 2
pl_y = HEIGHT - 80
pl_speed = 6

# Falling objects
def new_enemy():
    return {
        "x": random.randint(20, WIDTH - 40),
        "y": -30,
        "w": random.randint(20, 40),
        "h": random.randint(20, 40),
        "speed": random.uniform(3, 6)
    }

enemies = [new_enemy() for _ in range(4)]
score = 0
survived_frames = 0

running = True
while running:
    clock.tick(60)
    survived_frames += 1
    score = survived_frames // 60  # score = seconds survived

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pl_x = max(0, pl_x - pl_speed)
    if keys[pygame.K_RIGHT]:
        pl_x = min(WIDTH - pl_w, pl_x + pl_speed)

    # Move enemies
    for e in enemies:
        e["y"] += e["speed"]
        if e["y"] > HEIGHT:
            e.update(new_enemy())
            e["speed"] += 0.1  # gradually gets harder

    # Collision check
    player_rect = pygame.Rect(pl_x, pl_y, pl_w, pl_h)
    for e in enemies:
        enemy_rect = pygame.Rect(e["x"], e["y"], e["w"], e["h"])
        if player_rect.colliderect(enemy_rect):
            running = False

    # Draw
    screen.fill(BG)
    for e in enemies:
        pygame.draw.rect(screen, ENEMY_C,
                         (e["x"], e["y"], e["w"], e["h"]), border_radius=5)
    pygame.draw.rect(screen, PLAYER_C,
                     (pl_x, pl_y, pl_w, pl_h), border_radius=8)

    score_surf = font.render(f"Time: {score}s", True, WHITE)
    screen.blit(score_surf, (20, 20))
    pygame.display.flip()

# Game Over
screen.fill(BG)
over_surf = font.render(f"You survived {score} seconds!", True, RED)
screen.blit(over_surf, (WIDTH // 2 - over_surf.get_width() // 2, HEIGHT // 2 - 30))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
