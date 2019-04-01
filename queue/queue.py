class Queue:
  def __init__(self):
    self.size = 0
    self.storage = []

  def enqueue(self, item):
    self.storage = [item] + self.storage
    self.size += 1
  
  def dequeue(self):
    if len(self.storage) > 0:
      removed_item = self.storage.pop()
      self.size -= 1
      return removed_item
      
    return None

  def len(self):
    return self.size



testQueue = Queue()
testQueue.enqueue('daren')
testQueue.enqueue('jack')
testQueue.enqueue('jill')

print("testQueue:", testQueue)
print("testQueue.storage:", testQueue.storage)
print("testQueue.size:", testQueue.size)

testQueue.dequeue()

print("testQueue.storage after dequeue:", testQueue.storage)