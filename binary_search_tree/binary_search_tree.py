class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    new_node = BinarySearchTree(value)

    if value < self.value:
      if not self.left:
        self.left = new_node
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_node
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
      return True

    elif target < self.value:
      if not self.left:
        return False
      elif target == self.left.value:
        return True
      else:
        self.left.contains(target)
    
    elif target > self.value:
      if not self.right:
        return False
      elif target == self.right.value:
        return True
      else:
        self.right.contains(target)
    
    return False
        
  def get_max(self):
    current_node = self

    while current_node:
      if not current_node.right:
        return current_node.value
      else:
        current_node = current_node.right

  def for_each(self, cb):
    cb(self.value)

    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

"""
test = BinarySearchTree(20)
test.insert(10)
test.insert(30)
test.insert(5)
test.insert(15)
test.insert(25)
test.insert(35)
print(f'          {test.value}')
print(f'     {test.left.value}         {test.right.value}')
print(f'   {test.left.left.value}   {test.left.right.value}     {test.right.left.value}  {test.right.right.value}')

print("max:", test.get_max())

def add_one(num):
  return num + 1

test.for_each(add_one)

print(f'-----------------------After running add_one-----------------------')
print(f'          {test.value}')
print(f'     {test.left.value}         {test.right.value}')
print(f'   {test.left.left.value}   {test.left.right.value}     {test.right.left.value}  {test.right.right.value}')

print("max:", test.get_max())
"""