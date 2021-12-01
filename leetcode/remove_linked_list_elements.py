from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    # prevent the complex if/else statement
    dummy = ListNode(-1)
    dummy.next = head
    
    fast = head
    pre = dummy
    while fast:
      if fast.val == val:
        # Better in GC but slow compare to the current impl
        # tmp = fast.next
        # fast.next = None
        # fast = tmp
        # pre.next = tmp
        fast = fast.next
        pre.next = fast
      else:
        pre = fast
        fast = fast.next
    return dummy.next

sol = Solution()
arr = [1,2,6,3,4,5,6]
head = ListNode(arr[0])
cur = head
for i in range(1, len(arr)):
  cur.next = ListNode(arr[i])
  cur = cur.next
actual = sol.removeElements(head, 6)
assert actual.val == 1
assert actual.next.val == 2
assert actual.next.next.val == 3
assert actual.next.next.next.val == 4
assert actual.next.next.next.next.val == 5

arr = [7,7,7,7]
head = ListNode(arr[0])
cur = head
for i in range(1, len(arr)):
  cur.next = ListNode(arr[i])
  cur = cur.next
actual = sol.removeElements(head, 7)
assert actual == None

actual = sol.removeElements(ListNode(7, ListNode(1)), 7)
assert actual.val == 1
