class MyQueue:
  def __init__(self):
    self.queue = []
  def enqueue(self, item):
    self.queue.append(item)
  def dequeue(self):
    if len(self.queue) == 0:
      return None
    result = self.queue[0]
    del self.queue[0]
    return result

myq = MyQueue()
myq.enqueue(0)
myq.enqueue(1)
print(myq.dequeue())
print(myq.dequeue())
print(myq.dequeue())