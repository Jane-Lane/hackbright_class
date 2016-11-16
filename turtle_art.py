import turtle
import math

window = turtle.Screen()
window.bgcolor("black")

def make_star (new_turtle):
    new_turtle.pendown()
    for x in range(5):
        new_turtle.forward(200)
        new_turtle.left(18) #Makes the stamp face directly outward.
        new_turtle.stamp()
        new_turtle.left(198)
    new_turtle.penup()

def circumscribe(new_turtle):
    new_turtle.pendown()
    radius = 100/math.cos(math.pi/10) #radius from center of star to its tip.
    new_turtle.right(108)
    new_turtle.circle(radius)
    new_turtle.left(108)
    new_turtle.penup()


def displace(new_turtle):
    new_turtle.penup()
    radius = 100/math.cos(math.pi/10) #radius from center of star to its tip.
    new_turtle.right(108) #Faces perpendicular to directly outward.
    new_turtle.circle(radius, 18)
    new_turtle.left(108)
    new_turtle.pendown()

def main():
    sarita = turtle.Turtle()
    sarita.shape('turtle')
    sarita.color('yellow')
    sarita.speed('slow')

    make_star(sarita)
    displace(sarita)
    sarita.color('blue')
    make_star(sarita)
    displace(sarita)
    sarita.color('purple')
    make_star(sarita)
    displace(sarita)
    sarita.color('red')
    make_star(sarita)

    #To make a circle through all the points:
    #sarita.color('white')
    #circumscribe(sarita)

if __name__ == "__main__":
    main()


window.exitonclick()
