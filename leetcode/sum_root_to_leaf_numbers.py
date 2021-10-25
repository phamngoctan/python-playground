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
  def sumNumbers(self, root: Optional[TreeNode]) -> int:
    def dfs(node, prevStr, res):
      if node is None:
        return
      prevStr += str(node.val)
      if node.left is None and node.right is None:
        res[0] += int(prevStr)
      dfs(node.left, prevStr, res)
      dfs(node.right, prevStr, res)
    res = [0]
    dfs(root, "", res)
    # print(f'{res}')
    return res[0]
sol = Solution()
assert sol.sumNumbers(deserialize('[1,2,3]')) == 25
assert sol.sumNumbers(deserialize('[4,9,0,5,1]')) == 1026
assert sol.sumNumbers(deserialize('[1]')) == 1
