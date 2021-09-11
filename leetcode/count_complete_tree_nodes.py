import math
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
  def countNodes(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    height = self.getHeight(root)
    maxNodesInLeaves = 2 ** height / 2 - 1
    left = 0
    right = maxNodesInLeaves
    while left < right:
      mid = math.ceil((left + right) / 2)
      # print(mid)
      if self.nodeExists(root, mid, height):
        left = mid
      else:
        right = mid - 1
    # print(f'{2 ** (height - 1) + left}')
    return 2 ** (height - 1) - 1 + left + 1

  def nodeExists(self, root, pos, height):
    maxNodesInLeaves = 2 ** height / 2 - 1
    left = 0
    right = maxNodesInLeaves
    while left < right:
      mid = math.ceil((left + right) / 2)
      if mid <= pos:
        left = mid
        root = root.right
      else:
        right = mid - 1
        root = root.left
    return root != None
  
  def getHeight(self, root):
    height = 0
    while root:
      height += 1
      root = root.left
    return height

sol = Solution()
# print(sol.nodeExists(deserialize('[1,2,3,4,5,6,7,8,9,10,11,12]'), 3, 4))
assert sol.countNodes(deserialize('[1,2,3,4,5,6]')) == 6
assert sol.countNodes(deserialize('[]')) == 0
assert sol.countNodes(deserialize('[1]')) == 1
assert sol.countNodes(deserialize('[1,2,3,4,5,6,7,8,9,10,11,12]')) == 12