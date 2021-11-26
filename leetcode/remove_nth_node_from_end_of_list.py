from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = None
    fast = head
    count = 0
    while fast:
      if count == n:
        slow = head
      elif slow:
        slow = slow.next
      count += 1
      fast = fast.next
    if slow == None:
      return head.next if head.next else None
    else:
      slow.next = slow.next.next
    return head
sol = Solution()
actual = sol.removeNthFromEnd(ListNode(1, ListNode(2)), 2)
assert actual.val == 2

actual = sol.removeNthFromEnd(ListNode(1, ListNode(2)), 1)
assert actual.val == 1, "But " + str(actual.val)

actual = sol.removeNthFromEnd(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2)
assert actual.val == 1
assert actual.next.val == 2
assert actual.next.next.val == 3
assert actual.next.next.next.val == 5

actual = sol.removeNthFromEnd(ListNode(1), 1)
assert actual == None