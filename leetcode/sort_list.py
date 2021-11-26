from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
      return head
    slow = head
    fast = head.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    firstHalf = head
    secondHalf = slow.next
    slow.next = None
    sortedFirstHalf = self.sortList(firstHalf)
    sortedSecondHalf = self.sortList(secondHalf)
    ans = self.mergeTwoSortedList(sortedFirstHalf, sortedSecondHalf)
    return ans

  def mergeTwoSortedList(self, sortedFirstHalf, sortedSecondHalf):
    MIN_VALUE = - 10**5 - 1
    dummy = ListNode(MIN_VALUE)
    cur = dummy
    while sortedFirstHalf and sortedSecondHalf:
      if sortedFirstHalf.val < sortedSecondHalf.val:
        cur.next = sortedFirstHalf
        sortedFirstHalf = sortedFirstHalf.next
      else:
        cur.next = sortedSecondHalf
        sortedSecondHalf = sortedSecondHalf.next
      cur = cur.next
    cur.next = sortedFirstHalf if sortedFirstHalf else sortedSecondHalf
    return dummy.next
  
  def sortList_TLE(self, head: Optional[ListNode]) -> Optional[ListNode]:
    '''
    This is kind of insertion sort. Time complexity is O(n^2)
    '''
    def helper(head, newHead):
      if not head:
        return newHead
      helper(head.next, newHead)
      cur = newHead
      while cur.next and cur.next.val < head.val:
        cur = cur.next
      # next = cur.next if cur else None
      head.next = cur.next
      cur.next = head
      return newHead

    MIN_VALUE = - 10**5 - 1
    newHead = ListNode(MIN_VALUE)
    ans = helper(head, newHead)
    return ans.next
sol = Solution()
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
actual = sol.sortList(head)
assert actual.val == 1 
assert actual.next.next.val == 3 
assert actual.next.next.next.val == 4

head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
actual = sol.sortList(head)
assert actual.val == -1 
assert actual.next.next.val == 3 
assert actual.next.next.next.val == 4
assert actual.next.next.next.next.val == 5

