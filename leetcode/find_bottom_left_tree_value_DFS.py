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
    global res
    res = (0, root.val)
    print(f'{res[1]}')
    def dfs(root, level):
      global res
      if not root:
        return
      if root.left:
        dfs(root.left, level + 1)
      if root.right:
        dfs(root.right, level + 1)
      # print(f'({level}, {root.val})')
      if level > res[0]:
        res = (level, root.val)
        # print(f'{res}')
    dfs(root, 0)
    # print(f'{res}')
    return res[1]
sol = Solution()
assert sol.findBottomLeftValue(deserialize('[2,1,3]')) == 1
assert sol.findBottomLeftValue(deserialize('[1,2,3,4,null,5,6,null,null,7]')) == 7
assert sol.findBottomLeftValue(deserialize('[1]')) == 1
assert sol.findBottomLeftValue(deserialize('[1,null,3]')) == 3
