from typing import Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
      return head
    
    newHead = ListNode(-1)
    pre, pre.next = newHead, head
    while pre.next and pre.next.next:
      odd = pre.next
      even = odd.next
      
      # pre.next, even.next, odd.next = even, odd, even.next
      """
      pre -> 1 -> 2 -> 3
      odd = 1
      even = 2
      bkNextEven = 3
      pre.next = 2  # pre -> 2
      even.next = 1 # pre -> 2 -> 1
      odd.next = 3  # pre -> 2 -> 1 -> 3
      """
      bkNextEven = even.next
      pre.next = even
      even.next = odd
      odd.next = bkNextEven

      pre = odd
            
    return newHead.next
  
sol = Solution()
head = fromArrayToListNode([1,2,3,4])
actual = sol.swapPairs(head)
assert actual.val == 2
assert actual.next.val == 1, "But " + str(actual.next.val)
assert actual.next.next.val == 4, "But " + str(actual.next.next.val)
assert actual.next.next.next.val == 3, "But " + str(actual.next.next.next.val)

head = fromArrayToListNode([])
actual = sol.swapPairs(head)
assert actual == None

head = fromArrayToListNode([1])
actual = sol.swapPairs(head)
assert actual.val == 1

head = fromArrayToListNode([1,2,3,4,5])
actual = sol.swapPairs(head)
assert actual.val == 2
assert actual.next.val == 1, "But " + str(actual.next.val)
assert actual.next.next.val == 4, "But " + str(actual.next.next.val)
assert actual.next.next.next.val == 3, "But " + str(actual.next.next.next.val)
assert actual.next.next.next.next.val == 5, "But " + str(actual.next.next.next.next.val)
