
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

def print_status(status):
    for row in status:
        print('\n', row)

def account_border(grid_x_squares, grid_y_squares, status):
    for i in range(grid_x_squares):
        for j in range(grid_y_squares):
            if i == 0 or i == grid_y_squares-1 or j == 0 or j == grid_x_squares - 1:
                status[i][j] = 3
    
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
OPPOSITE = { "N":"S", "S":"N", "E":"W", "W":"E"}

def square_unvisited(x, y, status):
    return status[y][x] == 0
def square_frontier(x, y, status):
    return status[y][x] == 1
def square_visited(x, y, status):
    return status[y][x] == 2
def square_wall(x, y, status):
    return status[y][x] == 3


def do_prims(grid_x_squares, grid_y_squares):
    
    status = [[ 0 for j in range(grid_y_squares)] for i in range(grid_x_squares)]
    account_border(grid_x_squares, grid_y_squares, status)
    
    
    cur_x, cur_y = (1,1)

    status[cur_y][cur_x] = 2

    frontier_structure = set()
    while(True):
        #add all adjecent squares to cur to the frontier set
        for dir, move_func in ALL_DIRS:
            next_x, next_y = move_func(cur_x, cur_y)
            if square_unvisited(next_x, next_y, status):
                frontier_structure.add((next_x, next_y))
                status[next_y][next_x] = 1

        #print_status(status)
        #print()
        #now from the frontier set, choose a random member
        if len(frontier_structure) == 0:
            break
        front_x, front_y = frontier_structure.pop()
        ADL = list(ALL_DIRS)
        shuffle(ADL)
        #now, randomly, see where the nearest visited part is, then draw from frontier to visited
        for dir, move_func in ADL:
            next_x, next_y = move_func(front_x, front_y)
            if square_visited(next_x, next_y, status):
                status[front_y][front_x] = 2
                yield (front_x, front_y, dir)
                break
        cur_x, cur_y = front_x, front_y    
        #print_status(status)
        #print()

    return status
    
   
    


if __name__ == '__main__':
    s = do_prims(10,10)
    print("DONE")
    for row in s:
        print(row)
    