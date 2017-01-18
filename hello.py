# connect the Turtle and random libraries (aka "modules")
import turtle, random

# let's make a turtle
tina = turtle.Turtle()
tina.speed(10000)

# list of colors
colors = ["pink", "blue", "green", "orange", "aqua", "brown", "gold", "red", "moroon"]


def color_tina():
    pick = random.randint(0, len(colors) - 1)
    tina.color(colors[pick])


def draw_diamond(some_turtle):
    some_turtle.left(30)
    some_turtle.forward(50)
    some_turtle.right(60)
    some_turtle.forward(50)
    some_turtle.right(120)
    some_turtle.forward(50)
    some_turtle.right(60)
    some_turtle.forward(50)
    some_turtle.right(150)


def draw_art():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(0)

    for i in range(0, 36):
        draw_diamond(brad)
        brad.right(10)

    brad.right(90)
    brad.forward(200)

    window.exitonclick()


draw_art()


def triangle(size):
    tina.goto(150, 100)
    color_tina()
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)


'''
def star(size):
   color_tina()
   tina.forward(size)
   tina.right(220)
   tina.forward(size)
   tina.left(100)
   tina.forward(size)
   tina.right(120)
   tina.forward(size)
   tina.left(100)
   tina.forward(size)
   tina.right(120)
   tina.forward(size)
   tina.left(500)
   tina.forward(size)
   tina.right(90)
   tina.forward(size)
'''


def draw_star(size):
    pick = random.randint(0, len(colors) - 1)
    angle = 120
    turtle.fillcolor(colors[pick])
    turtle.begin_fill()

    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    turtle.end_fill()
    return


def octagon(size):
    color_tina()
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)


def octagons(size, num):
    for x in range(1, num):
        octagon(size * x)


# let's make some methods, like plays in a playbook
def square(some_turtle):
    # stop writing
    some_turtle.penup()
    # go to the middle
    some_turtle.goto(0, 0)
    # start writing
    some_turtle.pendown()
    # go up
    some_turtle.goto(0, 50)
    # go right
    some_turtle.goto(50, 50)
    # go down
    some_turtle.goto(50, 0)
    # go back to the start
    some_turtle.goto(0, 0)


def super_circles(size):
    for x in range(1, 10):
        color_tina()
        tina.circle(size * x)


square(tina)

tina.goto(25, 0)
tina.circle(25)

octagons(5, 20)

draw_star(75)

super_circles(2)

tina.goto(100, 100)
for x in range(10, 100, 5):
    triangle(x)

answer = input("What next?")
print("You just said:" + answer)
if answer == "triangle":
    draw_triangle(50)
elif answer == "super circles":
    super_circles(4)
elif answer == "move":
    tina.goto(random.randint(-200, 200), random.randint)
elif answer == "star":
    draw_star(60)
else:
    print("I don't know how to do that.")