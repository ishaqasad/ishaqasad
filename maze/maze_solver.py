from maze_generator import Maze
import turtle
import heapq as h


def bfs(Maze,turtle = None ,draw = False):
    order = []
    Maze.reset_cells()
    queue = []
    s = Maze.start
    path = []
    path.append(s)
    queue.append(path)
    s.visit()
    while queue:
        path = queue.pop(0)
        s = path[-1]

        order.append((s.i,s.j))
        if(draw):
            turtle.goto(-297 + s.j*60 ,297 - s.i*60)
            turtle.begin_fill()
            draw_rectangle()
            turtle.end_fill()
        if s.is_end:
            break
        else:
            if(s.north != None and not s.north.check_visit() ):
                new_path = list(path)
                new_path.append(s.north)
                queue.append(new_path)
                s.north.visit()
            if(s.east != None and not s.east.check_visit()):
                new_path = list(path)
                new_path.append(s.east)
                queue.append(new_path)
                s.east.visit()
            if(s.south != None and not s.south.check_visit()):
                new_path = list(path)
                new_path.append(s.south)
                queue.append(new_path)
                s.south.visit()
            if(s.west != None and not s.west.check_visit()):
                new_path = list(path)
                new_path.append(s.west)
                queue.append(new_path)
                s.west.visit()
    return order , path

def dfs(Maze,turtle = None ,draw = False):
    Maze.reset_cells()
    s = Maze.start
    order = []
    stack = []
    path = []
    path.append(s)
    stack.append(path)
    while(stack):
        path = stack.pop(-1)
        s = path[-1]
        order.append((s.i,s.j))
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
                new_path = list(path)
                new_path.append(s.north)
                stack.append(new_path)
            if(s.east != None and not s.east.check_visit()):
                new_path = list(path)
                new_path.append(s.east)
                stack.append(new_path)
            if(s.south != None and not s.south.check_visit()):
                new_path = list(path)
                new_path.append(s.south)
                stack.append(new_path)
            if(s.west != None and not s.west.check_visit()):
                new_path = list(path)
                new_path.append(s.west)
                stack.append(new_path)

    return order,path

def djikstras(Maze):
     Maze.reset_cells()
     pq = []
     s = Maze.start
     s.c = 0
     path = [s]
     h.heappush(pq,(s,path) )
     s.visit()
     order = []
     while(len(pq) != 0):
         s , path = h.heappop(pq)
         order.append((s.i,s.j))
         s.visit()
         if(s.is_end):
             break
         if(s.north != None and not s.north.check_visit() ):
             new_path = list(path)
             new_path.append(s.north)
             s.north.c = s.c+1
             h.heappush(pq,(s.north,new_path))
         if(s.east != None and not s.east.check_visit()):
             new_path = list(path)
             new_path.append(s.east)
             s.east.c = s.c+1
             h.heappush(pq,(s.east,new_path))
         if(s.south != None and not s.south.check_visit()):
             new_path = list(path)
             new_path.append(s.south)
             s.south.c = s.c+1
             h.heappush(pq,(s.south,new_path))
         if(s.west != None and not s.west.check_visit()):
             new_path = list(path)
             new_path.append(s.west)
             s.west.c = s.c+1
             h.heappush(pq,(s.west,new_path))
     return order , path
def a_star(Maze):
    Maze.reset_cells()
    pq = []
    s = Maze.start
    s.c = Maze.height - s.i +  Maze.width - s.j
    path = [s]
    h.heappush(pq,(s,path) )
    s.visit()
    order = []
    while(len(pq) != 0):
        s , path = h.heappop(pq)
        order.append((s.i,s.j))
        s.visit()
        if(s.is_end):
            break
        if(s.north != None and not s.north.check_visit() ):
            new_path = list(path)
            new_path.append(s.north)
            s.north.c = Maze.height - s.i +  Maze.width - s.j
            h.heappush(pq,(s.north,new_path))
        if(s.east != None and not s.east.check_visit()):
            new_path = list(path)
            new_path.append(s.east)
            s.east.c = Maze.height - s.i +  Maze.width - s.j
            h.heappush(pq,(s.east,new_path))
        if(s.south != None and not s.south.check_visit()):
            new_path = list(path)
            new_path.append(s.south)
            s.south.c = Maze.height - s.i +  Maze.width - s.j
            h.heappush(pq,(s.south,new_path))
        if(s.west != None and not s.west.check_visit()):
            new_path = list(path)
            new_path.append(s.west)
            s.west.c = Maze.height - s.i +  Maze.width - s.j
            h.heappush(pq,(s.west,new_path))
    return order , path
if __name__ == '__main__':
    m = Maze(10,10)
    m.build_maze()
    m.add_walls()
    m.print_maze()

    order , path  = djikstras(m)
    print(order)
