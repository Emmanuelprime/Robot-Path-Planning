import heapq

# Define a 2D grid with obstacles (0 for free, 1 for obstacles)
grid = [
    [0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0],
]

# Define start and goal coordinates
start = (0, 0)
goal = (3, 5)

# Define basic movement directions (up, down, left, right)
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def heuristic(a, b):
    # Calculate the Manhattan distance as a heuristic
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def is_valid(x, y):
    # Check if the coordinates are within the grid and not blocked by obstacles
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

def a_star_search(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    
    came_from = {}
    g_score = {(i, j): float('inf') for i in range(len(grid)) for j in range(len(grid[0]))}
    g_score[start] = 0

    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)
            return path
        
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            if is_valid(neighbor[0], neighbor[1]):
                tentative_g_score = g_score[current] + 1
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
    
    return None

def visualize_path(path):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start:
                print("S", end=' ')
            elif (i, j) == goal:
                print("G", end=' ')
            elif (i, j) in path:
                print("*", end=' ')
            elif grid[i][j] == 1:
                print("X", end=' ')
            else:
                print("_", end=' ')
        print()

path = a_star_search(start, goal)

if path:
    visualize_path(path)
else:
    print("No path found")
