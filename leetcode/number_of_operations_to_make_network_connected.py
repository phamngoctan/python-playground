from typing import List

class Solution:
  def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    if len(connections) < n - 1:
      return -1
    adjacencyList = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for connection in connections:
      adjacencyList[connection[0]].append(connection[1])
      adjacencyList[connection[1]].append(connection[0])
    
    def dfs(adjacencyList, vertex):
      visited[vertex] = True
      neighbors = adjacencyList[vertex]
      for neighbor in neighbors:
        if not visited[neighbor]:
          dfs(adjacencyList, neighbor)

    count = 0
    for i in range(n):
      if not visited[i]:
        dfs(adjacencyList, i)
        count += 1
    # print(f'{count - 1}')
    return count - 1
sol = Solution()
assert sol.makeConnected(4, [[0,1],[0,2],[1,2]]) == 1
assert sol.makeConnected(4, [[0,1],[0,2]]) == -1
assert sol.makeConnected(4, [[0,1],[0,2], [1,3]]) == 0
assert sol.makeConnected(5, connections = [[0,1],[0,2],[3,4],[2,3]]) == 0
