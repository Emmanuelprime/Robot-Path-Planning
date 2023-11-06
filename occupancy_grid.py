import numpy as np
import matplotlib.pyplot as plt

# Define the dimensions of the occupancy grid
grid_width = 20
grid_height = 20

# Create an empty occupancy grid with all cells initially unoccupied (white)
occupancy_grid = np.ones((grid_height, grid_width))

# Define obstacle positions in the grid (fewer obstacles)
obstacle_positions = [(5, 5), (8, 8), (12, 12),(2,4),(1,12)]

# Mark the obstacle positions as occupied (black) in the occupancy grid
for x, y in obstacle_positions:
    occupancy_grid[y, x] = 0

# Define the start and goal positions
start = (0, 0)
goal = (19, 19)

# Visualize the occupancy grid
plt.imshow(occupancy_grid, cmap='gray', origin='lower')
plt.colorbar()
plt.plot(start[0], start[1], 'go', label='Start')
plt.plot(goal[0], goal[1], 'ro', label='Goal')
plt.legend()
plt.title("Occupancy Grid with Start and Goal")
plt.grid(True)

# Show the occupancy grid
plt.show()
