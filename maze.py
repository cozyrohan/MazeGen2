import pygame
import sys
from math import floor
import bfs

import activeBG
import gridManager

PURPLE = (58,51,100)
BLACK = (0,0,0)
DESERT_TAN = (255,238,221)
LIGHT_GREEN = (204,255,229)
END_RED = (255,12,12)
WHITE = (255,255,255)





#Rectangle Constants

def get_uptangle(x,y, width, height):
    return pygame.Rect(x,y-height, width, 2*height)

def get_downtangle(x, y, width, height):
    return pygame.Rect(x,y, width, 2*height)

def get_rightangle(x, y, width, height):
    return pygame.Rect(x,y, 2*width, height)

def get_leftangle(x, y, width, height):
    return pygame.Rect(x-width, y, 2*width, height)

MOVES_DICT = {
    'N':get_uptangle,
    'S':get_downtangle,
    'E':get_rightangle,
    'W':get_leftangle
}


def do_bfs(grid_x_squares, grid_y_squares):
    start_x, start_y = 1,1
    bfs.do_bfs(grid_x_squares, grid_y_squares)
    return [m for m in bfs.do_bfs(grid_x_squares, grid_y_squares)]
        


def draw_maze(grid_start_x, grid_start_y, maze_width, maze_height):
    maze = do_bfs(gridManager.GRID_X, gridManager.GRID_Y)
    for x,y,dir in maze:
        w,h = int(maze_width/gridManager.GRID_X), int(maze_height/gridManager.GRID_Y)
        r = MOVES_DICT[dir](grid_start_x + (x * w) , grid_start_y + (y * h) , w - 2, h - 2)
        yield r
    




if __name__ == '__main__':
    print('Welcome to the maze generator/solver.')
    pygame.init()

    screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
    screen.fill(PURPLE)

    maze_backdrop = activeBG.init_maze_bg_rect(400, 400)
    
    running = True
    drawn = False
    while running:
        screen.fill(DESERT_TAN)

        WINDOW_WIDTH, WINDOW_HEIGHT =  screen.get_size()
        
        grid_start_x, grid_start_y, backdrop_width, backdrop_height = activeBG.update_maze_bg_rect(maze_backdrop, WINDOW_WIDTH, WINDOW_HEIGHT)
        pygame.draw.rect(screen, DESERT_TAN, maze_backdrop) 
        



        for sq in gridManager.make_grid(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
            pygame.draw.rect(screen, PURPLE, sq, width=1 ) 

        for sq in gridManager.make_wall_border(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
            pygame.draw.rect(screen, PURPLE, sq) 
       # if drawn == False: #not drawn:
        for sq in draw_maze(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
            pygame.draw.rect(screen, DESERT_TAN, sq) 
            pygame.display.update()
            pygame.time.wait(10)
            drawn = True
        #else:
        #    for sq in draw_maze(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
        #        pygame.draw.rect(screen, DESERT_TAN, sq) 

        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                

    # quit pygame after closing window
    pygame.quit()