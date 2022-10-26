from maze_generator import Maze
import turtle
from maze_solver import bfs
from maze_solver import dfs

def init_turtle():
    turtle.getscreen()
    turtle.hideturtle()
    turtle.pensize(4)
    turtle.speed(0)
    turtle.up()
    turtle.goto(-300,-300)

def draw_maze(m):
    turtle.down()
    turtle.goto(-300,300)
    turtle.goto(300,300)
    turtle.up()
    turtle.goto(-270,270)
    turtle.dot(20,"blue")
    turtle.goto(-300,300)
    for row in m.cells:
        for cell in row:
            if cell.south == None and cell.east == None:
                turtle.up()
                turtle.goto(turtle.xcor(),turtle.ycor()-60)
                turtle.down()
                turtle.goto(turtle.xcor()+60,turtle.ycor())
                turtle.goto(turtle.xcor(),turtle.ycor()+60)
            elif cell.east == None:
                turtle.up()
                turtle.goto(turtle.xcor()+60,turtle.ycor())
                turtle.down()
                turtle.goto(turtle.xcor(),turtle.ycor()-60)
                turtle.up()
                turtle.goto(turtle.xcor(),turtle.ycor()+60)
            elif cell.south == None:
                turtle.up()
                turtle.goto(turtle.xcor(),turtle.ycor()-60)
                turtle.down()
                turtle.goto(turtle.xcor()+60,turtle.ycor())
                turtle.up()
                turtle.goto(turtle.xcor(),turtle.ycor()+60)
            else:
                turtle.up()
                turtle.goto(turtle.xcor()+60,turtle.ycor())
        turtle.up()
        turtle.goto(-300,turtle.ycor()-60)
    turtle.goto(270,-270)
    turtle.dot(20,"red")
    turtle.up()
    turtle.goto(-270,270)



m = Maze(10,10)
m.build_maze()
m.add_walls()
m.print_maze()
init_turtle()
draw_maze(m)

turtle.pensize(1)
turtle.color("alice blue")
bfs(m,turtle, True)

turtle.up()
turtle.goto(-270,270)
turtle.dot(20,"blue")
turtle.goto(270,-270)
turtle.dot(20,"red")

turtle.pensize(1)
turtle.color("rosy brown")
dfs(m,turtle, True)
turtle.mainloop()
