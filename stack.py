# class MyStack:
#   def __init__(self):
#     self.stack = []
#   def push(self, item):
#     self.stack.append(item)
#   def pop(self):
#     result = self.stack[-1]
#     del self.stack[-1]
#     return result

# mystack = MyStack()
# mystack.push(0)
# mystack.push(1)
# print(mystack.pop())
# print(mystack.pop())

class MyStack:
  def __init__(self):
    self.stack = []
  def push(self, item):
    self.stack.append(item)
  def pop(self):
    if len(self.stack) == 0:
      return None
    return self.stack.pop()

mystack = MyStack()
mystack.push(0)
print(mystack.pop())
print(mystack.pop())