from typing import List

class Solution:
  def countHighestScoreNodes(self, parents: List[int]) -> int:
    n = len(parents)
    # print(n)
    adjacencyList = [[] for _ in range(n)]
    for i in range(1, len(parents)):
      adjacencyList[parents[i]].append(i)
    # degree = [0 for _ in range(n)]
    # leaves = []
    # for i in range(n):
    #   degree[i] = len(adjacencyList[i])
    #   if degree[i] == 0:
    #     leaves.append(i)
    # print(f'{degree}')
    # numberOfNodes = [0 for _ in range(n)]
    # while len(leaves) > 0:
    #   leaves.pop(0)
    cache = [0 for _ in range(n + 1)]
    def dfs(graph, node):
      if cache[node] == 0:
        neighbors = graph[node]
        if len(neighbors) == 0:
          cache[node] = 1
        else:
          total = 0
          for neighbor in neighbors:
            total += dfs(graph, neighbor)
          cache[node] = total + 1
      return cache[node]
    dfs(adjacencyList, 0)
    # print(f'{cache}')
    score = [0 for _ in range(n)]
    maxScore = 0
    res = []
    for i in range(n):
      left = adjacencyList[i][0] if len(adjacencyList[i]) >= 1 else n
      right = adjacencyList[i][1] if len(adjacencyList[i]) == 2 else n
      # parent = cache[parents[i]] - 1 if parents[i] != -1 else 1
      parent = cache[0] - 1 - cache[left] - cache[right]
      if i == 0:
        parent += 1
      score[i] = parent * (cache[left] or 1) * (cache[right] or 1)
      # print(f'i = {i} score {score[i]}')
      if score[i] > maxScore:
        maxScore = score[i]
        res = [i]
      elif score[i] == maxScore:
        res.append(i)
      
    # print(f'{res}')
    return len(res)


sol = Solution()
assert sol.countHighestScoreNodes([-1,2,0,2,0]) == 3
assert sol.countHighestScoreNodes([-1,0]) == 2
