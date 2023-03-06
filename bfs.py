'''
Attempt BFS implementation to find the end of GRID_X, GRID_Y


Basically looking like a BFS.
'''

from gridManager import Grid, GridSpace, GRID_X, GRID_Y
from moves import ALL_DIRS, OPPOSITE

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
        if old_dir != 'X': maze.append( (cur_x , cur_y, old_dir) )



        #STEP 1: QUEUE the children of the cur (if they are unvizited)
        
        #poss_moves = { ("N", move_north), ("S", move_south), ("E", move_east), ("W", move_west) }
        sl = list(ALL_DIRS)
        shuffle(sl)
        for dir, poss_move in sl:
            #dir, poss_move = .pop()
            next_x, next_y = poss_move(cur_x, cur_y)

            if  grid.square_unvisited(next_x, next_y): #and (next_x, next_y, old_dir) not in frontier_structure:
                
                frontier_structure.append((next_x, next_y, OPPOSITE[dir]))
                grid.space_at(next_x, next_y).set_status('frontier')
                #print(cur_x, cur_y, dir)
        
        #make da move 
        #grid.space_at(next_x, next_y).set_status('visited')
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
    