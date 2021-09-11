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
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(root):
      if not root:
        return
      dfs(root.left)
      dfs(root.right)
      res.append(root.val)
    dfs(root)
    # print(f'{res}')
    return res

sol = Solution()
assert sol.postorderTraversal(deserialize('[1,null,2,3]')) == [3,2,1]
assert sol.postorderTraversal(deserialize('[1]')) == [1]
assert sol.postorderTraversal(deserialize('[]')) == []