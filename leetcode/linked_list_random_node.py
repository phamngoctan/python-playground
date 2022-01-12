from typing import Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode
import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

  def __init__(self, head: Optional[ListNode]):
    self.head = head
    # count, tmp = 0, head
    # while tmp:
    #   tmp = tmp.next
    #   count += 1
    # self.n = count

  def getRandom(self) -> int:
    # print(f'{random.randint(1,2)}')
    cur = self.head
    ans = cur
    count = 0
    while cur:
      ran = random.randint(1, count + 1)
      if ran == count:
        ans = cur.val
      count += 1
      cur = cur.next
    return ans
  
  def getRandom_libraryVersion(self) -> int:
    no = random.randint(1, self.n)
    # print(f'{no}')
    count = 0
    tmp = self.head
    while count != no and tmp:
      count += 1
      if count == no:
        return tmp.val
      tmp = tmp.next
      
  

# Your Solution object will be instantiated and called as such:
sol = Solution(fromArrayToListNode([1, 2, 3]))
param_1 = sol.getRandom()