from typing import Counter, Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
    fre = {}
    for i in range(1, 10):
      fre[i] = 0
    def dfs(root, counting, countCurPath):
      if not root:
        return
      fre[root.val] += 1
      countCurPath += 1 if fre[root.val] % 2 == 1 else -1
      if not root.right and not root.left:
        if countCurPath <= 1:
          counting[0] += 1
      else:
        dfs(root.left, counting, countCurPath)
        dfs(root.right, counting, countCurPath)
      fre[root.val] -= 1
      countCurPath += 1 if fre[root.val] % 2 == 1 else -1
    counting = [0]
    dfs(root, counting, 0)
    # print(f'{counting[0]}')
    return counting[0]
sol = Solution()
assert sol.pseudoPalindromicPaths(deserialize('[2,3,1,3,1,null,1]')) == 2
assert sol.pseudoPalindromicPaths(deserialize('[2,1,1,1,3,null,null,null,null,null,1]')) == 1
assert sol.pseudoPalindromicPaths(deserialize('[9]')) == 1
assert sol.pseudoPalindromicPaths(deserialize('[2,1,3]')) == 0
assert sol.pseudoPalindromicPaths(deserialize('[2,3,2]')) == 1
assert sol.pseudoPalindromicPaths(deserialize('[2,3,2,2]')) == 2
assert sol.pseudoPalindromicPaths(deserialize('[2,2,null,null,2]')) == 1
assert sol.pseudoPalindromicPaths(deserialize('[2,2,null,null,2,3]')) == 0
assert sol.pseudoPalindromicPaths(deserialize('[6,6,6,null,6,6,null,null,null,2,8,8,8,3,2,5,6,null,8,null,null,1,1,7,9,null,null,null,null,null,null,null,null,5,null,null,4]')) == 1

