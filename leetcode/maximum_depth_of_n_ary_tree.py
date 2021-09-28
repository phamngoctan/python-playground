from util import NArrayNode as Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
  def maxDepth(self, root: 'Node') -> int:
    if not root:
      return 0
    def dfs(root, level):
      if not root:
        return
      maxDepth = level
      for i in range(len(root.children)):
        maxDepth = max(maxDepth, dfs(root.children[i], level + 1))
      return maxDepth
    return dfs(root, 0) + 1
