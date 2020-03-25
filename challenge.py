# coding:utf-8

class User:
    count = 0
    def __init__(self, name):
        User.count += 1 
        self.name = name

print(User.count)
tom = User("tom")
bob = User("bob")
print(User.count)

print(tom.count)
