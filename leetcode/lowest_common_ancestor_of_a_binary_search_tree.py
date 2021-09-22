from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    while True:
      if root.val < p.val and root.val < q.val:
        root = root.right
      elif root.val > p.val and root.val > q.val:
        root = root.left
      else:
        break
    return root
sol = Solution()
assert sol.lowestCommonAncestor(deserialize('[6,2,8,0,4,7,9,null,null,3,5]'), deserialize('2'), deserialize('8')) == deserialize('6')
assert sol.lowestCommonAncestor(deserialize('[6,2,8,0,4,7,9,null,null,3,5]'), deserialize('2'), deserialize('4')) == deserialize('2')
assert sol.lowestCommonAncestor(deserialize('[2,1]'), deserialize('2'), deserialize('1')) == deserialize('2')

