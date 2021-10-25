from typing import Optional
from util.Array import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if root1 == None or root2 == None:
      return root1 == root2
    return root1.val == root2.val and (
                (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) 
                or
                (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)))
sol = Solution()
assert sol.flipEquiv(deserialize('[1,2,3,4,5,6,null,null,null,7,8]'), deserialize('[1,3,2,null,6,4,5,null,null,null,null,8,7]')) == True
assert sol.flipEquiv(deserialize('[]'), deserialize('[]')) == True
assert sol.flipEquiv(deserialize('[]'), deserialize('[1]')) == False
assert sol.flipEquiv(deserialize('[0,null,1]'), deserialize('[]')) == False
assert sol.flipEquiv(deserialize('[0,null,1]'), deserialize('[0,1]')) == True
