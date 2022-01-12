from typing import List, Optional
from util.TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def buildTree(left, right):
      if left > right: return None
      # if left == right: return TreeNode(nums[left])
      mid = (left + right)//2
      root = TreeNode(nums[mid])
      root.left = buildTree(left, mid - 1)
      root.right = buildTree(mid + 1, right)
      return root
    return buildTree(0, len(nums) - 1)

sol = Solution()
head = sol.sortedArrayToBST([-10,-3,0,5,9])
assert head.val == 0
assert head.left.val == -10
assert head.left.right.val == -3
assert head.right.val == 5
assert head.right.right.val == 9
