from typing import List
from util.Node import Node
from queue import PriorityQueue

class Solution:
  
  def demoDijkstra(self, numberOfNodes, times:List, start):
    '''
    Start the node from 1, NOT 0
    '''
    INF = 1e9
    adjacentList = [[] for i in range(numberOfNodes + 1)]
    for i in range(len(times)):
      item = times[i]
      adjacentList[item[0]].append(Node(item[1], item[2]))
    print(f'{(adjacentList)}')
    dist = [INF for i in range(numberOfNodes + 1)]
    print(f'{dist}')
    dir = [-1 for i in range(numberOfNodes + 1)]
    print(f'{dir}')
    print('-----------------------')
    def dijkstra(start):
      pq = PriorityQueue()
      pq.put(Node(start, 0))
      dist[start] = 0
      while not pq.empty():
        curNode = pq.get()
        v = curNode.id
        w = curNode.dist # this is the cur distance from starting point to curNode
        for neighbor in adjacentList[v]:
          if w + neighbor.dist < dist[neighbor.id]:
            shorterDist = w + neighbor.dist
            dist[neighbor.id] = shorterDist
            pq.put(Node(neighbor.id, shorterDist))
            dir[neighbor.id] = v
    dijkstra(start)
    print(f'{dist}')
    print(f'{dir}')
    # Ignore the zero index please, we start counting from 1
    return dist


if __name__ == '__main__':
  sol = Solution()
  times = [[1,4,2],[1,2,9],[2,5,1],[3,1,5],[3,2,3],[4,2,4],[4,5,6]]
  sol.demoDijkstra(5, times, 1)

  print(f'========================================')
  times = [[1,4,2],[1,2,9],[2,5,1],[3,1,5],[3,2,3],[4,2,4],[4,5,6],[5,3,7]]
  sol.demoDijkstra(5, times, 1)
  