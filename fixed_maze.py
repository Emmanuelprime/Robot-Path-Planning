# Define the maze as a 2D array
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

# Define the A* search function
def a_star_search(maze, start, goal):
    open_set = [(0, start)]  # Priority queue with the initial cell
    came_from = {}  # Dictionary to store the path
    g_score = {(x, y): float('inf') for x in range(len(maze)) for y in range(len(maze[0]))}

    g_score[start] = 0
    f_score = {cell: float('inf') for row in maze for cell in row}
    f_score[start] = heuristic_func(start, goal)

    while open_set:
        current = min(open_set, key=lambda cell: f_score[cell[1]])

        if current[1] == goal:
            path = reconstruct_path(came_from, current[1])
            return path

        open_set.remove(current)

        for neighbor in get_neighbors(current[1], maze):
            tentative_g_score = g_score[current[1]] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current[1]
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic_func(neighbor, goal)
                if neighbor not in open_set:
                    open_set.append((f_score[neighbor], neighbor))

    return None  # No path found

def heuristic_func(cell, goal):
    return abs(cell[0] - goal[0]) + abs(cell[1] - goal[1])

def get_neighbors(cell, maze):
    neighbors = []
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        x, y = cell[0] + dx, cell[1] + dy
        if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0:
            neighbors.append((x, y))
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

if __name__ == '__main__':
    start = (4, 0)
    goal = (0, 4)
    path = a_star_search(maze, start, goal)
    
    if path:
        print("Path found:")
        for cell in path:
            print(cell)
    else:
        print("No path found")
