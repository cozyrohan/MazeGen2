import pygame
from math import ceil


GRID_X, GRID_Y =  20,20


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

class Grid:
    def __init__(self):
        self.status = [[ GridSpace(j, i, 'unvisited') for j in range(GRID_Y)] for i in range(GRID_X)]
        
        #add "walls" to the grid
        for i in range(GRID_X):
            for j in range(GRID_Y):
                if i == 0 or i == GRID_Y-1 or j == 0 or j == GRID_X - 1:
                    self.status[i][j].set_status("wall")
        
    def square_unvisited(self, x, y):
        return self.status[y][x].get_status() == "unvisited"

    def square_frontier(self, x, y):
        return self.status[y][x].get_status() == "frontier"

    def square_visited(self, x, y):
        return self.status[y][x].get_status() == "visited" 

    def square_wall(self, x, y):
        return self.status[y][x].get_status() == "wall" 

    def space_at(self, x, y):
        return self.status[y][x]

    def print_status(self):
        for row in self.status:
            msg = ''
            for space in row:
                msg += (str(space.get_rect_dir()) + str(space.get_status()) + str(space.get_distance_from_start())).center(13)
            print(msg)







###  Functions for the drawing of a grid, placed here largly for lack of a better location ###

def make_grid(px, py, rect_width, rect_height):
    square_side = int(rect_width/GRID_X)
    print("square_side, ", square_side) 
    for i in range(GRID_X):
        for j in range(GRID_Y):
            r = pygame.Rect(px+(i*square_side)-1, py+(square_side*j)-1, square_side, square_side)
            yield r

def make_wall_border(px, py, rect_width, rect_height):
    square_side = int(rect_width/GRID_X)
    for i in range(GRID_X):
        for j in range(GRID_Y):
            if i == 0 or i == GRID_Y-1 or j == 0 or j == GRID_X - 1:
                r = pygame.Rect(px+(i*square_side), py+(square_side*j), square_side, square_side)
            yield r 