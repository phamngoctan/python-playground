from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
      res = []
      if (n == 0 or n == 1):
        return nums
      half = n
      res.append(nums[0])
      res.append(nums[half])

      for i in range(1, int(half)):
        res.append(nums[i])
        res.append(nums[half + i])
      return res
s = Solution()
print(s.shuffle([2,5,1,3,4,7], 3))