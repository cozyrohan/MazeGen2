
'''
Attempt at a prims algo implementation of the graph maze maker

Should generate a maze using a randomized Prims Algo Approach.

Basically looking like a BFS (with salts??)
    # note this is unsystematic because we do not use a queue datam to get neighbors of neighbors in an
        orderly fashion. Instead we can go into depths randomly.

Plan of action:
    Pick a start location (x,y). 
    {
    Current is (x,y)

    Add neigbors to frontier struture {(x+1,y, righttangle), (x-1,y, lefttangle), (x,y+1, downtangle), (x,y-1, uptangle)}

    From the entire frontier set, then pick a square at random (this is akin to dequing a neighbor)
    Draw the inverse direction rectangle to connect it to a visited neighbor (at random if there is more than one adjacent). 
    In the 
    } repeat till done

'''

from random import shuffle
import gridManager
class GridSpace:
    def __init__(self, x, y, status):
        self.x_coord = x
        self.y_coord = y
        self.status = status   #unvisited, wall, or a number
        self.distance_from_start = 0 
        self.rect_direction = 'X'
    def set_status(self, stat):
        self.status = stat
    def get_status(self):
        return self.status
    def get_distance_from_start(self):
        return self.distance_from_start
    def increment_distance_from_prev(self, prev):
        self.distance_from_start +=  prev + 1
    def get_rect_dir(self):
        return self.rect_direction
    def set_rect_dir(self, dir):
        self.rect_direction = dir
    def get_backtrack_rect(self):
        return (self.x_coord, self.y_coord, self.rect_direction)

def print_status(status = None):
    #status = [[ GridSpace(i, j, 'unvisited') for j in range(10)] for i in range(10)]
    for row in status:
        msg = ''
        for space in row:
            msg += (str(space.get_rect_dir()) + str(space.get_status()) + str(space.get_distance_from_start())).center(13)
        print(msg)

def account_border(GRID_X_SQUARES, GRID_Y_SQUARES, status):
    for i in range(GRID_X_SQUARES):
        for j in range(GRID_Y_SQUARES):
            if i == 0 or i == GRID_Y_SQUARES-1 or j == 0 or j == GRID_X_SQUARES - 1:
                status[i][j].set_status("wall")
    
    return status

def move_north(cur_x, cur_y):
    return cur_x, cur_y-1
def move_south(cur_x, cur_y):
    return cur_x, cur_y+1
def move_east(cur_x, cur_y):
    return cur_x+1, cur_y
def move_west(cur_x, cur_y):
    return cur_x-1, cur_y

ALL_DIRS = { ("N", move_north), ("S", move_south), ("E", move_east), ("W", move_west) }
ALL_DIRS_DICT = { "N": move_north, "S": move_south, "E": move_east, "W": move_west }

OPPOSITE = { "N":"S", "S":"N", "E":"W", "W":"E"}

def square_unvisited(x, y, status):
    return status[y][x].get_status() == "unvisited"
def square_frontier(x, y, status):
    return status[y][x].get_status() == "frontier"
def square_visited(x, y, status):
    return status[y][x].get_status() == "visited" 
def square_wall(x, y, status):
    return status[y][x].get_status() == "wall" 

GRID_X_SQUARES = gridManager.GRID_X
GRID_Y_SQUARES = gridManager.GRID_Y

grid = [[ GridSpace(j, i, 'unvisited') for j in range(gridManager.GRID_Y)] for i in range(gridManager.GRID_X)]

def do_prims(GRID_X_SQUARES, GRID_Y_SQUARES):
    
    account_border(GRID_X_SQUARES, GRID_Y_SQUARES, grid)
    
    #print_status(grid)
    
    cur_x, cur_y = (1,1)


    #index  row , col
    grid[cur_y][cur_x].set_status('visited')


    frontier_structure = set()
    nth_step = 1

    while(True):
        #add all adjecent squares to cur to the frontier set
        for dir, move_func in ALL_DIRS:
            next_x, next_y = move_func(cur_x, cur_y)
            if square_unvisited(next_x, next_y, grid):
                frontier_structure.add((next_x, next_y))
                #grid[next_y][next_x].increment_distance_from_prev( grid[cur_y][cur_x].get_distance_from_start())
                grid[next_y][next_x].set_status('frontier')


        #print_status(grid)
        #print()
        #now from the frontier set, choose a random member
        if len(frontier_structure) == 0:
            break
        front_x, front_y = frontier_structure.pop()
        ADL = list(ALL_DIRS)
        shuffle(ADL)
        #now, randomly, see where the nearest visited part is, then draw from frontier to visited
        for dir, move_func in ADL:
            prev_x, prev_y = move_func(front_x, front_y)
            if square_visited(prev_x, prev_y, grid):
                grid[front_y][front_x].set_status('visited')
                grid[front_y][front_x].increment_distance_from_prev( grid[prev_y][prev_x].get_distance_from_start())
                grid[front_y][front_x].set_rect_dir(dir)

                yield (front_x, front_y, dir)
                break
        cur_x, cur_y = front_x, front_y    
        nth_step += 1
        #print_status(grid)
        #print()

    return grid
    
   
def maze_solve():
    print("solving maze")
    path = []
    cur_space = grid[GRID_Y_SQUARES-2][GRID_X_SQUARES-2]
    while(True):
        print("inloop")
        path.append(cur_space.get_backtrack_rect())

        dir = cur_space.get_rect_dir()
        if dir == 'X': break

        next_x, next_y = ALL_DIRS_DICT[dir](cur_space.x_coord, cur_space.y_coord)
        
        cur_space = grid[next_y][next_x]
    
    print(path)
    return path




if __name__ == '__main__':
    g = do_prims(GRID_X_SQUARES,GRID_Y_SQUARES) 
    print_status(g)
    maze_solve()  