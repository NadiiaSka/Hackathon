# 01_catch.py
# Catch the falling ball with your paddle!
# Move left/right with the arrow keys.

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Ball!")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

# Colors
BG      = pygame.Color("midnightblue")
BALL_C  = pygame.Color("tomato")
PAD_C   = pygame.Color("deepskyblue")
WHITE   = pygame.Color("white")
RED     = pygame.Color("red")

# Paddle
pad_w, pad_h = 120, 18
pad_x = WIDTH // 2 - pad_w // 2
pad_y = HEIGHT - 50
pad_speed = 7

# Ball
ball_r = 18
ball_x = random.randint(ball_r, WIDTH - ball_r)
ball_y = 0
ball_speed = 4

score = 0
lives = 3

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pad_x = max(0, pad_x - pad_speed)
    if keys[pygame.K_RIGHT]:
        pad_x = min(WIDTH - pad_w, pad_x + pad_speed)

    # Move ball
    ball_y += ball_speed

    # Caught?
    if (pad_y <= ball_y + ball_r <= pad_y + pad_h and
            pad_x <= ball_x <= pad_x + pad_w):
        score += 1
        ball_speed += 0.3   # gets faster each catch!
        ball_x = random.randint(ball_r, WIDTH - ball_r)
        ball_y = 0

    # Missed
    if ball_y - ball_r > HEIGHT:
        lives -= 1
        ball_x = random.randint(ball_r, WIDTH - ball_r)
        ball_y = 0
        if lives <= 0:
            running = False

    # Draw
    screen.fill(BG)
    pygame.draw.circle(screen, BALL_C, (ball_x, int(ball_y)), ball_r)
    pygame.draw.rect(screen, PAD_C, (pad_x, pad_y, pad_w, pad_h), border_radius=8)

    score_surf = font.render(f"Score: {score}   Lives: {lives}", True, WHITE)
    screen.blit(score_surf, (20, 20))
    pygame.display.flip()

# Game Over screen
screen.fill(BG)
over_surf = font.render(f"Game Over!  Score: {score}", True, RED)
screen.blit(over_surf, (WIDTH // 2 - over_surf.get_width() // 2, HEIGHT // 2 - 30))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
