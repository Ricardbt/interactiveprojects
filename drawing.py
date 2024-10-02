import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (155, 255, 255)
DRAW_COLOR = (0, 0, 0)
LINE_WIDTH = 4

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Drawing Program")

# Initialize drawing variables
drawing = False
last_pos = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
                last_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                current_pos = event.pos
                if last_pos is not None:
                    pygame.draw.line(screen, DRAW_COLOR, last_pos, current_pos, LINE_WIDTH)
                last_pos = current_pos

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
