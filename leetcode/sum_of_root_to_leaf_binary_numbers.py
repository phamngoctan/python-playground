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
  def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    # def dfs(root, level, varOnPath, res):
    #   if not root:
    #     return
    #   varOnPath.append(root.val)
    #   dfs(root.left, level + 1, varOnPath, res)
    #   dfs(root.right, level + 1, varOnPath, res)
    #   if not root.left and not root.right:
    #     # print(f'{varOnPath}')
    #     # print(f'{"".join(str(x) for x in varOnPath)}')
    #     res[0] += int("".join(str(x) for x in varOnPath), 2)
    #   varOnPath.pop()
    def dfs(root, level, varOnPath, res):
      if not root:
        return
      varOnPath += str(root.val)
      dfs(root.left, level + 1, varOnPath, res)
      dfs(root.right, level + 1, varOnPath, res)
      if not root.left and not root.right:
        res[0] += int(varOnPath, 2)
    res = [0]
    dfs(root, 0, '', res)
    return res[0]
sol = Solution()
assert sol.sumRootToLeaf(deserialize('[1,0,1,0,1,0,1]')) == 22
assert sol.sumRootToLeaf(deserialize('[0,0,1,0,1,0,1]')) == 6
assert sol.sumRootToLeaf(deserialize('[0]')) == 0
assert sol.sumRootToLeaf(deserialize('[1]')) == 1
assert sol.sumRootToLeaf(deserialize('[1,1,1]')) == 6