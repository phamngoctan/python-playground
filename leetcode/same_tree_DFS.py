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
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def dfs(root1, root2):
      if root1 and not root2:
        return False
      if not root1 and root2:
        return False
      if not root1 and not root2:
        return True
      if root1.val == root2.val:
        return dfs(root1.left, root2.left) and dfs(root1.right, root2.right) 
      else:
        return False
    res = dfs(p, q)
    return res
sol = Solution()
assert sol.isSameTree(deserialize('[1,2,3]'), deserialize('[1,2,3]')) == True
assert sol.isSameTree(deserialize('[1,2]'), deserialize('[1,null,2]')) == False
assert sol.isSameTree(deserialize('[1,2]'), deserialize('[1]')) == False
assert sol.isSameTree(deserialize('[1]'), deserialize('[]')) == False
assert sol.isSameTree(deserialize('[]'), deserialize('[1]')) == False
assert sol.isSameTree(deserialize('[]'), deserialize('[]')) == True
assert sol.isSameTree(deserialize('[1]'), deserialize('[1,null,2]')) == False

