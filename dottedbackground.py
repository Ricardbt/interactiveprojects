import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 700
screen_height = 700

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Smooth Gradient Circles")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to generate a smooth gradient color
def gradient_color(t):
    r = int((math.sin(0.02 * t + 0) * 127) + 128)
    g = int((math.sin(0.02 * t + 2) * 127) + 128)
    b = int((math.sin(0.02 * t + 4) * 127) + 128)
    return (r, g, b)

# Main loop
running = True
t = 0  # Time variable for color gradient animation
circle_radius = 15
circle_center_distance = 40  # Distance between circle centers

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a black background
    screen.fill((0, 0, 0))

    # Draw circles with gradient colors
    for y in range(0, screen_height, circle_center_distance):
        for x in range(0, screen_width, circle_center_distance):
            # Calculate the color based on time
            circle_color = gradient_color(t)

            pygame.draw.circle(screen, circle_color, (x, y), circle_radius)

    # Update the display
    pygame.display.flip()

    # Control frame rate (30 frames per second)
    clock.tick(30)

    # Increment the time variable for color animation
    t += 1

# Quit Pygame
pygame.quit()
