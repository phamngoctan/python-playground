from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m = {}
        for i in range(len(nums)):
            t = m.get(nums[i], 0)
            m[nums[i]] = t + 1
        preValue = 0
        m2 = {}
        preKey = None
        for k, v in sorted(m.items()):
          if (preKey != k):
            m2[k] = preValue
            preValue = preValue + v
          preKey = k      

        ans = []
        for i in range(len(nums)):
            ans.append(m2[nums[i]])
        return ans
s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))