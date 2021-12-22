from typing import Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    slow = fast = head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    # print(slow.val)
    reversedSecondPart = self.reverse(slow)
    # print(f'{reversedSecondPart.val}')
    newHead = ListNode(-1)
    curNewHead = newHead
    arr = [head, reversedSecondPart]
    i = 0
    while arr[0] and arr[1]:
      tmp = arr[i].next
      curNewHead.next = arr[i]
      curNewHead = curNewHead.next
      arr[i] = tmp
      i = (i + 1) % 2
    # return newHead.next

  def reverse(self, head):
    newHead = None
    curHead = head
    while curHead:
      tmp = curHead.next
      curHead.next = newHead
      newHead = curHead
      curHead = tmp
    return newHead
      
sol = Solution()
head = fromArrayToListNode([1,2,3,4])
expect = fromArrayToListNode([1,4,2,3])
sol.reorderList(head)
assert head.val == expect.val
assert head.next.val == expect.next.val
assert head.next.next.val == expect.next.next.val
assert head.next.next.next.val == expect.next.next.next.val

head = fromArrayToListNode([1,2,3,4,5])
expect = fromArrayToListNode([1,5,2,4,3])
sol.reorderList(head)
assert head.val == expect.val
assert head.next.val == expect.next.val
assert head.next.next.val == expect.next.next.val
assert head.next.next.next.val == expect.next.next.next.val
assert head.next.next.next.next.val == expect.next.next.next.next.val

head = fromArrayToListNode([1,2])
expect = fromArrayToListNode([1,2])
sol.reorderList(head)
assert head.val == expect.val
assert head.next.val == expect.next.val

head = fromArrayToListNode([1,2,3])
expect = fromArrayToListNode([1,3,2])
sol.reorderList(head)
assert head.val == expect.val
assert head.next.val == expect.next.val

head = fromArrayToListNode([1])
expect = fromArrayToListNode([1])
sol.reorderList(head)
assert head.val == expect.val
