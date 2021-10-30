from typing import Optional
from typing import List
from util.Array import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
    def dfs(root, stringSoFar, res):
      if not root:
        return
      stringSoFar += "->" if stringSoFar != '' else ''
      stringSoFar += str(root.val)
      if root.left is None and root.right is None:
        res.append(stringSoFar)
      dfs(root.left, stringSoFar, res)
      dfs(root.right, stringSoFar, res)
    res = []
    dfs(root, "", res)
    # print(f'{res}')
    return res
sol = Solution()
assert sol.binaryTreePaths(deserialize('[1,2,3,null,5]')) == ["1->2->5","1->3"]
assert sol.binaryTreePaths(deserialize('[1]')) == ["1"]
