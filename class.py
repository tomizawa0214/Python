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

# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.x = x
#         self.y = y
#     def difference(self, point=None):
#         if not point:
#             point = Point()
#         return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

# point1 = Point(1.0, 1.0)
# point2 = Point()
# point3 = Point(5, 4)

# print(point1.difference(point2))
# print(point1.difference())
# print(point3.difference(point1))

# class Point:
#     pass

# point1 = Point()
# point1.x = 1.0
# point1.y = 1.0

# point1.hello = lambda x: print('Hello', str(x))
# point1.hello('world')

# class MyClass:
#     count = 0

# print(MyClass.count)

# instance = MyClass()
# print(instance.count)

# instance.count = 100
# print(instance.count)
# print(MyClass.count)

# class MyClass:
#     count = 0

#     def __init__(self):
#         MyClass.count += 1
#         print(f'you made {MyClass.count} instance(s)')

# instance1 = MyClass()
# instance2 = MyClass()

# class MyClass:
#     count = 0

#     def __init__(self):
#         MyClass.count += 1
#         print(f'you made {MyClass.count} instance(s)')

#     @classmethod
#     def get_count(cls):
#         print(cls.count)

# MyClass.get_count()
# instance1 = MyClass()
# instance2 = MyClass()
# instance2.get_count()

# class MyClass:
#     count = 0

#     def __init__(self):
#         MyClass.count += 1
#         print(f'you made {MyClass.count} instance(s)')

#     @classmethod
#     def get_count(cls):
#         cls.another_get_count()

#     another_get_count = classmethod(lambda cls: print('count:', cls.count))

# MyClass.another_get_count()
# instance1 = MyClass()
# instance1.another_get_count()
# instance1.get_count()
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod
    def get_count(cls):
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))

    @staticmethod
    def static_get_count():
        print('count:', MyClass.count)

MyClass.static_get_count()
instance = MyClass()
instance.static_get_count()