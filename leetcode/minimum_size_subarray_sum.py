from typing import List

class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    '''
    Sliding window approach
    '''
    MAX_VALUE = 10**5 + 1
    res = MAX_VALUE
    curSum = 0
    start = 0
    for end in range(len(nums)):
      curSum += nums[end]
      while curSum >= target:
        res = min(res, end - start + 1)
        curSum -= nums[start]
        start += 1
    # print(f'{res}')
    return res if res != MAX_VALUE else 0

  def minSubArrayLenWronglyApproach(self, target: int, nums: List[int]) -> int:
    '''
    This will not work because this problem requires the >= target
    '''
    MAX_VALUE = 10**5 + 1
    prefixSumHash = {0:-1}
    res = MAX_VALUE
    curSum = 0
    for i in range(len(nums)):
      curSum += nums[i]
      if curSum - target in prefixSumHash:
        res = min(res, i - prefixSumHash[curSum - target])
      prefixSumHash[curSum] = i
    # print(f'{res}')
    return res if res != MAX_VALUE else 0
sol = Solution()
assert sol.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
assert sol.minSubArrayLen(5, [2,3,1,2,4,3]) == 2
assert sol.minSubArrayLen(6, [2,3,1,2,4,3]) == 2
assert sol.minSubArrayLen(4, nums = [1,4,4]) == 1
assert sol.minSubArrayLen(11, nums = [1,1,1,1,1,1,1,1]) == 0
assert sol.minSubArrayLen(9, nums = [1,1,1,1,1,1,1,1,1]) == 9
assert sol.minSubArrayLen(11, nums = [1,2,3,4,5]) == 3

# res = 1 == 2 and 1 == 2 or 1 == 1
# print(f'{res}')