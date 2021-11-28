from typing import Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    curL1 = l1
    curL2 = l2
    dummy = ListNode(0)
    curNewHead = dummy
    carryAmount = 0
    while curL1 and curL2:
      tmp = curL1.val + curL2.val + carryAmount
      curNewHead.next = ListNode(tmp % 10)
      curNewHead = curNewHead.next
      carryAmount = tmp // 10
      curL1 = curL1.next
      curL2 = curL2.next
    
    curNewHead.next = curL1 if curL1 else curL2
    if not carryAmount:
      return dummy.next
    
    if curNewHead.next:
      curNewHead = curNewHead.next
      while curNewHead and carryAmount:
        tmp = curNewHead.val + carryAmount
        curNewHead.val = tmp % 10
        carryAmount = tmp // 10
        if curNewHead.next == None and carryAmount:
          curNewHead.next = ListNode(carryAmount)
          curNewHead = None
        else:
          curNewHead = curNewHead.next
    else:
      curNewHead.next = ListNode(carryAmount)
    return dummy.next
    
sol = Solution()
l1 = fromArrayToListNode([2,4,3])
l2 = fromArrayToListNode([2,4,3])
actual = sol.addTwoNumbers(l1, l2)
assert actual.val == 4
assert actual.next.val == 8
assert actual.next.next.val == 6

l1 = fromArrayToListNode([2,6,6])
l2 = fromArrayToListNode([2,4,3])
actual = sol.addTwoNumbers(l1, l2)
assert actual.val == 4
assert actual.next.val == 0
assert actual.next.next.val == 0
assert actual.next.next.next.val == 1

l1 = fromArrayToListNode([2,6,6])
l2 = fromArrayToListNode([2,4,3,5])
actual = sol.addTwoNumbers(l1, l2)
assert actual.val == 4
assert actual.next.val == 0
assert actual.next.next.val == 0
assert actual.next.next.next.val == 6

l1 = fromArrayToListNode([2,8])
l2 = fromArrayToListNode([8])
actual = sol.addTwoNumbers(l1, l2)
assert actual.val == 0
assert actual.next.val == 9

l1 = fromArrayToListNode([9,9,9,9,9,9,9])
l2 = fromArrayToListNode([9,9,9,9])
actual = sol.addTwoNumbers(l1, l2)
assert actual.val == 8
assert actual.next.val == 9
assert actual.next.next.val == 9
assert actual.next.next.next.val == 9
assert actual.next.next.next.next.val == 0
assert actual.next.next.next.next.next.val == 0
assert actual.next.next.next.next.next.next.val == 0
assert actual.next.next.next.next.next.next.next.val == 1
