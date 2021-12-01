from typing import List

class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    target = len(graph) - 1
    ans = []
    def DFS(graph, curVertex, targetVertex, curPath):
      if curVertex == targetVertex:
        ans.append(curPath[::])
      neighbors = graph[curVertex]
      if not neighbors:
        return
      for neighbor in neighbors:
        curPath.append(neighbor)
        DFS(graph, neighbor, targetVertex, curPath)
        curPath.pop()
    DFS(graph, 0, target, [0])
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.allPathsSourceTarget([[1,2],[3],[3],[]], ) == [[0,1,3],[0,2,3]]
assert sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
