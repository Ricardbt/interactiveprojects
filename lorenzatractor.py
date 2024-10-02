import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz attractor parameters
sigma = 10
rho = 28
beta = 8 / 3

# Time parameters
dt = 0.01
num_steps = 10000

# Initialize arrays for x, y, and z coordinates
x = np.zeros(num_steps)
y = np.zeros(num_steps)
z = np.zeros(num_steps)

# Initial conditions
x[0] = 0
y[0] = 1
z[0] = 1.05

# Numerical integration (Euler's method)
for i in range(1, num_steps):
    dx = sigma * (y[i - 1] - x[i - 1])
    dy = x[i - 1] * (rho - z[i - 1]) - y[i - 1]
    dz = x[i - 1] * y[i - 1] - beta * z[i - 1]
    
    x[i] = x[i - 1] + dx * dt
    y[i] = y[i - 1] + dy * dt
    z[i] = z[i - 1] + dz * dt

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Lorenz attractor
ax.plot(x, y, z, lw=0.5)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Attractor')

# Show the plot
plt.show()
