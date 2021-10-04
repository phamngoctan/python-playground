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
  def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    def dfs(root, preVal):
      if not root:
        return 0
      preVal = preVal * 2 + root.val
      if not root.left and not root.right:
        return preVal
      leftVal = dfs(root.left, preVal)
      rightVal = dfs(root.right, preVal)
      return leftVal + rightVal
    res = dfs(root, 0)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.sumRootToLeaf(deserialize('[1,0,1,0,1,0,1]')) == 22
assert sol.sumRootToLeaf(deserialize('[0,0,1,0,1,0,1]')) == 6
assert sol.sumRootToLeaf(deserialize('[0]')) == 0
assert sol.sumRootToLeaf(deserialize('[1]')) == 1
assert sol.sumRootToLeaf(deserialize('[1,1,1]')) == 6
assert sol.sumRootToLeaf(deserialize('[1,1,null,1]')) == 7