class MyLinkedList:
    def __init__(self):
      self.head = None
      # self.tail = None

    def get(self, index: int) -> int:
        if index < 0:
          return -1
        head = self.head
        if index == 0:
          return head.val if head else -1
        head = self.head
        count = 0
        while head and head.next and count < index:
            head = head.next
            count += 1
        if count != index:
            return -1
        return head.val

    def addAtHead(self, val: int) -> None:
        newHead = SinglyListNode(val, self.head)
        self.head = newHead

    def addAtTail(self, val: int) -> None:
        newTail = SinglyListNode(val)
        head = self.head
        if head:
            head = self.head
            while head and head.next:
                head = head.next
            head.next = newTail
        else:
            self.head = newTail

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        head = self.head
        count = 0
        while head and head.next and count < index - 1:
            head = head.next
            count += 1
        if count < index - 1 or not head:
            return
        tmp = head.next
        head.next = SinglyListNode(val, tmp)

    def deleteAtIndex(self, index: int) -> None:
        head = self.head
        if index == 0:
          head = head.next
          self.head = head
          return
        count = 0
        while head and head.next and count < index - 1:
            head = head.next
            count += 1
        if count < index - 1 or not head.next:
            return
        deletedNode = head.next
        head.next = deletedNode.next
        deletedNode.next = None

class SinglyListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(0)
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# obj.get(1)
# obj.deleteAtIndex(1)
# obj.get(1)

# ["MyLinkedList","addAtHead","deleteAtIndex"]
# [[],[1],[0]]
# obj.addAtHead(1)
# obj.addAtHead(2)
# obj.deleteAtIndex(1)

# ["MyLinkedList","addAtHead","deleteAtIndex","addAtHead",
# "addAtHead","addAtHead","addAtHead","addAtHead",
# "addAtTail","get","deleteAtIndex","deleteAtIndex"]
# [[],[2],[1],[2],[7],[3],[2],[5],[5],[5],[6],[4]]
# obj.addAtHead(2)
# obj.deleteAtIndex(1)
# obj.addAtHead(2)
# obj.addAtHead(7)
# obj.addAtHead(3)
# obj.addAtHead(2)
# obj.addAtHead(5)
# obj.addAtTail(5)
# obj.get(5)
# obj.deleteAtIndex(6)
# obj.deleteAtIndex(4)

# ["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex",
# "addAtHead","get","get","get","addAtHead","deleteAtIndex"]
# [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]
# obj.addAtHead(4)
# obj.get(1)

# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get","get","deleteAtIndex","deleteAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1],[3],[3],[0],[0],[0],[0]]
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# obj.get(1)
# obj.deleteAtIndex(1)
# obj.get(1)
# obj.get(3)
# obj.get(3)
# obj.deleteAtIndex(0)
# obj.get(0)
# obj.deleteAtIndex(0)
# obj.get(0)

# ["MyLinkedList","addAtIndex","get"]
# [[],[1,0],[0]]
obj.addAtIndex(1, 0)
obj.get(0)