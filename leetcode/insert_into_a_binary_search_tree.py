from typing import Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
      return TreeNode(val)
    if root.val < val:
      root.right = self.insertIntoBST(root.right, val)
    else:
      root.left = self.insertIntoBST(root.left, val)
    return root

  def insertIntoBST_myIdea(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
      return TreeNode(val)
    def dfs(root, target):
      if not root:
        return
      if root.val < target:
        if root.right:
          dfs(root.right, target)
        else:
          root.right = TreeNode(target)
      else:
        if root.left:
          dfs(root.left, target)
        else: 
          root.left = TreeNode(target)
      return root
    return dfs(root, val)

sol = Solution()
head = sol.insertIntoBST(deserialize('[4,2,7,1,3]'), 5)
assert head.val == 4 
assert head.right.val == 7
assert head.right.left.val == 5