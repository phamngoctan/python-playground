from typing import Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next: return None # only one item linkedlist
    slow, fast = head, head.next.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    slow.next = slow.next.next
    return head
    
  def deleteMiddle_myIdea(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head.next: return None # only one item linkedlist
    preSlow = None
    slow = fast = head
    while fast and fast.next:
      preSlow = slow
      slow = slow.next
      fast = fast.next.next
    preSlow.next = slow.next
    return head
    
sol = Solution()
head = fromArrayToListNode([1,3,4,7,1,2,6])
expect = fromArrayToListNode([1,3,4,1,2,6])
actual = sol.deleteMiddle(head)
assert actual.val == expect.val
assert actual.next.val == expect.next.val
assert actual.next.next.val == expect.next.next.val
assert actual.next.next.next.val == expect.next.next.next.val
assert actual.next.next.next.next.val == expect.next.next.next.next.val
assert actual.next.next.next.next.next.val == expect.next.next.next.next.next.val
assert actual.next.next.next.next.next.next == None

head = fromArrayToListNode([1,3,4,1,2,6])
expect = fromArrayToListNode([1,3,4,2,6])
actual = sol.deleteMiddle(head)
assert actual.val == expect.val
assert actual.next.val == expect.next.val
assert actual.next.next.val == expect.next.next.val
assert actual.next.next.next.val == expect.next.next.next.val
assert actual.next.next.next.next.val == expect.next.next.next.next.val
assert actual.next.next.next.next.next == None

head = fromArrayToListNode([1,3,4])
expect = fromArrayToListNode([1,4])
actual = sol.deleteMiddle(head)
assert actual.val == expect.val
assert actual.next.val == expect.next.val
assert actual.next.next == None

head = fromArrayToListNode([1,3])
expect = fromArrayToListNode([1])
actual = sol.deleteMiddle(head)
assert actual.val == expect.val
assert actual.next == None

head = fromArrayToListNode([1])
expect = None
actual = sol.deleteMiddle(head)
assert actual == expect