import tkinter as tk
import random

GRID_SIZE = 10
CELL_SIZE = 40
NUM_OBSTACLES = 20

def generate_random_grid():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    
    for _ in range(NUM_OBSTACLES):
        x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
        grid[y][x] = 1  # Obstacle
    
    start_x, start_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    goal_x, goal_y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    
    grid[start_y][start_x] = 2  # Start position
    grid[goal_y][goal_x] = 3  # Goal position
    
    return grid

def draw_grid():
    root = tk.Tk()
    root.title("Grid Visualization")
    canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
    canvas.pack()
    
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] == 0:  # Open space
                fill_color = "white"
            elif grid[y][x] == 1:  # Obstacle
                fill_color = "black"
            elif grid[y][x] == 2:  # Start position
                fill_color = "red"
            elif grid[y][x] == 3:  # Goal position
                fill_color = "green"
            draw_rectangle(canvas, x, y, fill_color)
    
    root.mainloop()

def draw_rectangle(canvas, x, y, fill_color):
    x0 = x * CELL_SIZE
    y0 = y * CELL_SIZE
    x1 = x0 + CELL_SIZE
    y1 = y0 + CELL_SIZE
    canvas.create_rectangle(x0, y0, x1, y1, fill=fill_color, outline="black")

grid = generate_random_grid()
draw_grid()
