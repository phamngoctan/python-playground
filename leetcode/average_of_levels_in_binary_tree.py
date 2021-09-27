from typing import Optional
from typing import List
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
    def bfs(root):
      queue = [root]
      res = []
      while queue:
        size = len(queue)
        total = 0
        for _ in range(size):
          curItem = queue.pop(0)
          total += curItem.val
          if curItem:
            if curItem.left:
              queue.append(curItem.left)
            if curItem.right:
              queue.append(curItem.right)
        res.append(round(total / size, 5))
      return res
    return bfs(root)

sol = Solution()
assert sol.averageOfLevels(deserialize('[3,9,20,null,null,15,7]')) == [3, 14.5, 11]
assert sol.averageOfLevels(deserialize('[3,9,20,15,7]')) == [3.00000,14.50000,11.00000]