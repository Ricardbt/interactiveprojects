import pygame
import math
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
BACKGROUND_COLOR = (255, 255, 255)
CENTER_X, CENTER_Y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
BOUNCE_RADIUS = 50
START_COLOR = (24, 65, 67)
DOT_RADIUS = 4
SEPARATION = 8  # Separation between dots

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Phyllotaxis of Circles")

# Constants for phyllotaxis
a = 137.5  # Angle between each circle (Golden angle for phyllotaxis)
b = 9  # Scaling factor
n = 3   # Circle index

# Function to convert polar coordinates to Cartesian coordinates
def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the distance from the mouse to the center
    distance_to_center = math.sqrt((mouse_x - CENTER_X)**2 + (mouse_y - CENTER_Y)**2)

    # Calculate the color based on the distance
    color_multiplier = min(1.0, distance_to_center / BOUNCE_RADIUS)
    color_value = [int(start * (1 + color_multiplier)) for start in START_COLOR]

    # If the mouse is within the bouncing radius, modify the position and color of the circles
    if distance_to_center < BOUNCE_RADIUS:
        # Calculate the polar coordinates with an offset
        theta = (n * math.radians(a)) + math.radians(180)
        r = b * math.sqrt(n)
        x, y = polar_to_cartesian(r, theta)

        # Generate a color with a gradient from the start color to white
        color = tuple(color_value)

        # Draw a circle at the calculated position
        pygame.draw.circle(screen, color, (int(x + CENTER_X), int(y + CENTER_Y)), DOT_RADIUS)

        n += 1

    # Update the display less frequently
    pygame.display.flip()

    # Introduce a delay to slow down the frame rate
    time.sleep(0.02)

# Quit Pygame
pygame.quit()
sys.exit()
