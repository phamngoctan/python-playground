from typing import List

class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n == 1:
      return [0]
    graph = [[] for _ in range(n)] # adjacency list
    for edge in edges:
      graph[edge[0]].append(edge[1])
      graph[edge[1]].append(edge[0])
    leaves = []
    degree = [0 for i in range(n)]
    for i in range(n):
      degree[i] = len(graph[i])
      if len(graph[i]) == 1: # len(graph[i]) == 0 or 
        leaves.append(i)
    # print(f'{leaves}')
    
    newLeaves = None
    while len(leaves) > 0:
      newLeaves = leaves[::]
      for i in range(len(leaves)):
        curLeave = leaves.pop(0)
        neighbors = graph[curLeave]
        for neighbor in neighbors:
          if degree[neighbor] > 0:
            degree[neighbor] -= 1
            if degree[neighbor] == 1:
              leaves.append(neighbor)
        degree[curLeave] = 0
    # print(f'{newLeaves}')
    return newLeaves

sol = Solution()
assert sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]) == [1]
assert sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]) == [3,4]
assert sol.findMinHeightTrees(2, [[0,1]]) == [0,1]
assert sol.findMinHeightTrees(1, []) == [0]
