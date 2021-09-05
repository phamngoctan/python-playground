from typing import List, Optional
from util.TreeNode import TreeNode
from util.Array import array_to_bst

class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []
    res = []
    res.extend(self.inorderTraversal(root.left))
    res.append(root.val)
    res.extend(self.inorderTraversal(root.right))
    return res

if __name__ == '__main__':
  sol = Solution()
  root = array_to_bst([1,4,2,3,5,6,8])
  # print(sol.inorderTraversal(root))
  assert sol.inorderTraversal(root) == [3,4,5,1,6,2,8]