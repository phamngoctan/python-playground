from typing import List
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
  def minDepth(self, root: Optional[TreeNode]) -> int:
    if root == None:
      return 0
    # print(f'cur{root} left: {root.left} right: {root.right}')
    if root.left == None and root.right == None:
      return 1
    if root.left == None and root.right != None:
      return 1 + self.minDepth(root.right)
    if root.left != None and root.right == None:
      return 1 + self.minDepth(root.left)
    leftLength = self.minDepth(root.left)
    rightLength = self.minDepth(root.right)
    # print(f'{root.val}: {leftLength} vs {rightLength}')
    return min(leftLength, rightLength) + 1

sol = Solution()
assert sol.minDepth(deserialize('[3,9,20,null,null,15,7]')) == 2
assert sol.minDepth(deserialize('[2,null,3,null,4,null,5,null,6]')) == 5
assert sol.minDepth(deserialize('[6]')) == 1
assert sol.minDepth(deserialize('[]')) == 0