class Node:
  def __init__(self, data):
    self.item = data
    self.next = None

class MyLinkedList:
  def __init__(self):
    self.start_node = None

  def traverse_list(self):
    if self.start_node is None:
      print("List has no element")
      return
    else:
      n = self.start_node
      while n is not None:
        print(n.item, " ")
        n = n.next

  def insert_at_start(self, data):
    new_node = Node(data)
    new_node.next = self.start_node
    self.start_node = new_node

my_linked_list = MyLinkedList()
my_linked_list.insert_at_start(3)
my_linked_list.insert_at_start(4)
my_linked_list.insert_at_start(5)
my_linked_list.traverse_list()

