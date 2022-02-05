# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
from util.ListNode import ListNode
from util.Array import fromArrayToListNode
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        pq = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(pq, (lists[i].val, i, lists[i]))
        # print(f'{pq}')
        newHead = ListNode(-1)
        curNewHead = newHead
        while len(pq) > 0:
            _, i, cur = heappop(pq)
            curNewHead.next = cur
            curNewHead = curNewHead.next
            if cur.next:
                heappush(pq, (cur.next.val, i, cur.next))
        # print(f'{newHead}')
        return newHead.next

sol = Solution()
assert sol.mergeKLists([[]]) == None
assert sol.mergeKLists([]) == None
ans = sol.mergeKLists([fromArrayToListNode([1,4,5]), fromArrayToListNode([1,3,4]), fromArrayToListNode([2,6])])
assert ans.val == 1
assert ans.next.val == 1
assert ans.next.next.val == 2
assert ans.next.next.next.val == 3
assert ans.next.next.next.next.val == 4
