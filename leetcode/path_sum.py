from typing import Optional
from util.Array import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    def dfs(root, prevSum, targetSum):
      if root is None:
        return False
      prevSum += root.val
      if root.left is None and root.right is None and prevSum == targetSum:
        return True
      return dfs(root.left, prevSum, targetSum) or dfs(root.right, prevSum, targetSum)
    return dfs(root, 0, targetSum)
sol = Solution()
assert sol.hasPathSum(deserialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]'), 22) == True
assert sol.hasPathSum(deserialize('[1,2,3]'), 5) == False
assert sol.hasPathSum(deserialize('[1]'), 1) == True
