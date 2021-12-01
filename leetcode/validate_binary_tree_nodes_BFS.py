from typing import List

class Solution:
  def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    '''
    Main idea: pick any root, run the BFS from this root
    Inside the BFS, if a node is visited two times => invalid
    If visiting all nodes -> valid
    Else -> invalid (there are more than one root)
    '''
    root = None
    childrenNodes = set(leftChild + rightChild) # Not in children nodes means the root one :)
    for i in range(n):
      if i not in childrenNodes:
        root = i
        break
    if root == None:
      return False # no root :)

    visited = [False for _ in range(n)]
    queue = [root]
    
    while queue:
      cur = queue.pop(0)
      if visited[cur]:
        return False # cycle inside
      visited[cur] = True
      if leftChild[cur] != -1:
        queue.append(leftChild[cur])
      if rightChild[cur] != -1:
        queue.append(rightChild[cur])
    # print(f'{visited.count(True)}')
    return visited.count(True) == n

sol = Solution()
assert sol.validateBinaryTreeNodes(4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]) == True
assert sol.validateBinaryTreeNodes(4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]) == False
assert sol.validateBinaryTreeNodes(2, leftChild = [1,0], rightChild = [-1,-1]) == False
assert sol.validateBinaryTreeNodes(6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]) == False
assert sol.validateBinaryTreeNodes(3, leftChild = [1,-1,-1], rightChild = [-1,-1,1]) == False
assert sol.validateBinaryTreeNodes(4, leftChild = [-1,0,1,2], rightChild = [-1,-1,-1,-1]) == True
