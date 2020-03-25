# coding:utf-8

def say_hi(name, age = 20):
    print("hi{0} ({1})".format(name, age))

say_hi("tomi", 23)
say_hi("bob", 21)
say_hi("steve")
say_hi(age = 18, name = "rick")
