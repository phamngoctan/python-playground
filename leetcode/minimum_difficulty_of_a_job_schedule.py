from typing import List

class Solution:
  def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
    n = len(jobDifficulty)
    if n < d: # could not schedule the job for each day
      return -1
    
    hardestJobRemaining = [0] * n
    hardestJob = 0
    for i in range(n - 1, -1, -1):
      hardestJob = max(hardestJob, jobDifficulty[i])
      hardestJobRemaining[i] = hardestJob
    # print(f'{hardestJobRemaining}')
    
    def dp(memo, day, i):
      if day == d:
        # the maximum job difficulty between job i and the end of the array (inclusive)
        memo[(day, i)] = hardestJobRemaining[i] 
        return hardestJobRemaining[i]
      if not (day, i) in memo:
        best = float('inf')
        hardest = 0
        for j in range(i, n - (d - day)):
          hardest = max(hardest, jobDifficulty[j])
          best = min(best, hardest + dp(memo, day + 1, j + 1))
        memo[(day, i)] = best
      return memo[(day, i)]
    memo = {}
    ans = dp(memo, 1, 0)
    print(f'{memo}')
    print(f'{ans}')
    return ans

sol = Solution()
assert sol.minDifficulty([6,5,4,3,2,1], d = 2) == 7
assert sol.minDifficulty([6,5,4,3,2,1], d = 3) == 9
assert sol.minDifficulty([9,9,9], d = 4) == -1
assert sol.minDifficulty([1,1,1], d = 3) == 3