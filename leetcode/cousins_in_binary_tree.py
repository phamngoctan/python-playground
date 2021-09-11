from typing import Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
    queue = [[root, None]]
    while queue:
      length = len(queue)
      cousins = {}
      for _ in range(length):
        curItem = queue.pop(0)
        curNode = curItem[0]
        if curNode:
          if curNode.left:
            queue.append([curNode.left, curNode.val])
          if curNode.right:
            queue.append([curNode.right, curNode.val])
          cousins[curNode.val] = curItem[1]
      # print(f'{cousins}')
      if x in cousins and y in cousins and cousins[x] != cousins[y]:
        return True
    return False

sol = Solution()
assert sol.isCousins(deserialize('[1,2,3,4]'), 4, 3) == False
assert sol.isCousins(deserialize('[1,2,3,null,4,null,5]'), 5, 4) == True
assert sol.isCousins(deserialize('[1,2,3,null,4]'), 2, 3) == False
assert sol.isCousins(deserialize('[1,2,null]'), 1, 2) == False