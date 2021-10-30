from typing import Optional
from util.Array import TreeNode
from util.Array import deserialize
from util.Array import inOrderTraversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node):
      if not node:
        return
      tmp = node.left
      node.left = node.right
      node.right = tmp
      dfs(node.left)
      dfs(node.right)
    dfs(root)
    return root
sol = Solution()
assert inOrderTraversal(sol.invertTree(deserialize('[4,2,7,1,3,6,9]'))) == inOrderTraversal(deserialize('[4,7,2,9,6,3,1]'))
assert inOrderTraversal(sol.invertTree(deserialize('[2,1,3]'))) == inOrderTraversal(deserialize('[2,3,1]'))
assert inOrderTraversal(sol.invertTree(deserialize('[]'))) == inOrderTraversal(deserialize('[]'))
assert inOrderTraversal(sol.invertTree(deserialize('[1,2,null]'))) == inOrderTraversal(deserialize('[1,null,2]'))
