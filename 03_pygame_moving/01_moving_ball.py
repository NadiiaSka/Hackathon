# 01_moving_ball.py
# A ball that bounces around the screen!

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()

# Ball properties
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_radius = 25
speed_x = 5   # Try changing the speed!
speed_y = 4
color = pygame.Color("tomato")

BG = pygame.Color("midnightblue")

running = True
while running:
    clock.tick(60)  # 60 frames per second

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball
    ball_x += speed_x
    ball_y += speed_y

    # Bounce off the walls
    if ball_x + ball_radius >= WIDTH or ball_x - ball_radius <= 0:
        speed_x = -speed_x
    if ball_y + ball_radius >= HEIGHT or ball_y - ball_radius <= 0:
        speed_y = -speed_y

    screen.fill(BG)
    pygame.draw.circle(screen, color, (ball_x, ball_y), ball_radius)
    pygame.display.flip()

pygame.quit()
