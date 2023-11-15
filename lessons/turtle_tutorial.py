from turtle import Turtle, colormode, done



leo: Turtle = Turtle()

i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1

leo.penup()
leo.goto(45, 60)
leo.pendown()
 
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1



# Create a function to draw a planet
def draw_planet(color, radius, distance):
    planet = Turtle.Turtle()
    planet.shape("circle")
    planet.color(color)
    planet.shapesize(stretch_wid=0.5)
    planet.penup()
    planet.goto(distance, 0)
    return planet

# Create the sun
sun = Turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(stretch_wid=3)

# Create Earth and Moon
earth = draw_planet("blue", 150, 150)
moon = draw_planet("gray", 30, 30)

# Function to move the planets
def move_planet(planet, distance, angle):
    planet.goto(distance * 10, 0)
    planet.setheading(angle)

# Animate the solar system
angle = 0
while True:
    move_planet(earth, 150, angle)
    move_planet(moon, 30, angle * 1.5)
    angle += 0.1

done()