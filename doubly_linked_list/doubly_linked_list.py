"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev



"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = ListNode(value)

    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.insert_before(value)
      self.head = self.head.prev

    self.length += 1


  def remove_from_head(self):
    # If there is no head, just return None
    if self.head is None:
      return None

    # Store the current head before deleting it
    head_to_remove = self.head

    # Delete the current head
    self.head.delete()

    # Reassign the head to the next node in the list
    self.head = head_to_remove.next

    # if list only had 1 node, no nodes are remaining
    if self.length == 1:
      self.tail = None
      self.head = None

    self.length -= 1
    
    return head_to_remove.value

  def add_to_tail(self, value):
    new_node = ListNode(value)

    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.insert_after(value)
      self.tail = self.tail.next

    self.length += 1

  def remove_from_tail(self):
    if self.tail is None:
      return None

    previous_tail = self.tail

    self.tail.delete()

    self.tail = previous_tail.prev

    if self.length == 1:
      self.head = None
      self.tail = None

    self.length -= 1

    return previous_tail.value

  def move_to_front(self, node):
    target_node = node

    node.delete()

    self.head.insert_before(target_node.value)
    
    self.head = self.head.prev

    if target_node is self.tail:
      self.tail = target_node.prev

  def move_to_end(self, node):
    target_node = node

    node.delete()

    self.tail.insert_after(target_node.value)

    self.tail = self.tail.next

    if target_node is self.head:
      self.head = target_node.next

  def delete(self, node):
    target_node = node

    node.delete()

    if target_node is self.head:
      self.head = target_node.next
    if target_node is self.tail:
      self.tail = target_node.prev
    
    self.length -= 1
    
  def get_max(self):
    if self.head is None:
      return None

    maximum = self.head.value
    
    cur_node = self.head
    while cur_node:
      if cur_node.value > maximum:
        maximum = cur_node.value
      cur_node = cur_node.next

    return maximum



# Testing NodeList and LinkedList creation
# nodeAlex = ListNode('alex')
# nodeBrad = ListNode('brad')
# nodeCindy = ListNode('cindy')

# nodeAlex.prev = None
# nodeAlex.next = nodeBrad
# nodeBrad.prev = nodeAlex
# nodeBrad.next = nodeCindy
# nodeCindy.prev = nodeBrad
# nodeCindy.next = None

# linkedList = DoublyLinkedList(nodeAlex)
# linkedList.tail = nodeCindy

# # nodeAlex = ListNode('alex', None, nodeBrad)
# # nodeBrad = ListNode('brad', nodeAlex, nodeCindy)
# # nodeCindy = ListNode('cindy', nodeBrad, None)

# print(f'nodeAlex - value: {nodeAlex.value}, prev: {nodeAlex.prev}, next: {nodeAlex.next.value}')
# print(f'nodeBrad - value: {nodeBrad.value}, prev: {nodeBrad.prev.value}, next: {nodeBrad.next.value}')
# print(f'nodeCindy - value: {nodeCindy.value}, prev: {nodeCindy.prev.value}, next: {nodeCindy.next}')
# print(f'linkedList - head.value: {linkedList.head.value}, tail.value: {linkedList.tail.value}')

# # nodeAlex.insert_before('andy')
# # nodeAndy = ListNode('andy', None, nodeAlex)
# # linkedList.head = linkedList.head.prev

# # print(nodeAlex.prev.next.value)

# # print('---------------------------------------------------------')
# # print(f'nodeAndy - value: {nodeAndy.value}, prev: {nodeAndy.prev}, next: {nodeAndy.next.value}')
# # print(f'nodeAlex - value: {nodeAlex.value}, prev: {nodeAlex.prev.value}, next: {nodeAlex.next.value}')
# # print(f'nodeBrad - value: {nodeBrad.value}, prev: {nodeBrad.prev.value}, next: {nodeBrad.next.value}')
# # print(f'nodeCindy - value: {nodeCindy.value}, prev: {nodeCindy.prev.value}, next: {nodeCindy.next}')



# linkedList.add_to_head('andy')

# print('---------------------------------------------------------')
# print(f'nodeAndy - value: {nodeAlex.prev.value}, prev: {nodeAlex.prev.prev}, next: {nodeAlex.prev.next.value}')
# print(f'nodeAlex - value: {nodeAlex.value}, prev: {nodeAlex.prev.value}, next: {nodeAlex.next.value}')
# print(f'nodeBrad - value: {nodeBrad.value}, prev: {nodeBrad.prev.value}, next: {nodeBrad.next.value}')
# print(f'nodeCindy - value: {nodeCindy.value}, prev: {nodeCindy.prev.value}, next: {nodeCindy.next}')
# print(f'linkedList - head.value: {linkedList.head.value}, tail.value: {linkedList.tail.value}')


# linkedList2 = DoublyLinkedList()
# linkedList2.add_to_head('fred')

# print('---------------------------------------------------------')
# print(f'linkedList2 - {linkedList2.head.value}')
# print(len(linkedList))