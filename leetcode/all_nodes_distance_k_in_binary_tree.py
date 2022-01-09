from typing import List
from util.TreeNode import TreeNode
from util.Array import deserialize
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
  def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """ Borrow idea from LC - Lee215
    """
    def buildConnectionHash(parent, node):
      if not node: return
      if parent and node: # preorder
        connect[parent.val].append(node.val)
        connect[node.val].append(parent.val)
      buildConnectionHash(node, node.left)
      buildConnectionHash(node, node.right)
    connect = collections.defaultdict(list)
    buildConnectionHash(None, root)
    
    # print(f'{connect}')
    # start the breadth-first search from the target, hence the starting level is 0
    levelVertice = [target.val]
    seen = set(levelVertice)
    for i in range(k):
      newLevel = []
      for vertex in levelVertice:
        for val in connect[vertex]:
          if not val in seen:
            newLevel.append(val)
            seen.add(val)
      levelVertice = newLevel
    # print(f'{levelVertice}')
    return levelVertice

sol = Solution()
assert sol.distanceK(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), 2) == [1,7,4]
assert sol.distanceK(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), 3) == [0,8]
assert sol.distanceK(deserialize('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5), 1) == [3,6,2]
assert sol.distanceK(deserialize('[]'), TreeNode(1), 3) == []
