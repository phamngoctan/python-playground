from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow = head
    fast = head.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    stack = []
    while slow:
      stack.append(slow)
      slow = slow.next
    while stack:
      if stack[-1].val != head.val:
        return False
      stack.pop()
      head = head.next
    return True
  
  def isPalindrome_goodEnough(self, head: Optional[ListNode]) -> bool:
    if not head or not head.next:
      return True
    mid = self.findMiddle(head)
    secondHalf = mid.next
    mid.next = None
    reversedSecondHalf = self.reverse(secondHalf)
    while head and reversedSecondHalf:
      if reversedSecondHalf and head.val != reversedSecondHalf.val:
        return False
      head = head.next
      reversedSecondHalf = reversedSecondHalf.next
    return not head or not head.next
    
  def findMiddle(self, head):
    slow = head
    fast = head.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow

  def reverse(self, head):
    newHead = None
    while head:
      tmp = head.next
      head.next = newHead
      newHead = head
      head = tmp
    return newHead

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
assert sol.isPalindrome(head) == True

head = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
assert sol.isPalindrome(head) == True

head = ListNode(1, ListNode(3, ListNode(3, ListNode(2, ListNode(1)))))
assert sol.isPalindrome(head) == False

head = ListNode(1)
assert sol.isPalindrome(head) == True

head = ListNode(1, ListNode(1))
assert sol.isPalindrome(head) == True

head = ListNode(1, ListNode(2))
assert sol.isPalindrome(head) == False
