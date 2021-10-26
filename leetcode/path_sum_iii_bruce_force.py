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
  def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
    res = [0]
    def dfs(root, targetSum):
      if root is None:
        return 
      test(root, targetSum)
      dfs(root.left, targetSum)
      dfs(root.right, targetSum)
    def test(root, targetSum):
      if root is None:
        return
      if root.val == targetSum:
        res[0] += 1
      test(root.left, targetSum - root.val)
      test(root.right, targetSum - root.val)
    dfs(root, targetSum)
    # print(f'{res}')
    return res[0]

  def pathSumMemoryLimitExceeded(self, root: Optional[TreeNode], targetSum: int) -> int:
    res = []
    def dfs(root, targetSum):
      if root is None:
        return 
      # dfs break down 
      test(root, targetSum, []) # you can move the line to any order, here is pre-order
      dfs(root.left, targetSum)
      dfs(root.right, targetSum)
    def test(root, targetSum, path):
      if root is None:
        return
      path.append(root.val)
      if sum(path) == targetSum:
        res.append(path[::])
      test(root.left, targetSum, path)
      test(root.right, targetSum, path)
      path.pop()
    dfs(root, targetSum)
    # print(f'{res}')
    return len(res)
    
sol = Solution()
assert sol.pathSum(deserialize('[10,5,-3,3,2,null,11,3,-2,null,1]'), targetSum = 8) == 3
assert sol.pathSum(deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), targetSum = 22) == 3
assert sol.pathSum(deserialize('[1,null,2,null,3,null,4,null,5]'), 3) == 2
