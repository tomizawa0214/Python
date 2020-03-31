class MyStack:
    def __init__(self):
      self.stack = []
    def push(self, item):
      self.stack.append(item)
    def pop(self):
      return self.stack.pop()

# class MyStack3(list):
#     def push(self, item):
#         self.append(item)

# mystack = MyStack3()
# mystack.push(1)
# mystack.push(2)
# mystack.push(3)
# mystack.push(4)
# mystack.push(5)
# print(mystack)
# print(mystack.pop())
# print(mystack.pop())
# for item in mystack:
#     print(item)
# print(mystack[1:])

# print('MyStack:', dir(MyStack))
# print('---')
# print('MyStack3:', dir(MyStack3))

# class MyStack3(list):
#     def __init__(self, *args):
#         # print(args) # 可変長位置引数を確認したければコメントアウト
#         super(). __init__(args)
#     def push(self, item):
#         self.append(item)

# mystack = MyStack3()
# # print(mystack)
# mystack = MyStack3(1)
# # print(mystack)
# mystack = MyStack3([1, 2, 3])
# # print(mystack)
# mystack = MyStack3(1, 2, 3)
# # print(mystack)
# mystack = MyStack3(1, 2, [3, 4])
# # print(mystack)

# mystack2 = mystack.copy()
# print(type(mystack2))

class MyStack3(list):
    def __init__(self, *args):
        # print(args)
        super(). __init__(args)
    def push(self, item):
        self.append(item)
    def copy(self):
        tmp = list.copy(self)
        return MyStack3(*tmp)

mystack = MyStack3(1, 2, [3, 4])
print(mystack)
mystack2 = mystack.copy()
print(type(mystack2))
print('mystack:', mystack)
print('mystack2:', mystack2)
print('mystack == mystack2:', mystack == mystack2)
print('mystack is mystack2:', mystack is mystack2)