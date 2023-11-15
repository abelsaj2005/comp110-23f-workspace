"""This program draws a valley where there is a house and some mountains with a sunrise."""
__author__ = "730673903"
 
from turtle import Turtle, done 


def main() -> None:
    """The entrypoint of my scene."""
    # Initializes the object.
    abel: Turtle = Turtle()

    background(abel, -400, 400, "peach puff")
    sun(abel, 10, -25, 120)
    background(abel, -400, 0, "green")
    
    # Draws the house building with a roof and window.
    house_building(abel, -200, -250, 100, "white")
    house_roof(abel, -200, -150, 100)
    house_windows(abel, -185, -175)
    house_windows(abel, -135, -175)

    # Draws the house building with a roof and window.
    house_building(abel, 0, -250, 100, "white")
    house_roof(abel, 0, -150, 100)
    house_windows(abel, 15, -175)
    house_windows(abel, 65, -175)

    # Draws four mountains that cover up the sun. "Peru" is the color of the mountains since "light brown" wasn't available.
    mountains(abel, -400, 0, "peru")
    mountains(abel, -275, 0, "peru")
    mountains(abel, 25, 0, "peru")
    mountains(abel, 150, 0, "peru")
    # Ensures that the scene is not closing immediately after being run.
    done()


def background(abel: Turtle, x: float, y: float, color: str) -> None:
    """Sets up the background for the scene."""
    abel.penup()
    abel.goto(x, y)
    abel.setheading(0.0)
    abel.pendown()
    abel.begin_fill()
    abel.fillcolor(color)
    for i in range(2):
        abel.forward(800)
        abel.right(90)
        abel.forward(400)
        abel.right(90)
    abel.end_fill()


def house_building(abel: Turtle, x: float, y: float, width: float, color: str) -> None:
    """Draws the basic house building structure."""
    abel.penup()
    abel.pencolor("black")
    abel.goto(x, y)
    abel.setheading(0.0)
    abel.pendown()
    abel.begin_fill()
    abel.fillcolor(color)
    for i in range(4):
        abel.forward(width)
        abel.left(90)
    abel.end_fill()


def house_roof(abel: Turtle, x: float, y: float, width: float) -> None:
    """Adds a roof on top of the basic house building."""
    abel.penup()
    abel.goto(x, y)
    abel.setheading(0.0)
    abel.pendown()
    abel.begin_fill()
    abel.fillcolor("brown")
    for i in range(3):
        abel.forward(width)
        abel.left(120)
    abel.end_fill()
    

def house_windows(abel: Turtle, x: float, y: float) -> None:
    """Adds windows to the house."""
    abel.penup()
    abel.pencolor("black")
    abel.goto(x, y)
    abel.setheading(0.0)
    abel.pendown()
    abel.begin_fill()
    abel.fillcolor("grey")
    index: int = 0
    while index < 4:
        abel.forward(20)
        abel.right(90)
        index += 1
    abel.end_fill()

    
def mountains(abel: Turtle, x: float, y: float, color: str) -> None:
    """Draws mountains that will overlap the sun to give it the illusion that the sun is rising."""
    abel.penup()
    abel.pencolor("brown")
    abel.goto(x, y)
    abel.setheading(0.0)
    abel.pendown()
    abel.begin_fill()
    abel.fillcolor(color)
    index: int = 0
    while index < 3:
        abel.forward(265)
        abel.left(120)
        index += 1
    abel.end_fill()


def sun(abel: Turtle, x: float, y: float, radius: float) -> None:
    """Draws a sun with a red border and orange fill in. This is me trying to go above and beyond."""
    abel.penup()
    abel.pencolor("red")
    abel.goto(x, y)
    abel.setheading(0.0)
    abel.pendown()
    abel.begin_fill()
    abel.fillcolor("orange")
    abel.circle(radius)
    abel.end_fill()


if __name__ == "__main__":
    main()