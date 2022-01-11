from typing import Optional
from util.ListNode import ListNode
from util.TreeNode import TreeNode
from util.Array import fromArrayToListNode
  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head: return None
    if not head.next: return TreeNode(head.val)
    slow, fast = head, head.next.next
    while fast and fast.next:
      slow, fast = slow.next, fast.next.next
    mid, slow.next = slow.next, None
    root = TreeNode(mid.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(mid.next)
    return root
  
  def sortedListToBST_oneIdea(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    if not head: return None
    if not head.next: return TreeNode(head.val)
    slow, fast = head, head
    prev = None
    while fast and fast.next:
      prev = slow
      slow = slow.next
      fast = fast.next.next
    # print(f'{slow.val}')
    
    prev.next = None
    root = TreeNode(slow.val)
    root.left = self.sortedListToBST(head)
    root.right = self.sortedListToBST(slow.next)
    return root
  
  def sortedListToBST_fromLC(self, head: Optional[ListNode]) -> Optional[TreeNode]:
    def buildTree(head, tail):
      if head == tail: return None
      slow, fast = head, head
      while fast != tail and fast.next != tail:
        slow = slow.next
        fast = fast.next.next
      # print(f'{slow.val}')
      # cut the linked list into two parts
      # cur = slow.next
      # secondHalf = None
      # if cur:
      #   secondHalf = slow.next if cur else None
      #   cur.next = None
      # slow.next = None
      
      root = TreeNode(slow.val)
      root.left = buildTree(head, slow)
      root.right = buildTree(slow.next, tail)
      return root
    return buildTree(head, None)

sol = Solution()
# head = sol.sortedListToBST(fromArrayToListNode([1]))
head = sol.sortedListToBST(fromArrayToListNode([-10,-3,0,1,5,9]))
head.val == 0
head.left.val == -3
head.left.left == -10
head.left.right == None
head.right.val == 9
head.right.left.val == 5
head.right.right == None
