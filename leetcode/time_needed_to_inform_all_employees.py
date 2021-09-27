from typing import List

class Solution:
  def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    adjacentList = [[] for i in range(n)] 
    for i in range(n):
      if manager[i] != -1:
        adjacentList[manager[i]].append(i) # the adjacent list will have one more item due to the -1 of the head manager
    # print(f'{adjacentList}')
    # visited = [False for i in range(n)]
    # print(f'{visited}')
    def dfs(adjacentList, pos):
      # visited[pos] = True
      adjacents = adjacentList[pos]
      maxTime = 0
      for i in range(len(adjacents)):
        # print(f'{adjacents[i]}')
        # don't need the visited because it has no cyclic inside :)
        # if not visited[adjacents[i]]:
        maxTime = max(dfs(adjacentList, adjacents[i]), maxTime)
      return maxTime + informTime[pos]
    return dfs(adjacentList, headID)
    
      
sol = Solution()
# assert sol.numOfMinutes(n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]) == 1
# assert sol.numOfMinutes(n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]) == 21
# assert sol.numOfMinutes(n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]) == 3
assert sol.numOfMinutes(n = 8, headID = 4, manager = [2,2,4,6,-1,4,4,5], informTime = [0,0,4,0,7,3,6,0]) == 13
# assert sol.numOfMinutes(n = 1, headID = 0, manager = [-1], informTime = [1]) == 1

