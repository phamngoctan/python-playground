from typing import List, Optional
from util.TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    self.i = 0
    def dfs(lowerBound, upperBound):
      if self.i >= len(preorder) or not lowerBound <= preorder[self.i] <= upperBound:
        return None
      root = TreeNode(preorder[self.i])
      self.i += 1
      root.left = dfs(lowerBound, root.val)
      root.right = dfs(root.val, upperBound)
      return root
    return dfs(-float('inf'), float('inf'))
  
  def bstFromPreorder_stack(self, preorder: List[int]) -> Optional[TreeNode]:
    root = TreeNode(preorder[0])
    monotonicStack = [root]
    for i in range(1, len(preorder)):
      val = preorder[i]
      if monotonicStack[-1].val > val:
        monotonicStack[-1].left = TreeNode(val)
        monotonicStack.append(monotonicStack[-1].left)
      else:
        while monotonicStack and monotonicStack[-1].val < val:
          last = monotonicStack.pop()
        last.right = TreeNode(val)
        monotonicStack.append(last.right)
    return root

sol = Solution()
head = sol.bstFromPreorder([8,5,1,7,10,12])
assert head.val == 8
assert head.right.val == 10
assert head.left.val == 5
assert head.left.right.val == 7
assert head.left.left.val == 1
assert head.left.left.left == None
assert head.left.left.right == None

