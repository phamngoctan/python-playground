from typing import List

class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    '''
    Time complexity n log n
    '''
    graph = [[] for _ in range(len(isConnected))]
    for i, connectedInfo in enumerate(isConnected):
      for j, node in enumerate(connectedInfo):
        if node and i != j:
          graph[i].append(j)
    # print(f'{graph}')
    
    parent = [i for i in range(len(isConnected))]
    ranks = [0 for _ in range(len(isConnected))]
    def findSet(u):
      while u != parent[u]:
        u = parent[u]
      return u
    def unionSet(u, v):
      uParent = findSet(u)
      vParent = findSet(v)
      if vParent == uParent:
        return
      if ranks[uParent] > ranks[vParent]:
        parent[vParent] = uParent
      elif ranks[uParent] < ranks[vParent]:
        parent[uParent] = vParent
      else:
        parent[uParent] = vParent
        ranks[vParent] += 1
    
    for i in range(len(graph)):
      for j in range(len(graph[i])):
        unionSet(i, graph[i][j])
    # print(f'{parent}')
    ans = 0
    for i in range(len(parent)):
      if i == parent[i]:
        ans += 1
    return ans
sol = Solution()
assert sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3
assert sol.findCircleNum([[1,0],[0,1]]) == 2
assert sol.findCircleNum([[1,1],[1,1]]) == 1
