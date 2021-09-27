from typing import List

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adjacentList = [[] for i in range(numCourses)]
    inDegree = [0 for i in range(numCourses)]
    for i in range(len(prerequisites)):
      pair = prerequisites[i]
      adjacentList[pair[1]].append(pair[0])
      inDegree[pair[0]] += 1
    # print(f'{adjacentList}')
    # print(f'{inDegree}')

    stack = []
    for i in range(len(inDegree)):
      if inDegree[i] == 0:
        stack.append(i)
    actualProcessedNode = 0
    while stack:
      cur = stack.pop()
      # print(f'popped vertex: {cur}')
      actualProcessedNode += 1
      adjacents = adjacentList[cur]
      for i in range(len(adjacents)):
        next = adjacents[i]
        inDegree[next] -= 1
        if inDegree[next] == 0:
          stack.append(next)
    # print(f'{actualProcessedNode}')
    return actualProcessedNode == numCourses

sol = Solution()
assert sol.canFinish(6, [[1,0],[2,1],[2,5],[0,3],[4,3],[3,5],[4,5]]) == True
assert sol.canFinish(6, [[1,0],[2,1],[5,2],[0,3],[4,3],[3,5],[4,5]]) == False
assert sol.canFinish(2, [[1,0]]) == True
assert sol.canFinish(2, [[1,0],[0,1]]) == False
assert sol.canFinish(3, [[1,0],[2,1],[0,2]]) == False
assert sol.canFinish(3, [[1,0],[0,1],[0,2]]) == False
assert sol.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]) == False
