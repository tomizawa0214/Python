class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'Mystack(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)
    def __iter__(self):
        return iter(self.stack)
    def __getitem__(self, key):
        return self.stack[key]

mystack = MyStack(1, 2, [3, 4])
print(mystack[0])
print(mystack[0:2])