from typing import List
from queue import PriorityQueue
import collections
import heapq

class Solution:
  def findCheapestPrice(self, n, flights, src, dst, k):
    visited = {}
    graph = collections.defaultdict(list)
    for s, d, p in flights:
        graph[s].append((d, p))
    heap = [(0, 0, src)]
    while heap:
        dist, moves, node = heapq.heappop(heap)
        if node == dst and k >= moves - 1:
            return dist
        if node not in visited or visited[node] > moves:
            visited[node] = moves
            for nei, weight in graph[node]:
                heapq.heappush(heap, (dist + weight, moves + 1, nei))
    return -1
  
  def findCheapestPrice_TLE(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    graph = [[] for _ in range(n)]
    for fromCity, toCity, price in flights:
      graph[fromCity].append([toCity, price])
    # print(f'{graph}')
    dist = [float("inf") for _ in range(n)]
    pqueue = PriorityQueue()
    pqueue.put([0, src, k + 1])
    dist[src] = 0
    while pqueue.qsize() > 0:
      curPrice, curCity, stops = pqueue.get()
      # if curPrice > dist[curCity]:
      #   continue
      if curCity == dst:
        return curPrice
      if stops == 0:
        continue
      for toCity, cost in graph[curCity]:
        pqueue.put([curPrice + cost, toCity, stops - 1])
        # newDist = curPrice + cost
        # if newDist < dist[toCity]:
        #   dist[toCity] = newDist
        #   pqueue.put([newDist, toCity])
    # print(f'{dist}')
    # print(f'{dist[dst]}')
    return -1
        
sol = Solution()
assert sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1) == 200
