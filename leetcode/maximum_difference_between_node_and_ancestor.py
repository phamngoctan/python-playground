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
  def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    global ans
    ans = 0
    def DFS(root, maxInPath, minInPath):
      if not root:
        return
      global ans
      ans = max(ans, abs(root.val - maxInPath), abs(root.val - minInPath))
      maxInPath = max(maxInPath, root.val)
      minInPath = min(minInPath, root.val)
      DFS(root.left, maxInPath, minInPath)
      DFS(root.right, maxInPath, minInPath)
    DFS(root, root.val, root.val)
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.maxAncestorDiff(deserialize('[8,3,10,1,6,null,14,null,null,4,7,13]')) == 7
assert sol.maxAncestorDiff(deserialize('[1,null,2,null,0,3]')) == 3
assert sol.maxAncestorDiff(deserialize('[2,5,0,null,null,4,null,null,6,1,null,3]')) == 6
