# Definition for singly-linked list.
from typing import List


class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def detectCycle(self, head):
    slow = fast = head
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if slow == fast: break
    
    if not fast or not fast.next: return None
    slow = head
    while slow != fast:
      slow = slow.next
      fast = fast.next
    return slow
  
  def detectCycle_myCode(self, head: ListNode) -> ListNode:
    if not head or (head and head.next == None):
      return None
    # phase one, finding the tortoise
    tortoise = head.next
    hare = head.next.next
    while tortoise != hare:
      if tortoise == None or hare == None or hare.next == None:
        return None
      tortoise = tortoise.next
      hare = hare.next.next
      
    tortoise = head
    while tortoise != hare:
      tortoise = tortoise.next
      hare = hare.next
    return hare

sol = Solution()
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next
assert sol.detectCycle(head) == head.next

head = ListNode(1)
head.next = head
assert sol.detectCycle(head) == head

head = ListNode(1)
assert sol.detectCycle(head) == None
