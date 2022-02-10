from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cur = 0
        hash = {}
        hash[0] = 1
        for i in range(len(nums)):
            cur += nums[i]
            if (cur - k) in hash:
                ans += hash[cur - k]
            hash.setdefault(cur, 0)
            hash[cur] += 1
        # print(f'{hash}')
        return ans

sol = Solution()
assert sol.subarraySum([1,1,1], k = 2) == 2
assert sol.subarraySum([1,2,3], k = 3) == 2
assert sol.subarraySum([1,-1,1,1], k = 2) == 2
assert sol.subarraySum([1,-1,1,1], k = 3) == 0
