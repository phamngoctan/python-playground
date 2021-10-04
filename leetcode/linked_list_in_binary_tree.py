from typing import List, Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
    def dfs(root, curHead):
      if curHead == None:
        return True
      if not root:
        return
      return root.val == curHead.val and (
                dfs(root.left, curHead.next) 
                or dfs(root.right, curHead.next))
      # if root.val == curHead.val:
      #   return dfs(root.left, head, curHead.next) or dfs(root.right, head, curHead.next)
      # elif root.val == head.val:
      #   return dfs(root.left, head, head.next) or dfs(root.right, head, head.next)
      # else:
      #   return dfs(root.left, head, head) or dfs(root.right, head, head)
    if not root:
      return False
    # res = dfs(root, head, head)
    # print(f'{res}')
    return dfs(root, head) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
sol = Solution()
head = ListNode(4, ListNode(2, ListNode(8)))
assert sol.isSubPath(head, deserialize('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]')) == True
head = ListNode(1, ListNode(4, ListNode(2, ListNode(6))))
assert sol.isSubPath(head, deserialize('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]')) == True
head = ListNode(1, ListNode(4, ListNode(2, ListNode(9))))
assert sol.isSubPath(head, deserialize('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]')) == False
head = ListNode(1, ListNode(4, ListNode(2, ListNode(8))))
assert sol.isSubPath(head, deserialize('[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]')) == True
assert sol.isSubPath(ListNode(1), deserialize('[1]')) == True
assert sol.isSubPath(ListNode(1, ListNode(2)), deserialize('[1]')) == False
assert sol.isSubPath(ListNode(1, ListNode(2)), deserialize('[1,2]')) == True
assert sol.isSubPath(ListNode(2), deserialize('[1,2]')) == True
assert sol.isSubPath(ListNode(1, ListNode(10)), deserialize('[1,null,1,10,1,9]')) == True
assert sol.isSubPath(ListNode(2, ListNode(2, ListNode(1))), deserialize('[2,null,2,null,2,null,1]')) == True

