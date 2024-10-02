import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Random Circles Bouncing")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Circle properties
circle_radius = 20
circle_speed = 5
circle_x = random.randint(circle_radius, screen_width - circle_radius)
circle_y = random.randint(circle_radius, screen_height - circle_radius)

# Mouse position
mouse_x, mouse_y = pygame.mouse.get_pos()

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate angle to move towards the mouse
    angle = math.atan2(mouse_y - circle_y, mouse_x - circle_x)

    # Calculate new circle position
    new_x = circle_x + circle_speed * math.cos(angle)
    new_y = circle_y + circle_speed * math.sin(angle)

    # Check if the circle is outside the screen boundaries
    if (
        new_x - circle_radius < 0
        or new_x + circle_radius > screen_width
        or new_y - circle_radius < 0
        or new_y + circle_radius > screen_height
    ):
        # Bounce off the edges
        angle = math.atan2(circle_y - mouse_y, circle_x - mouse_x)
        new_x = circle_x + circle_speed * math.cos(angle)
        new_y = circle_y + circle_speed * math.sin(angle)

    # Update circle position
    circle_x, circle_y = new_x, new_y

    # Clear the screen
    screen.fill(white)

    # Draw the circle
    pygame.draw.circle(screen, red, (int(circle_x), int(circle_y)), circle_radius)

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
