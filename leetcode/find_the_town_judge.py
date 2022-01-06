from typing import List

class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    '''
    This just works if and only if there is no duplicated entry.
    n = 6
    2,1 3,1 4,1 5,1 6,1
    Every edge comes, increase 1 -> because of the no duplicated
    -> Any other vertex, cannot make two connections to the same vertex.
    -> max count of a vertex should be n - 1. :D
    '''
    if len(trust) < n - 1:
      return -1
    count = [0 for _ in range(n + 1)]
    for a, b in trust:
      count[a] -= 1
      count[b] += 1
    for i in range(1, n + 1):
      if count[i] == n - 1:
        return i
    return -1

sol = Solution()
assert sol.findJudge(2, trust = [[1,2]]) == 2
assert sol.findJudge(3, trust = [[1,3],[2,3]]) == 3
assert sol.findJudge(4, trust = [[1,3],[2,3]]) == -1
assert sol.findJudge(3, trust = [[1,3],[2,3],[3,1]]) == -1
