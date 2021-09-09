from typing import Optional
from typing import List
from util.TreeNode import TreeNode
from util.Array import array_to_bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    queue = []
    queue.append(root)
    res = []
    while queue:
      queueLength = len(queue)
      levelNode = []
      for i in range(queueLength):
        node = queue.pop(0)
        if node:
          queue.append(node.left)
          queue.append(node.right)
          if node.val != None:
            levelNode.append(node.val)
    
      if levelNode:
        res.append(levelNode)
      # print(f'{levelNode}')
    return res

sol = Solution()
# assert sol.levelOrder(array_to_bst([3,9,20,None,None,15,7])) == [[3],[9,20],[15,7]]
# assert sol.levelOrder(array_to_bst([1])) == [[1]]
# assert sol.levelOrder(array_to_bst([])) == []
assert sol.levelOrder(array_to_bst([0,2,4,1,None,3,-1,5,1,None,6,None,8])) == [[0],[2,4],[1,3,-1],[5,1,6,8]]
