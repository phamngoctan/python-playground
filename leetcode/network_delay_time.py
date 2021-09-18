from typing import List
from util.Node import Node
from queue import PriorityQueue

class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    # prepare
    INF = 1e4
    graph = [[] for i in range(n + 1)]
    for time in times:
      graph[time[0]].append(Node(time[1], time[2]))
    dist = [INF for i in range(n + 1)]
    def dijkstra(start):
      pq = PriorityQueue()
      dist[start] = 0
      pq.put(Node(start, 0))
      while not pq.empty():
        curNode = pq.get()
        v = curNode.id
        w = curNode.dist
        for neighbor in graph[v]:
          if w + neighbor.dist < dist[neighbor.id]:
            shorterDist = w + neighbor.dist
            dist[neighbor.id] = shorterDist
            pq.put(Node(neighbor.id, shorterDist))
    dijkstra(k)
    # print(f'{dist}')
    res = -1
    for i in range(1, n + 1):
      if dist[i] == INF:
        return -1
      res = max(res, dist[i])
    return res
sol = Solution()
assert sol.networkDelayTime([[1,4,2],[1,2,9],[2,5,1],[3,1,5],[3,2,3],[4,2,4],[4,5,6],[5,3,7]], 5, 1) == 14
assert sol.networkDelayTime([[1,4,2],[1,2,9],[2,5,1],[3,1,5],[3,2,3],[4,2,4],[4,5,6]], 5, 1) == -1
assert sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert sol.networkDelayTime([[1,2,1]], 2, 1) == 1
assert sol.networkDelayTime([[1,2,1]], 2, 2) == -1
