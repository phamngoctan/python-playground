from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        fre = [0] * 101
        for i in range(len(nums)):
            fre[nums[i]] += 1
        
        pre = 0
        for i in range(101):
          if fre[i] > 0:
            temp = fre[i]
            fre[i] = pre
            pre = pre + temp
        return [fre[i] for i in nums]
s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))
# expect [4, 0, 1, 1, 3]