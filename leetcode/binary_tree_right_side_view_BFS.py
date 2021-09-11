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
    queue = [root]
    res = []
    level = 0
    while queue:
      length = len(queue)
      level += 1
      for _ in range(length):
        curVal = queue.pop(0)
        if curVal != None:
          if curVal.right != None:
            queue.append(curVal.right)
          if curVal.left != None:
            queue.append(curVal.left)
          if level > len(res):
            res.append(curVal.val)
    # print(f'{res.values()}')
    return res

sol = Solution()
assert sol.rightSideView(deserialize('[1,2,3,null,5,null,4]')) == [1,3,4]
assert sol.rightSideView(deserialize('[1,null,3]')) == [1,3]
assert sol.rightSideView(deserialize('[]')) == []
assert sol.rightSideView(deserialize('[3]')) == [3]
assert sol.rightSideView(deserialize('[1,3]')) == [1,3]