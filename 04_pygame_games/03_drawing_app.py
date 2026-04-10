# 03_drawing_app.py
# A simple drawing app!
# - Hold left mouse button to draw
# - Press C to clear the canvas
# - Press 1-7 to change color
# - Press +/- to change brush size

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

PALETTE = [
    pygame.Color("white"),      # 1 white
    pygame.Color("tomato"),     # 2 red
    pygame.Color("orange"),     # 3 orange
    pygame.Color("gold"),       # 4 yellow
    pygame.Color("limegreen"),  # 5 green
    pygame.Color("dodgerblue"), # 6 blue
    pygame.Color("mediumorchid"), # 7 purple
]

BG = pygame.Color("dimgray")
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill(BG)

current_color = PALETTE[0]
brush_size = 8

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                canvas.fill(BG)   # Clear
            # Number keys 1-7 change color
            for i, key in enumerate([pygame.K_1, pygame.K_2, pygame.K_3,
                                      pygame.K_4, pygame.K_5, pygame.K_6,
                                      pygame.K_7]):
                if event.key == key:
                    current_color = PALETTE[i]
            if event.key in (pygame.K_EQUALS, pygame.K_PLUS):
                brush_size = min(60, brush_size + 2)
            if event.key == pygame.K_MINUS:
                brush_size = max(2, brush_size - 2)

    # Draw while mouse button is held
    if pygame.mouse.get_pressed()[0]:
        mx, my = pygame.mouse.get_pos()
        pygame.draw.circle(canvas, current_color, (mx, my), brush_size)

    screen.blit(canvas, (0, 0))

    # HUD
    tip = font.render(
        f"Color: 1-7 | Size: {brush_size} (+/-) | Clear: C",
        True, pygame.Color("gainsboro")
    )
    screen.blit(tip, (10, 10))

    # Color swatches
    for i, col in enumerate(PALETTE):
        rect = pygame.Rect(10 + i * 36, HEIGHT - 44, 30, 30)
        pygame.draw.rect(screen, col, rect, border_radius=5)
        if col == current_color:
            pygame.draw.rect(screen, pygame.Color("white"), rect, 3, border_radius=5)

    pygame.display.flip()

pygame.quit()
