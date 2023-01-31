'''
Attempt at a prims algo implementation of the graph maze maker

Should generate a maze using a randomized Prims Algo Approach.

Basically looking like a BFS.
'''

def account_border(grid_x_squares, grid_y_squares, status):
    for i in range(grid_x_squares):
        for j in range(grid_y_squares):
            if i == 0 or i == grid_y_squares-1 or j == 0 or j == grid_x_squares - 1:
                status[i][j] = 2
    
    return status

def move_north(cur_x, cur_y):
    return cur_x, cur_y-1
def move_south(cur_x, cur_y):
    return cur_x, cur_y+1
def move_east(cur_x, cur_y):
    return cur_x+1, cur_y
def move_west(cur_x, cur_y):
    return cur_x-1, cur_y

def move_valid(x, y, status):
    return status[y][x] == 0

def do_bfs(grid_x_squares, grid_y_squares):
    status = [[ 0 for j in range(grid_y_squares)] for i in range(grid_x_squares)]
    account_border(grid_x_squares, grid_y_squares, status)
    q = [(1,1,"x")]
    cur_x,cur_y = (1,1)
    status[cur_y][cur_x] = 1
    
    while(q):
        cur_x,cur_y,old_dir = q.pop(0)
        poss_moves = { ("N", move_north), ("S", move_south), ("E", move_east), ("W", move_west) }
        #STEP 1: QUEUE the children of the cur (if they are unvizited)
        for i in range(4):
            dir, poss_move = poss_moves.pop()
            next_x, next_y = poss_move(cur_x, cur_y)
            #print( next_x, next_y,  move_valid(next_x, next_y, status))

            if move_valid(next_x, next_y, status) and (next_x, next_y, old_dir) not in q:
                
                q.append((next_x, next_y, dir))

                #print(cur_x, cur_y, dir)
                yield (cur_x, cur_y, dir)
        

        #make da move 
        status[cur_y][cur_x] = 1

        #for row in status:
        #    print(row)
        #print('\n\n')
            

        
   
    


if __name__ == '__main__':
    s = do_bfs(20,20)
    print("DONE")
    for row in s:
        print(row)
    