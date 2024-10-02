import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Define the size of the canvas
canvas_size = 400

# Create an empty canvas
canvas = np.zeros((canvas_size, canvas_size, 3), dtype=np.uint8)

# Define a function to generate a random shape with a random color
def generate_random_shape(size):
    shape = np.zeros((size, size, 3), dtype=np.uint8)
    color = [random.randint(0, 255) for _ in range(3)]

    for i in range(size):
        for j in range(size):
            if random.random() < 0.5:
                shape[i, j] = color

    return shape

# Generate three random shapes, each with a random color and larger size
shape_size = 150  # Adjust the size of the shapes
shape1 = generate_random_shape(shape_size)
shape2 = generate_random_shape(shape_size)
shape3 = generate_random_shape(shape_size)

# Extract the colors from the shapes
color1 = shape1[0, 0].tolist()
color2 = shape2[0, 0].tolist()
color3 = shape3[0, 0].tolist()

# Place the shapes in an ABBA pattern with symmetry axes at the center
canvas[25:25+shape_size, 25:25+shape_size] = shape1  # A
canvas[25:25+shape_size, 225:225+shape_size] = shape2  # B
canvas[225:225+shape_size, 25:25+shape_size] = shape2  # B
canvas[225:225+shape_size, 225:225+shape_size] = shape3  # A

# Define the animation update function
def update(frame):
    # Generate new random colors for each shape
    new_color1 = [random.randint(0, 255) for _ in range(3)]
    new_color2 = [random.randint(0, 255) for _ in range(3)]
    new_color3 = [random.randint(0, 255) for _ in range(3)]

    # Update the canvas with the new colors
    canvas[25:25+shape_size, 25:25+shape_size] = shape1 * new_color1  # A
    canvas[25:25+shape_size, 225:225+shape_size] = shape2 * new_color2  # B
    canvas[225:225+shape_size, 25:25+shape_size] = shape2 * new_color2  # B
    canvas[225:225+shape_size, 225:225+shape_size] = shape3 * new_color3  # A

    # Display the updated pattern
    plt.imshow(canvas)
    plt.axis('off')

# Create the animation
animation = FuncAnimation(plt.gcf(), update, frames=10, interval=400)

# Display the animation
plt.show()
