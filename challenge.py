# coding:utf-8

class A:
    def say_a(self):
        print("A!")
    def say_hi(self):
        print("hi! from A!")
class B:
    def say_b(self):
        print("B!")
    def say_hi(self):
        print("hi! from B!")

class C(B, A):
    pass

c = C()
c.say_hi()

