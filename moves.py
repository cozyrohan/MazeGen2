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
