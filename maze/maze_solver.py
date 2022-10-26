from maze_generator import Maze
import turtle
def draw_rectangle():
    for i in range(2):
        turtle.forward(55)
        turtle.right(90)
        turtle.forward(55)
        turtle.right(90)

def bfs(Maze,turtle = None ,draw = False):
    Maze.reset_cells()
    queue = []
    s = Maze.start
    queue.append(s)
    s.visit()
    while queue:
        s = queue.pop(0)
        if(draw):
            turtle.goto(-297 + s.j*60 ,297 - s.i*60)
            turtle.begin_fill()
            draw_rectangle()
            turtle.end_fill()
        if s.is_end:
            break
        else:
            if(s.north != None and not s.north.check_visit() ):
                queue.append(s.north)
                s.north.visit()
            if(s.east != None and not s.east.check_visit()):
                queue.append(s.east)
                s.east.visit()
            if(s.south != None and not s.south.check_visit()):
                queue.append(s.south)
                s.south.visit()
            if(s.west != None and not s.west.check_visit()):
                queue.append(s.west)
                s.west.visit()


def dfs(Maze,turtle = None ,draw = False):
    Maze.reset_cells()
    s = Maze.start
    stack = []
    stack.append(s)
    while(stack):
        s = stack.pop(-1)
        s.visit()
        if(draw):
            turtle.goto(-297 + s.j*60 ,297 - s.i*60)
            turtle.begin_fill()
            draw_rectangle()
            turtle.end_fill()
        if(s.is_end):
            break
        else:
            if(s.north != None and not s.north.check_visit() ):
                stack.append(s.north)
            if(s.east != None and not s.east.check_visit()):
                stack.append(s.east)
            if(s.south != None and not s.south.check_visit()):
                stack.append(s.south)
            if(s.west != None and not s.west.check_visit()):
                stack.append(s.west)


if __name__ == '__main__':

