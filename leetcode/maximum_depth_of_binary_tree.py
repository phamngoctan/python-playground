from typing import Optional
from util.TreeNode import TreeNode
from util.Array import array_to_bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    leftDepth = 1 + self.maxDepth(root.left)
    rightDepth = 1 + self.maxDepth(root.right)
    return leftDepth if leftDepth > rightDepth else rightDepth

sol = Solution()
assert sol.maxDepth(array_to_bst([3,9,20,None,None,15,7])) == 3
assert sol.maxDepth(array_to_bst([1,None,2])) == 2
assert sol.maxDepth(array_to_bst([])) == 0
assert sol.maxDepth(array_to_bst([0])) == 1


