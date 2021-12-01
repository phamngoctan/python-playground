from typing import List

class Solution:
  def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    parent = [i for i in range(n)]
    # ranks = [0 for _ in range(n)]
    def findSet(u):
      while u != parent[u]:
        u = parent[u]
      return u
    def unionSet(u, v):
      uParent = findSet(u)
      vParent = findSet(v)
      if uParent == vParent or uParent != u:
        # == in case forming the cycle
        # second check for two head  0 -> 1, 1 already has the root is 0
        # and we try to set the second root for 1 with new v value
        return False
      # if ranks[uParent] < ranks[vParent]:
      #   parent[uParent] = vParent
      # elif ranks[uParent] > ranks[vParent]:
      #   parent[vParent] = uParent
      # else:
      #   parent[uParent] = vParent
      #   ranks[vParent] += 1
      parent[uParent] = vParent
      return True
    def checkChild(children):
      for i, node in enumerate(children):
        if node != -1:
          if not unionSet(node, i):
            return False
      return True
    if not checkChild(leftChild) or not checkChild(rightChild):
      return False
    firstParent = findSet(0)
    for i in range(1, n):
      if firstParent != findSet(i):
        return False
    return True

sol = Solution()
assert sol.validateBinaryTreeNodes(4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]) == True
assert sol.validateBinaryTreeNodes(4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]) == False
assert sol.validateBinaryTreeNodes(2, leftChild = [1,0], rightChild = [-1,-1]) == False
assert sol.validateBinaryTreeNodes(6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]) == False
assert sol.validateBinaryTreeNodes(3, leftChild = [1,-1,-1], rightChild = [-1,-1,1]) == False
assert sol.validateBinaryTreeNodes(4, leftChild = [-1,0,1,2], rightChild = [-1,-1,-1,-1]) == True
