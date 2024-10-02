import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (0, 0, 0)  # Initial background color (black)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Interactive Background")

# Variables
background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
background.fill(BACKGROUND_COLOR)
color = BACKGROUND_COLOR

drawing = False  # To check if the user is drawing

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos
            pygame.draw.circle(background, color, (x, y), 10)

    # Blit the background onto the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
