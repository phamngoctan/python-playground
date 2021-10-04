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
    def bfs(root):
      queue = [root]
      res = 0
      while len(queue) > 0:
        curLevelTotalVal = 0
        size = len(queue)
        for _ in range(size):
          cur = queue.pop(0)
          curLevelTotalVal += cur.val
          if cur.left:
            queue.append(cur.left)
          if cur.right:
            queue.append(cur.right)
        res = curLevelTotalVal
      return res
    return bfs(root)
sol = Solution()
assert sol.deepestLeavesSum(deserialize('[1,2,3,4,5,null,6,7,null,null,null,null,8]')) == 15
assert sol.deepestLeavesSum(deserialize('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]')) == 19
assert sol.deepestLeavesSum(deserialize('[19]')) == 19
assert sol.deepestLeavesSum(deserialize('[1,2,null,4]')) == 4
