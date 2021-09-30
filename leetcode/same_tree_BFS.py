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
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def bfs(root1, root2):
      queue1 = [root1]
      queue2 = [root2]
      while queue1 and queue2:
        curRoot1 = queue1.pop(0)
        curRoot2 = queue2.pop(0)
        if curRoot1 and not curRoot2:
          return False
        if not curRoot1 and curRoot2:
          return False
        if not curRoot1 and not curRoot2:
          continue
        if curRoot1.val == curRoot2.val: 
          queue1.append(curRoot1.left)
          queue1.append(curRoot1.right)
          queue2.append(curRoot2.left)
          queue2.append(curRoot2.right)
        else:
          return False
      if queue1 or queue2:
        return False
      return True
    return bfs(p, q)
sol = Solution()
assert sol.isSameTree(deserialize('[1,2,3]'), deserialize('[1,2,3]')) == True
assert sol.isSameTree(deserialize('[1,2]'), deserialize('[1,null,2]')) == False
assert sol.isSameTree(deserialize('[1,2]'), deserialize('[1]')) == False
assert sol.isSameTree(deserialize('[1]'), deserialize('[]')) == False
assert sol.isSameTree(deserialize('[]'), deserialize('[1]')) == False
assert sol.isSameTree(deserialize('[]'), deserialize('[]')) == True
assert sol.isSameTree(deserialize('[1]'), deserialize('[1,null,2]')) == False
