import pygame

import bfs
import randomPrims

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


def do_bfs():
    return [m for m in bfs.do_bfs()]

def solve_bfs():
    pass

### FUNCTIONS FOR MAKING AND SOLVING A PRIMS MAZE ###
def do_random_prims():
    return randomPrims.do_prims()
def solve_random_prims():
    return randomPrims.maze_solve()
### FUNCTIONS FOR MAKING AND SOLVING A PRIMS MAZE ###

def gen_rects(grid_start_x, grid_start_y, maze_width, maze_height, figure = None):
    for x, y, dir in figure:
        if dir == 'X' : break
        w,h = int(maze_width/gridManager.GRID_X), int(maze_height/gridManager.GRID_Y)
        r = MOVES_DICT[dir](grid_start_x + (x * w) , grid_start_y + (y * h) , w - 2, h - 2)
        yield r  

def start_pygame():
    print('Welcome to the maze generator/solver.')
    pygame.init()
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    screen.fill(PURPLE)
    maze_backdrop = activeBG.init_maze_bg_rect(800, 800)
    pygame.display.update()
    return screen, maze_backdrop

def draw_grid(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
        for sq in gridManager.make_grid(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
            pygame.draw.rect(screen, PURPLE, sq, width=1 ) 
        for sq in gridManager.make_wall_border(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
            pygame.draw.rect(screen, PURPLE, sq) 

def draw_rects(rect_gen_function, *args_to_function, delay = None, step = False, color = None ):
    for sq in rect_gen_function(*args_to_function):
            pygame.draw.rect(screen, color, sq) 
            if step: 
                pygame.display.update()
                pygame.time.wait(delay)


if __name__ == '__main__':
    screen, maze_backdrop = start_pygame()
    running = True
    drawn = False

    # The maze we want to generate and draw
    MAZE = do_bfs() 
    print("maze generated")

    # The solution to aformentioned maze
    SOLUTION = solve_random_prims()                        
    print("maze solved")




    # Begin the pygame loop
    print("rendering graphics...")

    while running:

        WINDOW_WIDTH, WINDOW_HEIGHT =  screen.get_size()
        
        grid_start_x, grid_start_y, backdrop_width, backdrop_height = activeBG.update_maze_bg_rect(maze_backdrop, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        #print("grid_start_x, grid_start_y,",  grid_start_x, grid_start_y, 
        #      "WINDOW_WIDTH, WINDOW_HEIGHT",  WINDOW_WIDTH, WINDOW_HEIGHT,
        #      "backdrop_width, backdrop_height",  backdrop_width, backdrop_height)


        screen.fill(DESERT_TAN)
        draw_grid(grid_start_x, grid_start_y, backdrop_width, backdrop_height)
        draw_rects( gen_rects,
                    grid_start_x, grid_start_y, backdrop_width, backdrop_height, MAZE, 
                    step=True, delay=2, color = DESERT_TAN)
        draw_rects( gen_rects,
                    grid_start_x, grid_start_y, backdrop_width, backdrop_height, SOLUTION, 
                    step=True, delay=10, color = LIGHT_GREEN )
        
        pygame.time.wait(7000)

        
        drawn = True

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                

    # quit pygame after closing window
    pygame.quit()