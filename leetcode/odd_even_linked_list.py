from typing import Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode

# Definition for singly-linked list.
class Solution:
  def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
      return head
    odd = head
    evenHead = head.next
    even = evenHead
    while even and even.next:
      odd.next = even.next
      odd = odd.next
      even.next = odd.next
      even = even.next
    odd.next = evenHead
    return head

sol = Solution()
head = fromArrayToListNode([1,2,3,4,5])

actual = sol.oddEvenList(head)
assert actual.val == 1
assert actual.next.val == 3
assert actual.next.next.val == 5
assert actual.next.next.next.val == 2
assert actual.next.next.next.next.val == 4
assert actual.next.next.next.next.next == None

head = fromArrayToListNode([1,2,3,4,5,6])
actual = sol.oddEvenList(head)
assert actual.val == 1
assert actual.next.val == 3
assert actual.next.next.val == 5
assert actual.next.next.next.val == 2
assert actual.next.next.next.next.val == 4
assert actual.next.next.next.next.next.val == 6
assert actual.next.next.next.next.next.next == None
