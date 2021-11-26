from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Borrow from leetcode
    '''
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
      if l1.val < l2.val:
        tail.next = l1
        l1 = l1.next
      else:
        tail.next = l2
        l2 = l2.next
      tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

  def mergeTwoLists_recursive(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    '''
    Borrow from leetcode
    '''
    if l1 == None or l2 == None:
      return l1 or l2
    if l1.val < l2.val:
      l1.next = self.mergeTwoLists_recursive(l1.next, l2)
      return l1
    else:
      l2.next = self.mergeTwoLists_recursive(l1, l2.next)
      return l2
  
  def mergeTwoLists_improvement1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
      if l1.val < l2.val:
        tmp = l1
        l1 = l1.next
        tail.next = tmp
        tail = tmp
      else:
        tmp = l2
        l2 = l2.next
        tail.next = tmp
        tail = tmp
    while l1:
      tmp = l1
      l1 = l1.next
      tail.next = tmp
      tail = tmp
    while l2:
      tmp = l2
      l2 = l2.next
      tail.next = tmp
      tail = tmp
    return dummy.next
  
  def mergeTwoLists_myUglyImpl(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    ans = None
    curTail = None
    while l1 and l2:
      if l1.val < l2.val:
        tmp = l1
        l1 = l1.next
        if ans:
          curTail.next = tmp
          curTail = tmp
        else:
          ans = tmp
          curTail = tmp
      else:
        tmp = l2
        l2 = l2.next
        if ans:
          curTail.next = tmp
          curTail = tmp
        else:
          ans = tmp
          curTail = tmp
    while l1:
      tmp = l1
      l1 = l1.next
      if ans:
        curTail.next = tmp
        curTail = tmp
      else:
        ans = tmp
        curTail = tmp
    while l2:
      tmp = l2
      l2 = l2.next
      if ans:
        curTail.next = tmp
        curTail = tmp
      else:
        ans = tmp
        curTail = tmp
    return ans
    

sol = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
actual = sol.mergeTwoLists(l1, l2)
assert actual.val == 1
assert actual.next.val == 2

l1 = ListNode(1)
actual = sol.mergeTwoLists(l1, None)
assert actual.val == 1

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
actual = sol.mergeTwoLists(l1, l2)
assert actual.val == 1
assert actual.next.val == 1
assert actual.next.next.val == 2
assert actual.next.next.next.val == 3
assert actual.next.next.next.next.val == 4
assert actual.next.next.next.next.next.val == 4
