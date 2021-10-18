from typing import Optional
from typing import List
from util.Array import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
    def generateSubtrees(start, end):
      if start > end:
        return [None]
      res = []
      for i in range(start, end + 1):
        left = generateSubtrees(start, i - 1)
        right = generateSubtrees(i + 1, end)
        for l in left:
          for r in right:
            node = TreeNode(i)
            node.left = l
            node.right = r
            res.append(node)
      return res
    return generateSubtrees(1, n)

  def generateTrees_2(self, n: int) -> List[Optional[TreeNode]]:
    def generateSubtrees(start, end):
      if start > end:
        return [None]
      res = []
      if start + 1 == end:
        newNode1 = TreeNode(start)
        newNode1.right = TreeNode(end)
        res.append(newNode1)
        newNode2 = TreeNode(end)
        newNode2.left = TreeNode(start)
        res.append(newNode2)
        return res
      
      for i in range(start, end + 1):
        left = generateSubtrees(start, i - 1)
        right = generateSubtrees(i + 1, end)
        for l in left:
          for r in right:
            node = TreeNode(i)
            node.left = l
            node.right = r
            res.append(node)
      return res
    if n == 1:
      return [TreeNode(1)]
    return generateSubtrees(1, n)

sol = Solution()
res = sol.generateTrees(1)
res = sol.generateTrees(2)
res = sol.generateTrees(3)
res = sol.generateTrees(4)
res = sol.generateTrees(5)
res = sol.generateTrees(6)
res = sol.generateTrees(7)
res = sol.generateTrees(8)
print(f'{res}')