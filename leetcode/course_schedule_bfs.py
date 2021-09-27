from typing import List

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adjacentList = [[] for i in range(numCourses)]
    for i in range(len(prerequisites)):
      adjacentList[prerequisites[i][1]].append(prerequisites[i][0])
    # print(f'{adjacentList}')
    
    def bfs(start, rootVal):
      visited[start] = True
      queue = [start]
      while queue:
        length = len(queue)
        for _ in range(length):
          cur = queue.pop(0)
          visited[cur] = True
          for i in adjacentList[cur]:
            if i == rootVal:
              return False
            if not visited[i]:
              queue.append(i)
      return True

    for i in range(numCourses):
      visited = [False for i in range(numCourses)]
      if not bfs(i, i):
        return False
      # else:
      #   print(f'position {i} is good to go')
       
    return True

sol = Solution()
assert sol.canFinish(6, [[1,0],[2,1],[2,5],[0,3],[4,3],[3,5],[4,5]]) == True
assert sol.canFinish(2, [[1,0]]) == True
assert sol.canFinish(2, [[1,0],[0,1]]) == False
assert sol.canFinish(3, [[1,0],[2,1],[0,2]]) == False
assert sol.canFinish(3, [[1,0],[0,1],[0,2]]) == False
assert sol.canFinish(4, [[2,0],[1,0],[3,1],[3,2],[1,3]]) == False
