from typing import List

class Solution:
  def maximumUniqueSubarray(self, nums: List[int]) -> int:
    hash = {}
    ans = curSum = 0
    start = 0
    for end, num in enumerate(nums):
      if num in hash:
        while start <= hash[num]:
          curSum -= nums[start]
          start += 1
      hash[num] = end
      curSum += num
      ans = max(ans, curSum)
    # print(f'{ans}')
    return ans
  
  '''
  1 <= nums[i] <= 10**4
  '''
  def maximumUniqueSubarray_mySolution(self, nums: List[int]) -> int:
    hash = {nums[0]:0}
    ans = nums[0]
    curSum = nums[0]
    start = 0
    for end in range(1, len(nums)):
      num = nums[end]
      if num in hash and hash[num] != -1:
        pos = hash[num]
        while start <= pos:
          curSum -= nums[start]
          nums[start] = -1
          start += 1
      hash[num] = end
      curSum += num
      ans = max(ans, curSum)
    # print(f'{ans}')
    return ans

sol = Solution()
assert sol.maximumUniqueSubarray([5,2,1,2,3,4]) == 10
assert sol.maximumUniqueSubarray([1]) == 1
assert sol.maximumUniqueSubarray([2]) == 2
assert sol.maximumUniqueSubarray([2,2]) == 2
assert sol.maximumUniqueSubarray([4,2,4,5,6]) == 17
assert sol.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]) == 8
assert sol.maximumUniqueSubarray([2,2,3]) == 5
assert sol.maximumUniqueSubarray([187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]) == 16911
