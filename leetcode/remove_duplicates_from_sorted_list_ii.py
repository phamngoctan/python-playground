from typing import Optional
from util.ListNode import ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.val == fast.next.val:
                # loop until cur point to the last duplicates
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                slow.next = fast.next # propose the next for pre
                                      # this will be verified by next line
            else:
                slow = slow.next
            fast = fast.next
        return dummy.next
