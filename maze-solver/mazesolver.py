"""
                        I am using A* search for my robot.
    This algorithm is a type of informed search algorithm which means that it has an estimate of
    going from any node to the goal node using a hueristic function h(n).
    Generally, the total cost of moving from a node to a goal node or neighboring node f(n) is given by:
    f(n) = g(n) + h(n).
"""

#Algorithm Implementation
"""
    To implement the algorithm, we use a data structure known as priority queue. This algorithm gives priority
    what ever we design it to be. Example by Min or Max.
"""


from queue import PriorityQueue
from pyamaze import maze, agent

# Define the heuristic function to estimate the cost from one cell to another
def heuristic_func(cell1, cell2):
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

# Define the A* search function
def a_star_search(my_maze):
    start_cell = (my_maze.rows, my_maze.cols)
    
    # Initialize dictionaries to store g and f scores for each cell
    g_score = {cell: float('inf') for cell in my_maze.grid}
    g_score[start_cell] = 0
    f_score = {cell: float('inf') for cell in my_maze.grid}
    f_score[start_cell] = heuristic_func(start_cell, (1, 1))
    
    # Create a priority queue to store cells with lowest f scores
    open_set = PriorityQueue()
    open_set.put((f_score[start_cell], start_cell))
    
    # Create a dictionary to store the path
    came_from = {}
    
    while not open_set.empty():
        _, current = open_set.get()
        
        # Check if we reached the goal
        if current == (1, 1):
            break
        
        for d in 'ESNW':
            if my_maze.maze_map[current][d]:
                if d == 'E':
                    child_cell = (current[0], current[1] + 1)
                elif d == 'W':
                    child_cell = (current[0], current[1] - 1)
                elif d == 'N':
                    child_cell = (current[0] - 1, current[1])
                elif d == 'S':
                    child_cell = (current[0] + 1, current[1])

                tentative_g_score = g_score[current] + 1
                
                # Update g and f scores if a better path is found
                if tentative_g_score < g_score[child_cell]:
                    came_from[child_cell] = current
                    g_score[child_cell] = tentative_g_score
                    f_score[child_cell] = tentative_g_score + heuristic_func(child_cell, (1, 1))
                    open_set.put((f_score[child_cell], child_cell))
    
    # Reconstruct the path from the goal to the start
    path = []
    cell = (1, 1)
    while cell != start_cell:
        path.insert(0, cell)
        cell = came_from[cell]
    
    return path

if __name__ == '__main__':
    SIZE = 5
    my_maze = maze(SIZE, SIZE)
    my_maze.CreateMaze()
    path = a_star_search(my_maze)

    a = agent(my_maze, footprints=True)
    my_maze.tracePath({a: path})
    my_maze.run()
