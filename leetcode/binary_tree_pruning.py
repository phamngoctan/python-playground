from typing import Optional
from util.TreeNode import TreeNode
from util.Array import deserialize
from util.Array import inOrderTraversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(root, father, direction):
      if not root:
        return None
      dfs(root.left, root, 'left')
      dfs(root.right, root, 'right')
      if root.val == 0 and not root.left and not root.right:
        if father:
          if direction == 'left':
            father.left = None
          elif direction == 'right':
            father.right = None
        else:
          return None
      return root
    return dfs(root, None, None)

sol = Solution()
assert inOrderTraversal(sol.pruneTree(deserialize('[1,null,0,0,1]'))) == inOrderTraversal(deserialize('[1,null,0,null,1]'))
assert inOrderTraversal(sol.pruneTree(deserialize('[1,0,1,0,0,0,1]'))) == inOrderTraversal(deserialize('[1,null,1,null,1]'))
assert inOrderTraversal(sol.pruneTree(deserialize('[1,1,0,1,1,0,1,0]'))) == inOrderTraversal(deserialize('[1,1,0,1,1,null,1]'))
assert inOrderTraversal(sol.pruneTree(deserialize('[1]'))) == inOrderTraversal(deserialize('[1]'))
assert inOrderTraversal(sol.pruneTree(deserialize('[0]'))) == inOrderTraversal(deserialize('[null]'))
assert inOrderTraversal(sol.pruneTree(deserialize('[0,0]'))) == inOrderTraversal(deserialize('[null,null]'))
assert inOrderTraversal(sol.pruneTree(deserialize('[1,2]'))) == inOrderTraversal(deserialize('[1,2]'))
