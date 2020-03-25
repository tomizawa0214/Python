# coding:utf-8

class User:
    def __init__(self, name):
        self.name = name

tom = User("tom")
bob = User("bob")

print(tom.name)
print(bob.name)
