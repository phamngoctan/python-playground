from typing import List
from collections import defaultdict

class Solution:
  def minJumps(self, arr: List[int]) -> int:
    N = len(arr)
    hash = defaultdict(list)
    for i, val in enumerate(arr):
      hash[val].append(i)
    queue, visited = [[0,0]], set()
    while queue:
      steps, index = queue.pop(0)
      if index == N - 1: # reach the last position
        return steps
      
      for neighbor in [index - 1, index + 1]:
        if 0 <= neighbor < N and neighbor not in visited:
          visited.add(neighbor)
          queue.append([steps + 1, neighbor])
      
      # this can cause the TLE because the duplicated items inside the array
      # for example: arr [1,1,1,1,1,7]
      # for first time, it adds 1 value n - 1 times
      # from 2nd time to n - 1 time, it will loop all but not adds to the queue any more
      # => TLE
      # Solution: using visited_groups set to mark it as visited
      # Or remove the neighbor index (duplicated item) our of the hash
      for neighbor in hash[arr[index]]:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append([steps + 1, neighbor])
      del hash[arr[index]]

  
  def minJumps_notYetSolveVersion(self, arr: List[int]) -> int:
    N = len(arr)
    hash = defaultdict(list)
    for i, val in enumerate(arr):
      hash[val].append(i)
    dp = {}
    def dfs(pos, count, dp):
      if pos < 0 or pos >= N:
        return float('inf')
      if pos == N - 1:
        return count

      if not pos in dp:
        curPosMinValue = float('inf')
        curPosMinValue = min(dfs(pos + 1, count + 1, dp), curPosMinValue)
        # curPosMinValue = min(dfs(pos - 1, count + 1, dp), curPosMinValue)
        if arr[pos] in hash:
          for i in hash[arr[pos]]:
            if i != pos:
              curPosMinValue = min(dfs(i, count + 1, dp), curPosMinValue)
        dp[pos] = curPosMinValue
      return dp[pos]
    dfs(0, 0, dp)
    print(f'{self.ans}')
    return self.ans

sol = Solution()
# assert sol.minJumps([100,-23,-23,404,100,23,23,23,3,404]) == 3
# assert sol.minJumps([7]) == 0
# assert sol.minJumps([7,6,9,6,9,6,9,7]) == 1
assert sol.minJumps([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,7]) == 2
