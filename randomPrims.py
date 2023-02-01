'''
Attempt at a prims algo implementation of the graph maze maker

Should generate a maze using a randomized Prims Algo Approach.

Basically looking like a BFS.
'''

def account_border(grid_x_squares, grid_y_squares, status):
    for i in range(grid_x_squares):
        for j in range(grid_y_squares):
            if i == 0 or i == grid_y_squares-1 or j == 0 or j == grid_x_squares - 1:
                status[i][j].set_status("VISITED")
    
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


class GridCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = 0
        self.neighbors = set()
    
    def set_status(self, stat):
        if stat == "UNSEEN":
            self.status = 0
        elif stat == "SEEN":
            self.status = 1
        elif stat == "VISITED":
            self.status = 2
    def get_status(self):
        return self.status

    def find_valid_neighbors(self, status):
        poss_moves = { ("N", move_north), ("S", move_south), ("E", move_east), ("W", move_west) }
        for i in range(4):
            dir, poss_move = poss_moves.pop()
            neighbor_x, neighbor_y = poss_move(self.x, self.y)
            #print( next_x, next_y,  move_valid(next_x, next_y, status))
            if move_valid(neighbor_x, neighbor_y, status):
                self.neighbors.add((neighbor_x, neighbor_y, dir))
    
def print_grid(status_arr):
    for row in status_arr:
        s = ""
        for item in row:
            s  += " " + str(item.get_status()) + " "
        print(s)


def do_prims(grid_x_squares, grid_y_squares):
    status = [[ GridCell(x, y)  for y in range(grid_y_squares)] for x in range(grid_x_squares)]
    account_border(grid_x_squares, grid_y_squares, status)
    return status 


if __name__ == '__main__':
    s = do_prims(4,4)
    print_grid(s)
    s[1][1].find_valid_neighbors(s)
    print(s[1][1].neighbors)
    print("DONE")

    