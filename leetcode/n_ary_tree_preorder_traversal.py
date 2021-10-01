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
  def preorder(self, root: 'Node') -> List[int]:
    if not root:
      return []
    def dfs(root):
      if not root:
        return
      res = [root.val]
      for i in range(len(root.children)):
        res.extend(dfs(root.children[i]))
      return res
    return dfs(root)