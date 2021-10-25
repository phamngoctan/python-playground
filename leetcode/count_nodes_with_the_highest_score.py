from typing import Counter, List

class Solution:
  def countHighestScoreNodes(self, parents: List[int]) -> int:
    n = len(parents)
    adjacencyList = [[] for _ in range(n)]
    for i in range(1, len(parents)):
      adjacencyList[parents[i]].append(i)
    
    res = [0 for _ in range(n)]
    global count, maxScore
    count, maxScore = 0, 0
    def dfs(graph, node):
      global count, maxScore
      neighbors = graph[node]
      left = dfs(graph, neighbors[0]) if len(neighbors) >= 1 else 0
      right = dfs(graph, neighbors[1]) if len(neighbors) == 2 else 0
      parent = n - left - right - 1
      parent += 1 if node == 0 else 0
      res[node] = parent * (left or 1) * (right or 1)
      if res[node] > maxScore:
        maxScore = res[node]
        count = 1
      elif res[node] == maxScore:
        count += 1
      return left + 1 + right

    dfs(adjacencyList, 0)
    # print(f'{res}')
    return count

sol = Solution()
assert sol.countHighestScoreNodes([-1,2,0,2,0]) == 3
assert sol.countHighestScoreNodes([-1,0]) == 2
