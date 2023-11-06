import numpy as np

import matplotlib.pyplot as plt
from queue import PriorityQueue

def create_our_occupancy_grid():
    grid_width = 20
    grid_height = 20

    occupancy_grid = np.ones((grid_height, grid_width))
    my_obstacle_positions = [(5, 5), (8, 8), (12, 12), (2, 4), (1, 12),(0,6),(4,5),(3,9),(5, 2),(5, 3),(5, 4),(6, 4),(6, 5),(6, 6),(6, 7),(6, 8),(6, 9),(6, 10),(6, 11),(7, 11)]

    for x, y in my_obstacle_positions:
        occupancy_grid[y, x] = 0
    return occupancy_grid

start = (5, 1)
goal = (7, 15)

# A* search function
def a_star_search(occupancy_grid, start, goal):
    def heuristic(cell, goal):
        return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

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

# A function to reconstruct the path from the goal to the start
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

occupancy_grid = create_our_occupancy_grid()

path_found = a_star_search(occupancy_grid, start, goal)

if path_found:
    print("Path found:")
    for cell in path_found:
        print(cell)
else:
    print("No path found")
    plt.imshow(occupancy_grid, cmap='gray', origin='lower')
    plt.plot(start[0], start[1], 'go', label='Start')
    plt.plot(goal[0], goal[1], 'ro', label='Goal')
    plt.legend()
    plt.title("Occupancy Grid without Path")
    plt.grid(True)
    plt.show()


# Visualize the occupancy grid with the path found by the robot
plt.imshow(occupancy_grid, cmap='gray', origin='lower')
plt.colorbar()
plt.plot([cell[0] for cell in path_found], [cell[1] for cell in path_found], marker='o', markersize=4, color='blue', label='Path')
plt.plot(start[0], start[1], 'go', label='Start')
plt.plot(goal[0], goal[1], 'ro', label='Goal')
plt.legend()
plt.title("Occupancy Grid with Path")
plt.grid(True)

# Show the occupancy grid with the path
plt.show()
