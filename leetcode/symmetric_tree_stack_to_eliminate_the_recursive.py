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
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def dfs(root):
      stack = [(root.left, root.right)]
      while len(stack) > 0:
        left, right = stack.pop()
        # print(f'{left} {right}')
        if left is None and right is None:
          continue
        if left is None or right is None:
          return False
        if left.val == right.val:
          stack.append((left.left, right.right))
          stack.append((left.right, right.left))
        else:
          return False
      return True
    return dfs(root)
sol = Solution()
assert sol.isSymmetric(deserialize('[1,2,2,3,4,4,3]')) == True
assert sol.isSymmetric(deserialize('[1,2,2,null,3,null,3]')) == False
assert sol.isSymmetric(deserialize('[1,2,3]')) == False
assert sol.isSymmetric(deserialize('[1]')) == True
assert sol.isSymmetric(deserialize('[1,2,2,null,3,null,null]')) == False
assert sol.isSymmetric(deserialize('[1,2,2,null,3,null,null]')) == False
