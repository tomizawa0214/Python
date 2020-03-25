# coding:utf-8


msg = "hello"

def say_hi():
    global msg
    msg = "hello global"
    print(msg)
    
say_hi()
print(msg)
