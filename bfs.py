'''
Attempt BFS implementation to find the end of GRID_X, GRID_Y


Basically looking like a BFS.
'''

from gridManager import Grid, GridSpace, GRID_X, GRID_Y
from moves import ALL_DIRS, ALL_DIRS_DICT, OPPOSITE

from random import shuffle

grid = Grid()
def do_bfs():
    maze = []

    #start at the top left
    cur_x,cur_y = (1,1)
    #grid.space_at(cur_x, cur_y).set_status('visited')
    frontier_structure = [(cur_x, cur_y, 'X')] # a queue


    while(frontier_structure):
        cur_x,cur_y,old_dir = frontier_structure.pop(0)

        #visit to a frontier
        grid.space_at(cur_x, cur_y).set_status('visited')

        if old_dir != 'X': 
            grid.space_at(cur_x, cur_y).set_rect_dir(old_dir)

            maze.append( (cur_x , cur_y, old_dir) )


        #STEP 1: QUEUE the children of the cur (if they are unvizited)
        
        #poss_moves = { ("N", move_north), ("S", move_south), ("E", move_east), ("W", move_west) }
        sl = list(ALL_DIRS)
        shuffle(sl)
        for dir, poss_move in sl:
            #dir, poss_move = .pop()
            next_x, next_y = poss_move(cur_x, cur_y)

            if  grid.square_unvisited(next_x, next_y): #and (next_x, next_y, old_dir) not in frontier_structure:
                
                # OK the opposite direction is opted for because we want the first step from (1,1) to be random
                # so go from the second square back to (1,1)
                frontier_structure.append((next_x, next_y, OPPOSITE[dir]))
                grid.space_at(next_x, next_y).set_status('frontier')

                #print(cur_x, cur_y, dir)
        

    return maze

def maze_solve():
    #print("solving maze")
    path = []
    cur_space = grid.space_at(GRID_X-2, GRID_Y-2,)
    #print("BTR is: ", cur_space.get_backtrack_rect())
    while(True):
        path.append(cur_space.get_backtrack_rect())
        dir = cur_space.get_rect_dir()
        if dir == 'X': break
        next_x, next_y = ALL_DIRS_DICT[dir](cur_space.x_coord, cur_space.y_coord)
        cur_space = grid.space_at(next_x,next_y)
    return path

   
    


if __name__ == '__main__':
    s = do_bfs()
    print("DONE")
    for step in s:
        print(step)
    grid.print_status()
    p = maze_solve()
    print(p)
    