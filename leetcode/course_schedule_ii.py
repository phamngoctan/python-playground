from typing import List

class Solution:
  def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    counting = [0 for _ in range(numCourses)]
    outDegree = [[] for _ in range(numCourses)]
    for prerequisite in prerequisites:
      outDegree[prerequisite[1]].append(prerequisite[0])
      counting[prerequisite[0]] += 1
    # print(f'counting {counting}')
    # print(f'outDegree {outDegree}')
    queue = []
    for i in range(numCourses):
      if counting[i] == 0:
        queue.append(i)
    res = []
    while len(queue) > 0:
      vertex = queue.pop(0)
      res.append(vertex)
      curOutDegree = outDegree[vertex]
      for connectedVertex in curOutDegree:
        counting[connectedVertex] -= 1
        if counting[connectedVertex] == 0:
          queue.append(connectedVertex)
    # print(f'{res}')
    return res if len(res) == numCourses else []
sol = Solution()
assert sol.findOrder(2, prerequisites = [[1,0]]) == [0, 1]
assert sol.findOrder(2, prerequisites = [[1,0], [0,1]]) == []
assert sol.findOrder(4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]) == [0,1,2,3]
assert sol.findOrder(5, prerequisites = [[4,0],[1,0],[2,0],[4,2]]) == [0,3,1,2,4]
assert sol.findOrder(1, prerequisites = []) == [0]
