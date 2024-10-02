import turtle
import colorsys
import math

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
canvas = turtle.Turtle()

# Initialize variables
angle = 167.5
scale = 3.5
t = 0  # Initialize t here

# Set up the turtle drawing function
def hsl_to_rgb(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h / 360, l / 100, s / 100)
    return int(r * 255), int(g * 255), int(b * 255)

def rgb_to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def draw(x, y):
    global t, scale  # Declare t and scale as global variables
    scale *= 2  # Double the size of the squares
    canvas.clear()
    for i in range(6000):
        a = i * angle
        r = scale * math.sqrt(i) + 10 * math.sin(t + i * 0.01)
        x = r * math.cos(a)
        y = r * math.sin(a)
        h = i % 360  # Calculate hue value based on i
        r, g, b = hsl_to_rgb(h, 100, 50)
        fill_color = rgb_to_hex(r, g, b)
        canvas.fillcolor(fill_color)
        canvas.penup()
        canvas.goto(x, y)
        canvas.pendown()
        canvas.begin_fill()
        canvas.forward(scale)
        canvas.left(90)
        canvas.forward(scale)
        canvas.left(90)
        canvas.forward(scale)
        canvas.left(90)
        canvas.forward(scale)
        canvas.left(90)
        canvas.end_fill()
    t += 0.01
    screen.update()

# Set up the turtle environment
canvas.speed(0)
canvas.penup()
canvas.hideturtle()

# Set the screen refresh rate to 60 FPS
screen.tracer(60)

# Bind the draw function to mouse clicks
screen.onscreenclick(draw)

# Data
data = [
    {'mes': 'enero', 'dia': '2', 'year': "2021"},
    {'mes': 'febr', 'dia': '22', 'year': "2023"},
    {'mes': 'noviembre', 'dia': '12', 'year': "2020"},
]

# Iterate over the data and print key-value pairs
for obj in data:
    for key, value in obj.items():
        print(f"{key} {value}")

# Keep the turtle graphics window open
turtle.done()
