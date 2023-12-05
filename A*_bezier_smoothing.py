import numpy as np
import cv2
import matplotlib.pyplot as plt
from queue import PriorityQueue

# Create a Bézier curve interpolation function
def bezier_curve(t, p0, p1, p2, p3):
    return (1 - t)**3 * p0 + 3 * (1 - t)**2 * t * p1 + 3 * (1 - t) * t**2 * p2 + t**3 * p3

# Function to create the smoothed path for a Bézier curve segment
def create_smoothed_path(p0, p1, p2, p3, num_points=100):
    t_values = np.linspace(0, 1, num_points)
    return np.array([bezier_curve(t, p0, p1, p2, p3) for t in t_values])

# Function to apply Bézier smoothing to the entire path
def apply_bezier_smoothing(path, num_points=100):
    smoothed_path = []

    for i in range(len(path) - 1):
        p0 = np.array(path[i])
        p3 = np.array(path[i + 1])

        # Choose control points closer to the ends
        p1 = (p0 + p3) / 5  # Adjust the denominator as needed
        p2 = (p0 + p3) * 4 / 5  # Adjust the numerator as needed


        segment_smoothed_path = create_smoothed_path(p0, p1, p2, p3, num_points)
        smoothed_path.extend(segment_smoothed_path)

    return np.array(smoothed_path)

# Function to create an occupancy grid from an image
def create_occupancy_grid_from_image(image_path, threshold=128):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, thresholded = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

    occupancy_grid = thresholded // 255

    return occupancy_grid, image

# Example usage:
image_path = "grid2.png"  
start = (350, 50)
goal = (50, 350)

# Create an occupancy grid from the image
occupancy_grid, image = create_occupancy_grid_from_image(image_path)

# Apply A* search for the original path
def a_star_search(occupancy_grid, start, goal):
    def heuristic(cell, goal):
        #disitance = np.sqrt((cell[0]-goal[0])**2 + (cell[1]-goal[1])**2)
        manhat_distance =  abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])
        return manhat_distance

    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {cell: float('inf') for cell in np.ndindex(occupancy_grid.shape)}
    g_score[start] = 0

    while not open_set.empty():
        _, current = open_set.get()

        if current == goal:
            path = reconstruct_path(came_from, current)
            return path

        for small_step_x, small_step_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = current[0] + small_step_x, current[1] + small_step_y

            if 0 <= x < occupancy_grid.shape[1] and 0 <= y < occupancy_grid.shape[0] and occupancy_grid[y, x] == 1:
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score[(x, y)]:
                    came_from[(x, y)] = current
                    g_score[(x, y)] = tentative_g_score
                    f_score = tentative_g_score + heuristic((x, y), goal)
                    open_set.put((f_score, (x, y)))

    return None
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# A* search to find the original path
path_found = a_star_search(occupancy_grid, start, goal)

if path_found:
    print("Original Path found:")
    for cell in path_found:
        print(cell)
else:
    print("No original path found")
    # Plot the occupancy grid
    plt.imshow(occupancy_grid, cmap='gray', origin='lower')
    plt.plot(start[0], start[1], 'go', label='Start')
    plt.plot(goal[0], goal[1], 'ro', label='Goal')
    plt.legend()
    plt.title("Occupancy Grid without Path")
    plt.grid(True)
    plt.show()

# Apply Bézier curve smoothing to the path
smoothed_path = apply_bezier_smoothing(path_found)

# Plot the original image
plt.imshow(image, cmap='gray', origin='lower')
plt.colorbar()
plt.plot(start[0], start[1], 'go', label='Start')
plt.plot(goal[0], goal[1], 'ro', label='Goal')
plt.legend()
plt.title("Original Image")
plt.grid(True)
plt.show()

# Plot the occupancy grid with the smoothed path
plt.imshow(occupancy_grid, cmap='gray', origin='lower')
plt.colorbar()
plt.plot([int(cell[0]) for cell in smoothed_path], [int(cell[1]) for cell in smoothed_path], marker='o', markersize=4, color='blue', label='Path')
plt.plot(start[0], start[1], 'go', label='Start')
plt.plot(goal[0], goal[1], 'ro', label='Goal')
plt.legend()
plt.title("Occupancy Grid with Smoothed Path")
plt.grid(True)
plt.show()
