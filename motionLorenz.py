import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Lorenz attractor parameters
sigma = 1
rho = 2.8
beta = 4 / 3

# Time parameters
dt = 0.02
num_steps = 100

# Initialize arrays for x, y, and z coordinates
x = np.zeros(num_steps)
y = np.zeros(num_steps)
z = np.zeros(num_steps)

# Initial conditions
x[0] = 0
y[0] = 0.001
z[0] = 0.002

# Numerical integration (Euler's method)
for i in range(1, num_steps):
    dx = sigma * (y[i - 1] - x[i - 1])
    dy = x[i - 1] * (rho - z[i - 1]) - y[i - 1]
    dz = x[i - 1] * y[i - 1] - beta * z[i - 1]
    
    x[i] = x[i - 1] + dx * dt
    y[i] = y[i - 1] + dy * dt
    z[i] = z[i - 1] + dz * dt

# Create a 3D plot with a larger figure size
fig = plt.figure(figsize=(10, 8))  # Set width to 10 and height to 8
ax = fig.add_subplot(111, projection='3d')

# Initialize a rectangle's initial position
rect_x = [x[0]]
rect_y = [y[0]]
rect_z = [z[0]]

# Create a rectangle
rectangle = ax.plot(rect_x, rect_y, rect_z, 'ro-')[0]

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rectangle following Lorenz Attractor')

# Function to update the rectangle's position in the animation
def update(frame):
    if frame < num_steps:
        rect_x.append(x[frame])
        rect_y.append(y[frame])
        rect_z.append(z[frame])
        rectangle.set_data_3d(np.array(rect_x), np.array(rect_y), np.array(rect_z))
        return rectangle,

# Create the animation
ani = FuncAnimation(fig, update, frames=range(num_steps), blit=True, repeat=False)

# Show the animation
plt.show()
