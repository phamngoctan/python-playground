from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
      return head
    n = self.count(head)
    k = k % n
    if k == n or k == 0:
      return head
    
    reversedHead = self.reverseWholeLinkedlist(head)
    count = 0
    newHead = None
    cur = reversedHead
    firstPartTail = None
    while count < k:
      if not firstPartTail:
        firstPartTail = cur
      tmp = cur.next
      cur.next = newHead
      newHead = cur
      cur = tmp
      count += 1
    # print(f'{cur.val}')
    secondPartHead = None
    while count < n:
      tmp = cur.next
      cur.next = secondPartHead
      secondPartHead = cur
      cur = tmp
      count += 1
    # print(f'{firstPartTail.val}')
    # print(f'{secondPartHead.val}')
    firstPartTail.next = secondPartHead
    return newHead
  
  def reverseWholeLinkedlist(self, head):
    newHead = None
    cur = head
    while cur:
      tmp = cur.next
      cur.next = newHead
      newHead = cur
      cur = tmp
    return newHead
  
  def count(self, head):
    cur = head
    count = 0
    while cur:
      cur = cur.next
      count += 1
    return count
    
sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
actual = sol.rotateRight(head, k = 2)
assert actual.val == 4
assert actual.next.val == 5
assert actual.next.next.val == 1
assert actual.next.next.next.val == 2
assert actual.next.next.next.next.val == 3

head = ListNode(1, ListNode(2))
actual = sol.rotateRight(head, k = 1)
assert actual.val == 2
assert actual.next.val == 1
