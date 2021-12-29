from typing import List, Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    ans = []
    cur = head
    count = 0
    stack = []
    while cur:
      while stack and stack[-1][1] < cur.val:
        prePos, _ = stack.pop()
        ans[prePos] = cur.val
      stack.append([count, cur.val])
      ans.append(0)
      count += 1
      cur = cur.next
    # print(f'{ans}')
    return ans
sol = Solution()
head = fromArrayToListNode([2,1,5])
assert sol.nextLargerNodes(head) == [5,5,0]
head = fromArrayToListNode([2,7,4,3,5])
assert sol.nextLargerNodes(head) == [7,0,5,5,0]
head = fromArrayToListNode([2,7,6,4,3,5])
assert sol.nextLargerNodes(head) == [7,0,0,5,5,0]
