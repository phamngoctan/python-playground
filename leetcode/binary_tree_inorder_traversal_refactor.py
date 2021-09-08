from typing import List, Optional
from util.TreeNode import TreeNode
from util.Array import array_to_bst

class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(node):
      if not node:
        return
      dfs(node.left)
      res.append(node.val)
      dfs(node.right)
    dfs(root)
    return res

if __name__ == '__main__':
  sol = Solution()
  root = array_to_bst([1,4,2,3,5,6,8])
  # print(sol.inorderTraversal(root))
  assert sol.inorderTraversal(root) == [3,4,5,1,6,2,8]