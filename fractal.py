import numpy as np
import matplotlib.pyplot as plt

# Define the size of the image
image_size = 100  # 10x10 image

# Create an empty canvas
canvas = np.zeros((image_size, image_size))

# Define a function to generate a random 10x10 pattern
def generate_random_pattern():
    return np.random.rand(10, 10)

# Function to recursively fill the canvas with the random pattern
def fill_canvas(canvas, x, y, size):
    if size <= 0:
        return

    pattern = generate_random_pattern()

    x_end = min(x + 10, image_size)
    y_end = min(y + 10, image_size)

    canvas[x:x_end, y:y_end] = pattern[:x_end - x, :y_end - y]

    size //= 2

    # Recursive calls for the four quadrants
    fill_canvas(canvas, x, y, size)
    fill_canvas(canvas, x + size, y, size)
    fill_canvas(canvas, x, y + size, size)
    fill_canvas(canvas, x + size, y + size, size)

# Start filling the canvas
fill_canvas(canvas, 0, 0, image_size)

# Display the fractal image
plt.imshow(canvas, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.show()
