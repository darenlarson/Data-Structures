class Heap:
  def __init__(self):
    self.storage = []
    # self.storage = [100,36,28,30,10,15,19,27,3,2,5]

  def insert(self, value):
    # Insert the value to the end of the storage array.
    self.storage.append(value)

    # Save the index the new value is stored at.
    cur_index = len(self.storage) - 1

    # Find the index of the parent node for the new value using the provided formula.
    parent_index = int((cur_index - 1) / 2)

    # Stops looping if we reach the beginning of the heap's storage array or no swap occurs.
    swap = True
    while cur_index > 0 and swap == True:
      swap = False

      # Swap the parent and child values if child > parent.
      if self.storage[cur_index] > self.storage[parent_index]:
        # Store the parent and child values in variables so we don't lose them. Don't need to store both, but doing for clarity right now.
        parent = self.storage[parent_index]
        child = self.storage[cur_index]

        # Move the parent value to the child's index.
        self.storage[cur_index] = parent

        # Move the child value to the parent's index.
        self.storage[parent_index] = child

        # Reset the cur_index to the parent_index bc that's now where our new value is.
        cur_index = parent_index

        # Find the new index of the parent node for the new value using the provided formula.
        parent_index = int((cur_index - 1) / 2)

        # Set wap to True so that it can loop again.
        swap = True


  def delete(self):
    removed_item = self.storage[0]

    # Replace the first item in the heap's storage array with the last item.
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()

    # Initialize the parent_index to the first item in the list
    parent_index = 0

    # Stops looping if we reach the end of the heap's storage array or no swap occurs.
    swap = True
    while parent_index < len(self.storage) - 1 and swap == True:
      swap = False

      # Define the indexes of the parent, left child, and right child using provided formulas.
      left_child_index = (2 * parent_index) + 1
      right_child_index = (2 * parent_index) + 2

      # Define the values at those indexes.
      parent = self.storage[parent_index]
      if left_child_index < len(self.storage):
        left_child = self.storage[left_child_index]
      else:
        left_child = None
      if right_child_index < len(self.storage):
        right_child = self.storage[right_child_index]
      else:
        right_child = None

      # Find which child is the largest.
      if left_child is not None and right_child is not None:
        if left_child > right_child:
          largest_child_index = left_child_index
          largest_child = left_child
        else:
          largest_child_index = right_child_index
          largest_child = right_child
      elif left_child is None:
        largest_child_index = right_child_index
        largest_child = right_child
      elif right_child is None:
        largest_child_index = left_child_index
        largest_child = left_child
      else:
        largest_child = None

      # Swap the parent and largest child if the largest child is larger.
      if largest_child is not None:
        if largest_child > parent:
          # Swapping the values
          self.storage[parent_index] = largest_child
          self.storage[largest_child_index] = parent

          # Reseting the parent_index to the current position of the value so we can do this process again.
          parent_index = largest_child_index

          # Set wap to True so that it can loop again.
          swap = True

    return removed_item
  
  # def delete(self):
  #   removed_item = self.storage[0]

  #   # Replace the first item in the heap's storage array with the last item.
  #   self.storage[0] = self.storage[len(self.storage) - 1]
  #   self.storage.pop()

  #   # Initialize the parent_index to the first item in the list
  #   parent_index = 0

  #   swap = True
  #   while swap == True:
  #     swap = False
  #     largest = self._sift_down(parent_index)

  #     if largest is not None:
  #       parent_index = largest
  #       swap = True

  #   return removed_item


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    # Find the parent index using provided formula
    parent_index = int((index - 1) / 2)

    # Make sure parent exists and store it in a variable
    if parent_index < len(self.storage):
      parent = self.storage[parent_index]
    else:
      return

    # Store the child value
    if index < len(self.storage):
      child = self.storage[index]
    else:
      return

    # Swap child and parent if child is greater than parent
    if child > parent:
      self.storage[parent_index] = child
      self.storage[index] = parent

  def _sift_down(self, index):
    # Find and store the indexes of the children of the parent
    left_child_index = (2 * index) + 1
    right_child_index = (2 * index) + 2

    # Save the value of the parent
    if index < len(self.storage):
      parent = self.storage[index]
    else:
      return

    # Check to see if the index is within range of self.storage
    if left_child_index < len(self.storage):
      # Save the value of the left child
      left_child = self.storage[left_child_index]
    else:
      # If index is not in range, left child is None
      left_child = None

    # Check to see if the index is within range of self.storage
    if right_child_index  < len(self.storage):
      # Save the value of the right child
      right_child = self.storage[right_child_index]
    else:
      # If index is not in range, right child is None
      right_child = None

    # If both a left and right child exist...
    if left_child is not None and right_child is not None:
      # Check to see which child is larger and save that value and index
      if left_child >= right_child:
        largest_child_index = left_child_index
        largest_child = left_child
      else:
        largest_child_index = right_child_index
        largest_child = right_child
    # If one of the children is None, but the other exists, save that one as largest
    elif left_child is None and right_child is not None:
      largest_child = right_child
    elif right_child is None and left_child is not None:
      largest_child = left_child
    else:
      largest_child = None

    if largest_child is not None:
      if parent < largest_child:
        self.storage[index] = largest_child
        self.storage[largest_child_index] = parent

        return largest_child_index

    return None


"""
###### Tests #####
test = Heap()
test.insert(101)
print(test.storage)
test.delete()
print(test.storage)
"""