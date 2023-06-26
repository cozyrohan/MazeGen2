import json
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
##### 
from gridManager import set_grid_dimensions, GRID_X, GRID_Y
from maze import do_bfs, solve_bfs,do_random_prims

set_grid_dimensions(x = 20, y = 20)


app = FastAPI()
'''
@decorator(arg)
def func()

= 

func = decorator(func)
'''






'''     root = app.get("/", root)      '''






@app.get("/")
async def root():    # async means that root is a coroutine 
    return {"app":"This is the get maze api. Specify algo from {bfs, prims_random} and square dimiensions (x,y)"}    #return some json: which is a dict type basically {key : val}


class MazeInfo(BaseModel):
    x : int
    y : int

@app.post("/maze/gen/bfs")
def prep_bfs( info: MazeInfo ):
    x,y = info
    print(" before x,y: ",GRID_X, GRID_Y)
    set_grid_dimensions(x,y)
    print(" after x,y: ",GRID_X, GRID_Y)

@app.get("/maze/gen/bfs")
def gen_bfs_maze(): 
    print("x,y: ",GRID_X, GRID_Y)
    maze = do_bfs()     # only send a response when it is done cooking (aka the maze is done being generated)
    sol = solve_bfs()
    return {"maze" : maze, "solution": sol}

if __name__ == "__main__":
    pass