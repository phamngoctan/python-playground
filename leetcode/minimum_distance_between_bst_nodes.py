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
  def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    def helper(node, minVal, maxVal):
      global ans
      if not node:
        return
      helper(node.left, minVal, node.val)
      helper(node.right, node.val, maxVal)
      ans = min(ans, node.val - minVal)
      ans = min(ans, maxVal - node.val)
    global ans
    MAX_VALUE = 10**5 + 5
    ans = MAX_VALUE
    helper(root, -MAX_VALUE, MAX_VALUE)
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.minDiffInBST(deserialize('[4,2,6,1,3]')) == 1
assert sol.minDiffInBST(deserialize('[4,2,6]')) == 2
assert sol.minDiffInBST(deserialize('[48,30,60,null,null,49,null]')) == 1
assert sol.minDiffInBST(deserialize('[1,0,48,null,null,12,49]')) == 1
assert sol.minDiffInBST(deserialize('[0,null,2236,1277,2776,519]')) == 519
