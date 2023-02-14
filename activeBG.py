import pygame
import gridManager
from math import ceil

ASPECT_X, ASPECT_Y = 1,1

def find_nearest_whole_num(dimension):
    factor = int(dimension/gridManager.GRID_X)
    return factor * gridManager.GRID_X

def init_maze_bg_rect(WINDOW_WIDTH: int, WINDOW_HEIGHT: int):
    '''
    Based on the current window size, return an initial maze backdrop. (centered based on aspect ratio)
    '''
    multiplier = min(   int(WINDOW_WIDTH/ASPECT_X), int(WINDOW_HEIGHT/ASPECT_Y) )
    rw, rh  = ASPECT_X*multiplier, ASPECT_Y*multiplier 
    
    rect_width, rect_height = max(ASPECT_X, find_nearest_whole_num(rw)), max(ASPECT_Y, find_nearest_whole_num(rh) )

    px, py = ceil(  (WINDOW_WIDTH-rect_width)/2  ), ceil((WINDOW_HEIGHT-rect_height)/2)
    #print("xcoord, y coord  : ",px, py, "   rect_width, rect_height : ", rect_width, rect_height )
    return pygame.Rect(px, py, rect_width, rect_height)




def update_maze_bg_rect(maze_bg_rect: pygame.rect, WINDOW_WIDTH: int , WINDOW_HEIGHT: int):
    '''
    Based on the current window size, update the initial maze backdrop.

    Return the   (x,y, width, height) of the new backdrop
    '''
    multiplier = min(int(WINDOW_WIDTH/ASPECT_X), int(WINDOW_HEIGHT/ASPECT_Y))
    rw, rh  = ASPECT_X*multiplier, ASPECT_Y*multiplier 
    
    rect_width, rect_height = max(ASPECT_X, find_nearest_whole_num(rw)), max(ASPECT_Y, find_nearest_whole_num(rh) )

    px, py = ceil((WINDOW_WIDTH-rect_width)/2), ceil((WINDOW_HEIGHT-rect_height)/2)

    maze_bg_rect.update(px, py, rect_width, rect_height)
    
    return (px, py, rect_width, rect_height)