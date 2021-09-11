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
  def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
    global sumOfLeftLeaves
    sumOfLeftLeaves = 0
    def dfs(root, isLeft):
      global sumOfLeftLeaves
      if not root:
        return
      if isLeft and not root.left and not root.right:
        sumOfLeftLeaves += root.val
      dfs(root.left, True)
      dfs(root.right, False)
    dfs(root, False)
    # print(f'{sumOfLeftLeaves}')
    return sumOfLeftLeaves

sol = Solution()
assert sol.sumOfLeftLeaves(deserialize('[3,9,20,null,null,15,7]')) == 24
assert sol.sumOfLeftLeaves(deserialize('[1]')) == 0
