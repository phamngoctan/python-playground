from typing import List

class Solution:
  def findCircleNum(self, isConnected: List[List[int]]) -> int:
    graph = [[] for _ in range(len(isConnected))]
    for i, connectedInfo in enumerate(isConnected):
      for j, node in enumerate(connectedInfo):
        if node and i != j:
          graph[i].append(j)
    # print(f'{graph}')
    visited = [False for _ in range(len(isConnected))]
    def DFS(graph, node):
      visited[node] = True
      neighbors = graph[node]
      for neighbor in neighbors:
        if visited[neighbor]:
          continue
        DFS(graph, neighbor)
    
    ans = 0
    for i in range(len(graph)):
      if not visited[i]:
        DFS(graph, i)
        ans += 1
    return ans
sol = Solution()
assert sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3
assert sol.findCircleNum([[1,0],[0,1]]) == 2
assert sol.findCircleNum([[1,1],[1,1]]) == 1
