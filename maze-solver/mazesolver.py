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

from queue import PriorityQueue # for using the priority queue since we move to the cell with lowest f(n)
from pyamaze import maze, agent,textLabel # for generating our maze



# Important things about the library pyamaze
#print(my_maze.rows)
#print(my_maze.cols)
#print(my_maze.grid) # shows list of all cells
#print(my_maze.maze_map) # returns a dictionary of the coordinates of the squares(as tuple) and the moves from each square (dictionary)

def hueristic_func(cell1, cell2):
    """
    This function returns the hueristic value of moving from cell1 to cell2
    """
    x1,y1 = cell1
    x2,y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def a_star_search(my_maze):
    """
    This function implements the A* search algorithm
    """
    # we define start cell
    start_cell = (my_maze.rows,my_maze.cols) 
    
    # create dictionary comprehension to store the g values of each cell
    g_score = {cell:float('inf') for cell in my_maze.grid} 
    
    # start cell has a g_score of zero since we have not made any steps
    g_score[start_cell] = 0 
    
    #create dictionary comprehension to store the f values of each cell
    f_score = {cell:float('inf') for cell in my_maze.grid} 
    
    f_score[start_cell] = hueristic_func(start_cell,(1,1)) + 0

    # create a priority queue to store the cells with lowest f values
    my_buffer = PriorityQueue()

    #update the f score of the start cell
    my_buffer.put((hueristic_func(start_cell,(1,1)),hueristic_func(start_cell,(1,1)),start_cell))
    aPath={}
    while not my_buffer.empty():
        currCell=my_buffer.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if my_maze.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+hueristic_func(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    my_buffer.put((temp_f_score,hueristic_func(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start_cell:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath
if __name__=='__main__':
    SIZE = 25
    my_maze = maze(SIZE,SIZE)
    my_maze.CreateMaze()
    path=a_star_search(my_maze)

    a=agent(my_maze,footprints=True)
    my_maze.tracePath({a:path})
    l=textLabel(my_maze,'A Star Path Length',len(path)+1)

    my_maze.run()
