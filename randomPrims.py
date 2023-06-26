
'''
Attempt at a prims algo implementation of the graph maze maker

Should generate a maze using a randomized Prims Algo Approach.

Basically looking like a BFS 
    # note this is unsystematic because we do not use a queue ds to get neighbors of neighbors in an
        orderly fashion. Instead we can go into neighbors randomly.

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
from gridManager import Grid, GRID_X, GRID_Y
from moves import ALL_DIRS_DICT, ALL_DIRS

grid = Grid()
def do_prims():
    
     
    # this is the returned value, a list of coordinates (x,y, direction),
    # where direction is the direction of
    # the rectangle extending from (x,y)

    maze = []  
    
    
    cur_x, cur_y = (1,1)
    grid.space_at(cur_x, cur_y).set_status('visited')
    frontier_structure = set()
    while(True):
        for dir, move_func in ALL_DIRS:
            
            #add all unvisited adjecent squares to cur to the frontier set
            next_x, next_y = move_func(cur_x, cur_y)
            if grid.square_unvisited(next_x, next_y):
                frontier_structure.add((next_x, next_y))
                grid.space_at(next_x, next_y).set_status('frontier')
        
        #end condition (no more frontier)
        if len(frontier_structure) == 0:
            break

        #step into a frontier
        front_x, front_y = frontier_structure.pop()

        #shuffle the moves list
        ADL = list(ALL_DIRS)
        shuffle(ADL)

        #now, randomly, see where the nearest visited part is, then draw from frontier to visited
        for dir, move_func in ADL:
            prev_x, prev_y = move_func(front_x, front_y)
            if grid.square_visited(prev_x, prev_y):
                grid.space_at(front_x, front_y).set_status('visited')
                grid.space_at(front_x, front_y).increment_distance_from_prev( grid.space_at(prev_x, prev_y).get_distance_from_start())
                grid.space_at(front_x, front_y).set_rect_dir(dir)   #direction from frontier to previous square (back-tracker)
                maze.append( (front_x, front_y, dir) )
                break

        # the frontier added is the new current point, continue looping and adding frontiers from there...
        cur_x, cur_y = front_x, front_y    

    return maze
    
def maze_solve():
    print("solving maze")
    path = []
    cur_space = grid.space_at(GRID_X-2, GRID_Y-2,)
    while(True):
        path.append(cur_space.get_backtrack_rect())
        dir = cur_space.get_rect_dir()
        if dir == 'X': break
        next_x, next_y = ALL_DIRS_DICT[dir](cur_space.x_coord, cur_space.y_coord)
        cur_space = grid.space_at(next_x,next_y)
    return path




if __name__ == '__main__':
    g = do_prims(GRID_X,GRID_Y) 
    maze_solve()  