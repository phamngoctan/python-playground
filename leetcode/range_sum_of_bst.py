from typing import Optional
from util.TreeNode import TreeNode

class Solution:
  def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    global ans
    ans = 0
    def helper(node, lowerBound, higherBound):
      global ans
      if not node:
        return 0
      if lowerBound <= node.val <= higherBound:
        ans += node.val
      helper(node.left, lowerBound, higherBound)
      helper(node.right, lowerBound, higherBound)
    helper(root, low, high)
    # print(f'{ans}')
    return ans
