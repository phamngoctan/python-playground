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
  def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
    res = [-1, 0]
    def dfs(root, level):
      if not root:
        return
      dfs(root.left, level + 1)
      dfs(root.right, level + 1)
      if level > res[0]:
        res[0] = level
        res[1] = root.val
      elif level == res[0]:
        res[1] += root.val
    dfs(root, 0)
    # print(f'{res}')
    return res[1]
sol = Solution()
assert sol.deepestLeavesSum(deserialize('[1,2,3,4,5,null,6,7,null,null,null,null,8]')) == 15
assert sol.deepestLeavesSum(deserialize('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]')) == 19
assert sol.deepestLeavesSum(deserialize('[19]')) == 19
