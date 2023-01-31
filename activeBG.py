import pygame

ASPECT_X, ASPECT_Y = 18,18


def init_maze_bg_rect(WINDOW_WIDTH: int, WINDOW_HEIGHT: int):
    '''
    Based on the current window size, return an initial maze backdrop. (centered based on aspect ratio)
    '''
    multiplier = min(   int(WINDOW_WIDTH/ASPECT_X), int(WINDOW_HEIGHT/ASPECT_Y) )
    rect_width, rect_height = max(ASPECT_X, ASPECT_X*multiplier), max(ASPECT_Y, ASPECT_Y*multiplier )

    px, py = int((WINDOW_WIDTH-rect_width)/2), int((WINDOW_HEIGHT-rect_height)/2)

    return pygame.Rect(px, py, rect_width, rect_height)




def update_maze_bg_rect(maze_bg_rect: pygame.rect, WINDOW_WIDTH: int , WINDOW_HEIGHT: int):
    '''
    Based on the current window size, update the initial maze backdrop.

    Return the   (x,y, width, height) of the new backdrop
    '''
    multiplier = min(int(WINDOW_WIDTH/ASPECT_X), int(WINDOW_HEIGHT/ASPECT_Y))
    rect_width, rect_height = max(ASPECT_X, ASPECT_X*multiplier), max(ASPECT_Y, ASPECT_Y*multiplier )

    px, py = int((WINDOW_WIDTH-rect_width)/2), int((WINDOW_HEIGHT-rect_height)/2)

    maze_bg_rect.update(px, py, rect_width, rect_height)
    
    return (px, py, rect_width, rect_height)