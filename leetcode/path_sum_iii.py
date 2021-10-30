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
    cache = {0:1}
    def dfs(node, targetSum, curPathSum, cache):
      if node is None:
        return 
      # calculate curPathSum and required oldPathSum
      curPathSum += node.val
      oldPathSum = curPathSum - targetSum
      # update result & cache
      res[0] += cache.get(oldPathSum, 0)
      cache[curPathSum] = cache.get(curPathSum, 0) + 1

      dfs(node.left, targetSum, curPathSum, cache)
      dfs(node.right, targetSum, curPathSum, cache)
      cache[curPathSum] -= 1
    dfs(root, targetSum, 0, cache)
    # print(f'{res}')
    return res[0]
sol = Solution()
assert sol.pathSum(deserialize('[10,5,-3,3,2,null,11,3,-2,null,1]'), targetSum = 8) == 3
assert sol.pathSum(deserialize('[5,4,8,11,null,13,4,7,2,null,null,5,1]'), targetSum = 22) == 3
assert sol.pathSum(deserialize('[1,null,2,null,3,null,4,null,5]'), 3) == 2
