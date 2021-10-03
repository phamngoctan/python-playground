from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def sumEvenGrandparent(self, root: TreeNode) -> int:
    def dfs(root, level, levelVal):
      if not root:
        return 0
      levelVal.append(root.val)
      left = dfs(root.left, level + 1, levelVal)
      right = dfs(root.right, level + 1, levelVal)
      total = left + right
      if level >= 2 and levelVal[level - 2]%2 == 0:
        total += root.val
      levelVal.pop()
      return total
    res = dfs(root, 0, [])
    # print(f'{res}')
    return res
sol = Solution()
assert sol.sumEvenGrandparent(deserialize('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]')) == 18
assert sol.sumEvenGrandparent(deserialize('[1]')) == 0
assert sol.sumEvenGrandparent(deserialize('[1,2,null]')) == 0
assert sol.sumEvenGrandparent(deserialize('[1,2,3,null,2,null,2]')) == 0
assert sol.sumEvenGrandparent(deserialize('[1,2,3,null,2,null,2,2,null]')) == 2
