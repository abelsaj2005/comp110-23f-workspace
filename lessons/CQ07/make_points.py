"""Instatiating the class Point."""


from lessons.CQ07.point import Point

my_point: Point = Point(5, 4)

print(my_point.x)
print(my_point.y)

my_point.scale_by(5)
print(my_point.x)
print(my_point.y)

my_second_point: Point = my_point.scale(5)
print(my_second_point.x)
print(my_second_point.y)

my_point: Point = Point(1.0, 2.0)
print(str(my_point))