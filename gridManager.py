import pygame



GRID_X, GRID_Y =  5,5



def make_grid(px, py, rect_width, rect_height):
    square_side = int(rect_width/GRID_X)
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