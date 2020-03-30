# print(type('a'))

# class Point:
#   pass

# point1 = Point()
# # print(type(point1))

# point1.x = 1.0
# point1.y = 1.0

# print(dir(point1))

# point2 = Point()

# class Point:
#   def __init__(self, x=0.0, y=0.0):
#     self.x = x
#     self.y = y

# point1 = Point(1.0, 1.0)
# point2 = Point()
# # print(f'point1: ({point1.x}, ({point1.y})')
# # print(f'point2: ({point2.x}, ({point2.y})')

from math import sqrt
# print(sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2))

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def difference(self, point=None):
        if not point:
            point = Point()
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

point1 = Point(1.0, 1.0)
point2 = Point()
point3 = Point(5, 4)

print(point1.difference(point2))
print(point1.difference())
print(point3.difference(point1))