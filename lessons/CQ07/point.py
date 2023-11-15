"""Defining the class Point."""
from __future__ import annotations


class Point:
    """This is the class to represent a point."""
    # attributes
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0) -> None:
        """Constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method to scale each x and y point by a certain factor."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Method that creates a new point with a scaled factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Overrides the str method."""
        point_str: str = f"x: {self.x}; y: {self.y}"
        return point_str
    
    def __mul__(self, factor: int | float) -> Point:
        """Overrides the mul method."""
        new_mul_point: Point = Point(self.x * factor, self.y * factor)
        return new_mul_point

    def __add__(self, factor: int | float) -> Point:
        """Overrides the add method."""
        new_add_point: Point = Point(self.x + factor, self.y + factor)
        return new_add_point