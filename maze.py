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


def do_bfs(grid_x_squares, grid_y_squares):
    start_x, start_y = 1,1
    #bfs.do_bfs(grid_x_squares, grid_y_squares)
    return [m for m in bfs.do_bfs(grid_x_squares, grid_y_squares)]

def draw_maze_using_bfs(grid_start_x, grid_start_y, maze_width, maze_height):
    maze = do_bfs(gridManager.GRID_X, gridManager.GRID_Y)
    for x,y,dir in maze:
        w,h = int(maze_width/gridManager.GRID_X), int(maze_height/gridManager.GRID_Y)
        r = MOVES_DICT[dir](grid_start_x + (x * w) , grid_start_y + (y * h) , w - 2, h - 2)
        yield r       

def do_random_prims(grid_x_squares, grid_y_squares):
    start_x, start_y = 1,1
    #randomPrims.do_randomPrims(grid_x_squares, grid_y_squares)
    return [m for m in randomPrims.do_prims(grid_x_squares, grid_y_squares)]


def draw_maze_using_prims(grid_start_x, grid_start_y, maze_width, maze_height, maze = None):
    #maze = do_random_prims(gridManager.GRID_X, gridManager.GRID_Y)
    for x,y,dir in maze:
        w,h = int(maze_width/gridManager.GRID_X), int(maze_height/gridManager.GRID_Y)
        r = MOVES_DICT[dir](grid_start_x + (x * w) , grid_start_y + (y * h) , w - 2, h - 2)
        yield r

def solve_random_prims():
    return randomPrims.maze_solve()

def draw_maze_solution(grid_start_x, grid_start_y, maze_width, maze_height, solution):
    for x, y, dir in solution:
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
    
if __name__ == '__main__':
    screen, maze_backdrop = start_pygame()
    running = True
    drawn = False
    mz = do_random_prims(gridManager.GRID_X, gridManager.GRID_Y)
    solution_path = solve_random_prims()
    while running:

        WINDOW_WIDTH, WINDOW_HEIGHT =  screen.get_size()
        
        grid_start_x, grid_start_y, backdrop_width, backdrop_height = activeBG.update_maze_bg_rect(maze_backdrop, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        #print("grid_start_x, grid_start_y,",  grid_start_x, grid_start_y, 
        #      "WINDOW_WIDTH, WINDOW_HEIGHT",  WINDOW_WIDTH, WINDOW_HEIGHT,
        #      "backdrop_width, backdrop_height",  backdrop_width, backdrop_height)


        screen.fill(DESERT_TAN)
        #if not drawn:
        for sq in gridManager.make_grid(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
            pygame.draw.rect(screen, PURPLE, sq, width=1 ) 
        pygame.display.update()
        pygame.time.wait(1000)
        for sq in gridManager.make_wall_border(grid_start_x, grid_start_y, backdrop_width, backdrop_height):
            pygame.draw.rect(screen, PURPLE, sq) 
        pygame.display.update()
        pygame.time.wait(1000)

        for sq in list(draw_maze_using_prims(grid_start_x, grid_start_y, backdrop_width, backdrop_height, maze = mz)):
            pygame.draw.rect(screen, DESERT_TAN, sq) 
            #print("drew a rect")
            pygame.display.update()
            pygame.time.wait(4)

        for sq in draw_maze_solution(grid_start_x, grid_start_y, backdrop_width, backdrop_height, solution = solution_path):
            pygame.draw.rect(screen, LIGHT_GREEN, sq) 
            pygame.display.update()
            pygame.time.wait(4)

        
            drawn = True


        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                

    # quit pygame after closing window
    pygame.quit()