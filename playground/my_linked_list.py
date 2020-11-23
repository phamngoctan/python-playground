class Node:
  def __init__(self, data):
    self.value = data
    self.next = None
  
class MyLinkedList:
  def __init__(self):
    self.root = None
    self.tail = None
  
  def add_to_front(self, data):
    node = Node(data)
    node.next = self.root
    self.root = node
    if self.tail is None:
      self.tail = node

  def add_to_tail(self, data):
    node = Node(data)
    if self.root is None:
      self.root = node
    
    if self.tail is None:
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node

  def reverse_from_root(self, tail = None):
    return self.__reverse(self.root, tail)
  
  def __reverse(self, node, tail = None):
    if node == self.root:
      self.tail = node

    if node is None:
      self.root = tail
      return tail
    else:
      next_node = node.next
      node.next = tail
      tail = node
      return self.__reverse(next_node, tail)
  
  def print_all(self):
    if self.root is None:
      print("No item inside")
    else:
      cur = self.root
      while cur is not None:
        print(" " + str(cur.value))
        cur = cur.next

myLinkedList = MyLinkedList()
# myLinkedList.add_to_front(3)
# myLinkedList.add_to_front(2)
# myLinkedList.add_to_front(1)
# myLinkedList.add_to_front(0)
print("try to print empty MyLinkedList")
myLinkedList.print_all()
# stdin = list(map(int, input().split()))
# for i in stdin:
#   myLinkedList.add_to_tail(i)
print("====================")
myLinkedList.add_to_tail(1)
myLinkedList.add_to_tail(2)
myLinkedList.add_to_tail(3)

myLinkedList.print_all()
# myLinkedList.reverse()
myLinkedList.reverse_from_root()
print("after reversed")
myLinkedList.print_all()
print("====================")
print("after reversed and adding new item: 4")
myLinkedList.add_to_tail(4)
myLinkedList.print_all()
myLinkedList.reverse_from_root()
print("after reversed")
myLinkedList.print_all()