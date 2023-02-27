'''
Attempt at a prims algo implementation of the graph maze maker

Should generate a maze using a randomized Prims Algo Approach.

Basically looking like a BFS.
'''

from gridManager import Grid, GridSpace, GRID_X, GRID_Y
from moves import ALL_DIRS
grid = Grid()
def do_bfs():
    maze = []

    #start at the top left
    cur_x,cur_y = (1,1)
    grid.space_at(cur_x, cur_y).set_status('visited')
    frontier_structure = [(cur_x, cur_y, 'X')] # a queue


    while(frontier_structure):
        cur_x,cur_y,old_dir = frontier_structure.pop(0)
        #poss_moves = { ("N", move_north), ("S", move_south), ("E", move_east), ("W", move_west) }
        #STEP 1: QUEUE the children of the cur (if they are unvizited)

        for dir, poss_move in ALL_DIRS:
            #dir, poss_move = .pop()
            next_x, next_y = poss_move(cur_x, cur_y)

            if grid.square_unvisited(next_x, next_y): #and (next_x, next_y, old_dir) not in frontier_structure:
                
                frontier_structure.append((next_x, next_y, dir))
                grid.space_at(next_x, next_y).set_status('frontier')
                #print(cur_x, cur_y, dir)
        
        maze.append( (cur_x, cur_y, dir)  )
        #make da move 
        grid.space_at(next_x, next_y).set_status('visited')
        #status[cur_y][cur_x] = 1

        #for row in status:
        #    print(row)
        #print('\n\n')
    return maze

        
   
    


if __name__ == '__main__':
    s = do_bfs()
    print("DONE")
    for row in s:
        print(row)
    