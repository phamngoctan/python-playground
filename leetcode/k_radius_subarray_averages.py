from typing import List

class Solution:
  def getAverages(self, nums: List[int], k: int) -> List[int]:
    realDistance = k * 2 + 1
    start = 0
    ans = [-1 for _ in range(len(nums))]
    curSum = 0
    for i in range(len(nums)):
      curSum += nums[i]
      if i - start + 1 == realDistance:
        ans[start + k] = curSum // realDistance
        curSum -= nums[start]
        start += 1
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.getAverages([7,4,3,9,1,8,5,2,6], k = 3) == [-1,-1,-1,5,4,4,-1,-1,-1]
assert sol.getAverages([100000], k = 0) == [100000]
assert sol.getAverages([8], k = 100000) == [-1]
