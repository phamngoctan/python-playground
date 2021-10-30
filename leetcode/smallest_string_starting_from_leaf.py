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
  def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    global minStr
    minStr = 'zzzzzzzzzzzzzzzzzzzzzzzzzzz'
    valToStr = {}
    for i in range(26):
      valToStr[i] = chr(ord('a') + i)
    # print(f'{valToStr}')
    def dfs(root, strVal):
      if not root:
        return
      global minStr
      strVal = valToStr[root.val] + strVal
      if not root.left and not root.right:
        if strVal < minStr:
          minStr = strVal
      dfs(root.left, strVal)
      dfs(root.right, strVal)
    dfs(root, '')
    return minStr
sol = Solution()
assert sol.smallestFromLeaf(deserialize('[0,1,2,3,4,3,4]')) == 'dba'
assert sol.smallestFromLeaf(deserialize('[25,1,3,1,3,0,2]')) == 'adz'
assert sol.smallestFromLeaf(deserialize('[2,2,1,null,1,0,null,0]')) == 'abc'
assert sol.smallestFromLeaf(deserialize('[25]')) == 'z'
assert sol.smallestFromLeaf(deserialize('[0]')) == 'a'
assert sol.smallestFromLeaf(deserialize('[0,2,0]')) == 'aa'
assert sol.smallestFromLeaf(deserialize('[0,2]')) == 'ca'
