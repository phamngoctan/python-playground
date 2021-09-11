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
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    res = {0:root.val}
    def dfs(root, level):
      if root == None:
        return
      rightNode = root.right
      leftNode = root.left
      if not level in res and rightNode:
        res[level] = rightNode.val
      if not level in res and leftNode:
        res[level] = leftNode.val
      dfs(rightNode, level + 1)
      dfs(leftNode, level + 1)
    dfs(root, 1)
    # print(f'{res}')
    return list(res.values())

sol = Solution()
assert sol.rightSideView(deserialize('[1,2,3,null,5,null,4]')) == [1,3,4]
assert sol.rightSideView(deserialize('[1,null,3]')) == [1,3]
assert sol.rightSideView(deserialize('[]')) == []
assert sol.rightSideView(deserialize('[3]')) == [3]
assert sol.rightSideView(deserialize('[1,3]')) == [1,3]