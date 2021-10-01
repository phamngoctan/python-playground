from typing import List
from util.NArrayNode import Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
  def levelOrder(self, root: 'Node') -> List[List[int]]:
    if not root:
      return []
    def bfs(root):
      queue = [root]
      res = []
      while len(queue) > 0:
        size = len(queue)
        curLevelItems = []
        for _ in range(size):
          curItem = queue.pop(0)
          curLevelItems.append(curItem.val)
          for node in curItem.children:
            queue.append(node)
        res.append(curLevelItems)
      return res
    return bfs(root)