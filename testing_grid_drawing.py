import pygame

PURPLE = (113, 4, 196)
BLACK = (0,0,0)
DESERT_TAN = (196, 192, 167)
LIGHT_GREEN = (204,255,229)
END_RED = (255,12,12)
WHITE = (255,255,255)

GRID_X, GRID_Y = 50, 50 
ASPECT_X, ASPECT_Y = 18,18


def draw_grid(px, py, rect_width, rect_height):
    square_side = int(rect_width/GRID_X)
    for i in range(GRID_X):
        for j in range(GRID_Y):
            r = pygame.Rect(px+(i*square_side), py+(square_side*j), square_side, square_side)
            yield r



if __name__ == '__main__':
    print('Welcome to the maze generator/solver.')
    pygame.init()
    screen = pygame.display.set_mode((400, 400), pygame.RESIZABLE)
    screen.fill(PURPLE)


    # run window
    running = True
    while running:
        WINDOW_WIDTH, WINDOW_HEIGHT =  screen.get_size()
                
        screen.fill(DESERT_TAN)
        
        for sq in draw_grid(10, 10, WINDOW_WIDTH, WINDOW_HEIGHT):
                    #screen.fill(WHITE,  rect=sq)
            pygame.draw.rect(screen, BLACK, sq, width=1 ) 

        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


    # quit pygame after closing window
    pygame.quit()

