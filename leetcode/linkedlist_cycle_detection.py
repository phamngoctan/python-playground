# Definition for singly-linked list.
class ListNode:
  def __init__(self, x, next=None):
    self.val = x
    self.next = next
  def __str__(self):
    return str(self.val)

class Solution:
  def hasCycle(self, head: ListNode) -> bool:
    if not head or not head.next:
      return False
    tortoise = head
    hare = head
    while True:
      tortoise = tortoise.next
      hare = hare.next.next if hare.next else None
      if hare == tortoise:
        return True
      elif not hare:
        return False
      

def printNode(head):
  next = head
  while next != None:
    print(f'{next}')
    next = next.next

def createCyclicLinkedList() -> ListNode:
  head = ListNode(1)
  tail = ListNode(2)
  head.next = tail
  tail.next = head
  return head

sol = Solution()
head = createCyclicLinkedList()
assert sol.hasCycle(head) == True
print('--------')

inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
assert sol.hasCycle(inputList) == False
print('--------')

inputList = ListNode(1)
assert sol.hasCycle(inputList) == False
print('--------')

inputList = ListNode(1)
assert sol.hasCycle(None) == False
