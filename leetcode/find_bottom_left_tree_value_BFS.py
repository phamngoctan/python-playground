from typing import Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# number of nodes in the range [1, 104].
# -2*31 <= Node.val <= 2*31 - 1
class Solution:
  def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    def bfs(root):
      queue = [(0, root)]
      res = [0, root.val]
      while len(queue) > 0:
        size = len(queue)
        for _ in range(size):
          curLevel, node = queue.pop(0)
          if curLevel > res[0]:
            res = [curLevel, node.val]
          if node.left:
            queue.append((curLevel + 1, node.left))
          if node.right:
            queue.append((curLevel + 1, node.right))
      return res[1]
    res = bfs(root)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.findBottomLeftValue(deserialize('[2,1,3]')) == 1
assert sol.findBottomLeftValue(deserialize('[1,2,3,4,null,5,6,null,null,7]')) == 7
assert sol.findBottomLeftValue(deserialize('[1]')) == 1
assert sol.findBottomLeftValue(deserialize('[1,null,3]')) == 3
