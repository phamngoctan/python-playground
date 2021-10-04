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
  def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
    # print(f'{0}')
    MAX = 2**31
    global res
    res = [MAX,MAX]
    def dfs(root):
      if not root:
        return
      # global res
      dfs(root.left)
      dfs(root.right)
      first, second = res[0], res[1]
      if root.val < first:
        res[0] = root.val
        res[1] = first
      elif root.val < second and root.val != first:
        res[1] = root.val

    dfs(root)
    # print(f'{res}')
    if res[1] == MAX:
      return -1
    return res[1]
sol = Solution()
assert sol.findSecondMinimumValue(deserialize('[2,2,5,null,null,5,7]')) == 5
assert sol.findSecondMinimumValue(deserialize('[2,2,2]')) == -1
assert sol.findSecondMinimumValue(deserialize('[2]')) == -1
