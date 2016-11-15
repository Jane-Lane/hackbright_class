import turtle
window = turtle.Screen()
window.bgcolor("black")

def make_star (new_turtle):
    new_turtle.pendown()
    for x in range(5):
        new_turtle.forward(200)
        new_turtle.left(36)
        new_turtle.stamp()
        new_turtle.left(180)
    new_turtle.penup


sarita = turtle.Turtle()
sarita.shape('turtle')
sarita.color('yellow')
sarita.speed('slowest')

make_star(sarita)

sarita.color('blue')
make_star(sarita)
sarita.color('purple')
make_star(sarita)
sarita.color('red')
make_star(sarita)

window.exitonclick()
