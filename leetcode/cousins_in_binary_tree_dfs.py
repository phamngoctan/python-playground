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
  def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    def dfs(root, level, valToSearch):
      if not root:
        return
      if root.val == valToSearch:
        return [None, root]
      
      leftNode = root.left
      rightNode = root.right
      if leftNode and leftNode.val == valToSearch:
        return [root, level]
      if rightNode and rightNode.val == valToSearch:
        return [root, level]
      
      return dfs(root.left, level + 1, valToSearch) or dfs(root.right, level + 1, valToSearch)
    xParent = dfs(root, 0, x)
    yParent = dfs(root, 0, y)
    # print(f'{xParent} vs {yParent}')
    return xParent[0] != None and yParent[0] != None and xParent[0].val != yParent[0].val and xParent[1] == yParent[1]

sol = Solution()
assert sol.isCousins(deserialize('[1,2,3,4]'), 4, 3) == False
assert sol.isCousins(deserialize('[1,2,3,null,4,null,5]'), 5, 4) == True
assert sol.isCousins(deserialize('[1,2,3,null,4]'), 2, 3) == False
assert sol.isCousins(deserialize('[1,2,null]'), 1, 2) == False
