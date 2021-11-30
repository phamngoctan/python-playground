from typing import List, Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode
import heapq
from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    '''
    Not so good in performance compare to heapq
    '''
    queue = PriorityQueue()
    for index, head in enumerate(lists):
      if head:
        queue.put([head.val, index, head])
    dummy = ListNode(0)
    ans = dummy
    while queue.qsize() > 0:
      _, listId, head = queue.get()
      ans.next = head
      ans = ans.next
      if head.next:
        queue.put([head.next.val, listId, head.next])
    return dummy.next
  
  def mergeKLists_oneIdea(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    '''
    Using heapq
    '''
    queue = []
    for index, head in enumerate(lists):
      if head:
        heapq.heappush(queue, [head.val, index, head])
    dummy = ListNode(0)
    ans = dummy
    while queue:
      val, listId, head = heapq.heappop(queue)
      ans.next = head
      ans = ans.next
      if head.next:
        heapq.heappush(queue, [head.next.val, listId, head.next])
    return dummy.next
sol = Solution()
head1 = fromArrayToListNode([1,4,5])
head2 = fromArrayToListNode([1,3,4])
head3 = fromArrayToListNode([2,6])
actual = sol.mergeKLists([head1,head2,head3])
assert actual.val == 1
assert actual.next.val == 1
assert actual.next.next.val == 2
assert actual.next.next.next.val == 3
assert actual.next.next.next.next.val == 4
assert actual.next.next.next.next.next.val == 4
assert actual.next.next.next.next.next.next.val == 5
assert actual.next.next.next.next.next.next.next.val == 6
