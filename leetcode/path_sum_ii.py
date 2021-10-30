from typing import Optional
from typing import List
from util.Array import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    def dfs(root, targetSum, stack, res):
      if root is None:
        return
      stack.append(root.val)
      if root.left is None and root.right is None:
        if sum(stack) == targetSum:
          res.append(stack[::])
      dfs(root.left, targetSum, stack, res)
      dfs(root.right, targetSum, stack, res)
      stack.pop()
    res = []
    dfs(root, targetSum, [], res)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.pathSum(deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), 22) == [[5,4,11,2],[5,8,4,5]]
assert sol.pathSum(deserialize('[1,2,3]'), targetSum = 5) == []
assert sol.pathSum(deserialize('[1,2]'), targetSum = 0) == []
