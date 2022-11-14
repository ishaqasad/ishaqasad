import random

class Cell:
    def __init__ (self,index_i , index_j,north = None, east = None , south = None, west = None, c= 100000000):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.i = index_i
        self.j = index_j
        self.is_visited = False
        self.is_start = False
        self.is_end = False
        self.c = c
    def add_neighbour(self,cell, direction):
        if(direction == 0):
            self.north = cell
        elif(direction == 1):
            self.east = cell
        elif(direction == 2):
            self.south = cell
        elif(direction == 3):
            self.west = cell
    def get_neighbour(self,direction):
        if(direction == 0):
            return self.north
        elif(direction == 1):
            return self.east
        elif(direction == 2):
            return self.south
        elif(direction == 3):
            return self.west
    def visit(self):
        self.is_visited = True
    def check_visit(self):
        return self.is_visited
    def add_wall(self,direction):
        if(direction == 0):
            self.north = None
        elif(direction == 1):
            self.east = None
        elif(direction == 2):
            self.south = None
        elif(direction == 3):
            self.west = None
    def reset_visit(self):
        self.is_visited = False
    def set_start(self):
        self.is_start = True
    def set_end(self):
        self.is_end = True
    def __lt__(self,other):
        return self.c <= other.c
    def __gt__(self,other):
        return self.c > other.c
class Maze:
    def __init__ (self, height, width):
        self.height = height
        self.width = width

    def build_maze(self):
        self.cells = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Cell(i,j))
            self.cells.append(row)
        self.cells[0][0].set_start()
        self.cells[-1][-1].set_end()
        self.start = self.cells[0][0]
        self.end = self.cells[-1][-1]

    def add_walls(self):
        i = random.randint(0,self.height-1)
        j = random.randint(0,self.width-1)
        cell = self.cells[i][j]
        cell.visit()
        count = 1
        while(count < self.width * self.height):
            choice = []
            if(i != 0):
                choice.append((i-1,j))
            if(j != 0):
                choice.append((i,j-1))
            if(i != self.height -1):
                choice.append((i+1,j))
            if(j != self.width -1):
                choice.append((i,j+1))
            n_i, n_j = random.choice(choice)
            next_cell = self.cells[n_i][n_j]
            if(not next_cell.check_visit()):
                count += 1
                if(i - n_i == -1):
                    cell.south = next_cell
                    next_cell.north = cell
                if(i - n_i == 1):
                    cell.north = next_cell
                    next_cell.south = cell
                if(j-n_j == -1):
                    cell.east = next_cell
                    next_cell.west = cell
                if(j-n_j == 1):
                    cell.west = next_cell
                    next_cell.east = cell
                next_cell.visit()
            cell = next_cell
            i = n_i
            j = n_j
    def print_maze(self):
        print(" "+ "_,"*self.width)
        for i in range(self.height):
            s = "|"
            for j in range(self.width):
                if self.cells[i][j].south == None and self.cells[i][j].east == None:
                    s += "_|"
                elif self.cells[i][j].east == None:
                    s+= " |"
                elif self.cells[i][j].south == None:
                    s+= "_,"
                else:
                    s+= "  "
            print(s)
    def reset_cells(self):
        for row in self.cells:
            for cell in row:
                cell.reset_visit()
    def set_start(self, i,j):
        self.start.is_start = False
        self.cells[i][j].set_start()
        self.start = self.cells[i][j]
if __name__ == '__main__':
    m = Maze(10,10)
    m.build_maze()
    m.add_walls()
    m.print_maze()
