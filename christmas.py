import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("Merry Christmas")
screen.setup(width=800, height=600)

# Create the turtle for drawing the tree
tree = turtle.Turtle()
tree.speed(0)
tree.hideturtle()

# Create the turtle for snowflakes
snow = turtle.Turtle()
snow.hideturtle()
snow.speed(0)
snow.color("white")

# Create the turtle for text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.color("white")

# Function to draw a triangle for the tree
def draw_triangle(t, x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.goto(x + width / 2, y - height)
    t.goto(x - width / 2, y - height)
    t.goto(x, y)
    t.end_fill()

# Function to draw snowflakes outside the tree
def draw_snowflakes():
    for _ in range(50):  # Adjust the number of snowflakes
        snow.penup()
        snow.goto(random.randint(-400, 400), random.randint(-300, 300))
        snow.pendown()
        snow.dot(random.randint(3, 5))

# Draw the Christmas tree
levels = 5
base_width = 200
base_height = 50
x, y = 0, 200  # Starting position for the top of the tree
for i in range(levels):
    draw_triangle(tree, x, y, base_width, base_height, "green")
    y -= base_height - 10  # Adjust overlap between levels
    base_width += 30

# Draw the tree trunk
trunk_width = 40
trunk_height = 60
tree.penup()
tree.goto(-trunk_width / 2, y)
tree.pendown()
tree.fillcolor("brown")
tree.begin_fill()
for _ in range(2):
    tree.forward(trunk_width)
    tree.right(90)
    tree.forward(trunk_height)
    tree.right(90)
tree.end_fill()

# Draw snowflakes outside the tree
draw_snowflakes()

# Draw the star on top of the tree
def draw_star(x, y, size, color):
    star = turtle.Turtle()
    star.speed(0)
    star.color(color)
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()
    star.hideturtle()

draw_star(-14, 230, 30, "yellow")

# Draw the "Merry Christmas" message
def draw_text():
    text_turtle.penup()
    text_turtle.goto(0, -250)
    text_turtle.write("Merry Christmas!", align="center", font=("Courier", 24, "bold"))

draw_text()

# Keep the window open
turtle.done()
