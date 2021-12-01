from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
      return head
    slow = None
    fast = head
    count = 1
    kthFromTop = None
    while fast:
      if count == k:
        kthFromTop = fast
        slow = head
      elif slow:
        slow = slow.next
      fast = fast.next
      count += 1
    
    # print(f'{kthFromTop.val}')
    # print(f'{slow.val}')
    tmp = kthFromTop.val
    kthFromTop.val = slow.val
    slow.val = tmp    
    return head
    
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
actual = sol.swapNodes(head, 2)
assert actual.val == 1
assert actual.next.val == 4
assert actual.next.next.val == 3
assert actual.next.next.next.val == 2
assert actual.next.next.next.next.val == 5

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
actual = sol.swapNodes(head, 5)
assert actual.val == 5
assert actual.next.val == 2
assert actual.next.next.val == 3
assert actual.next.next.next.val == 4
assert actual.next.next.next.next.val == 1

head = ListNode(1)
actual = sol.swapNodes(head, 1)
assert actual.val == 1

head = ListNode(1, ListNode(2, ListNode(3)))
actual = sol.swapNodes(head, 1)
assert actual.val == 3
assert actual.next.val == 2
assert actual.next.next.val == 1

head = ListNode(1, ListNode(2, ListNode(3)))
actual = sol.swapNodes(head, 2)
assert actual.val == 1
assert actual.next.val == 2
assert actual.next.next.val == 3

head = ListNode(1, ListNode(3))
actual = sol.swapNodes(head, 1)
assert actual.val == 3
assert actual.next.val == 1

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
actual = sol.swapNodes(head, 2)
assert actual.val == 1
assert actual.next.val == 3
assert actual.next.next.val == 2
assert actual.next.next.next.val == 4
