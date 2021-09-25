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
  def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    MIN = -2**31 - 1
    if not root:
      return []
    res = []
    def dfs(root, level):
      if not root:
        return
      if level >= len(res):
        res.append(root.val)
      else:
        res[level] = max(root.val, res[level])
      dfs(root.left, level + 1)
      dfs(root.right, level + 1)
    dfs(root, 0)
    # print(f'{res}')
    return res
    
sol = Solution()
assert sol.largestValues(deserialize('[1,3,2,5,3,null,9]')) == [1,3,9]
assert sol.largestValues(deserialize('[1,2,3]')) == [1,3]
assert sol.largestValues(deserialize('[1]')) == [1]
assert sol.largestValues(deserialize('[]')) == []
assert sol.largestValues(deserialize('[1,null,2]')) == [1,2]