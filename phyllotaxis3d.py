import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Use the TkAgg backend (or other GUI backend of your choice)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the objective function you want to optimize
def objective_function(x, y):
    return -(x**2 + y**2)

# Initialize variables
x = np.random.rand() * 10  # Random initial x value
y = np.random.rand() * 10  # Random initial y value
step_size = 0.1  # Step size for optimization
num_iterations = 100  # Number of iterations

# Lists to store the trajectory of optimization
x_trajectory = [x]
y_trajectory = [y]

# Perform Hill Climbing optimization
for _ in range(num_iterations):
    # Calculate the objective function value at the current position
    current_value = objective_function(x, y)

    # Generate neighboring points
    x_neighbor = x + (np.random.rand() - 0.5) * step_size
    y_neighbor = y + (np.random.rand() - 0.5) * step_size

    # Calculate the objective function value at the neighbor
    neighbor_value = objective_function(x_neighbor, y_neighbor)

    # If the neighbor has a better value, move to the neighbor
    if neighbor_value > current_value:
        x, y = x_neighbor, y_neighbor

    # Store the current position in the trajectory
    x_trajectory.append(x)
    y_trajectory.append(y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the objective function surface
x_range = np.linspace(-10, 10, 100)
y_range = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = objective_function(X, Y)
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Plot the trajectory of optimization
ax.plot(x_trajectory, y_trajectory, [objective_function(x, y) for x, y in zip(x_trajectory, y_trajectory)], marker='o', color='r')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Objective Function')

# Show the plot
plt.show()
