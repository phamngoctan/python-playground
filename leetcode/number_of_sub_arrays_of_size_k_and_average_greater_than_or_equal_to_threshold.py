from typing import List

class Solution:
  def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
    start, curSum, ans = 0, 0, 0
    for i in range(len(arr)):
      curSum += arr[i]
      if i - start + 1 == k:
        if curSum/k >= threshold:
          ans += 1
        curSum -= arr[start]
        start += 1
    # print(f'{ans}')
    return ans
sol = Solution()
assert sol.numOfSubarrays([2,2,2,2,5,5,5,8], k = 3, threshold = 4) == 3
assert sol.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5) == 6
assert sol.numOfSubarrays([2], k = 1, threshold = 2) == 1
assert sol.numOfSubarrays([2], k = 1, threshold = 3) == 0
assert sol.numOfSubarrays([2], k = 1, threshold = 1) == 1
