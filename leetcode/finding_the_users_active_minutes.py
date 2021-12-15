import collections
from typing import List
from collections import defaultdict

class Solution:
  def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
    hashActionsByUser = defaultdict(set)
    for user, minute in logs:
      hashActionsByUser[user].add(minute)
    # print(f'{hashActionsByUser}')
    ans = [0 for _ in range(k)]
    for _, value in hashActionsByUser.items():
      if len(value) > 0 and len(value) <= k:
        ans[len(value) - 1] += 1
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5) == [0,2,0,0,0]
assert sol.findingUsersActiveMinutes([[1,1],[2,2],[2,3]], k = 4) == [1,1,0,0]
