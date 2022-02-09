from email.policy import default
from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """Borrow idea from LC"""
        counter = {}
        for num in nums:
            counter.setdefault(num, 0)
            counter[num] += 1
        # print(f'{counter}')
        ans = 0
        for val in counter.keys():
            if k == 0: # k == 0 means that at least a duplicated val must be existed to increase the ans
                ans += 1 if counter[val] > 1 else 0
            else:
                ans += 1 if (val + k) in counter else 0
        return ans

    def findPairs_myIdea(self, nums: List[int], k: int) -> int:
        """the space complexity is not good"""
        hash = {}
        ans = set()
        for i, num in enumerate(nums):
            if (num - k) in hash:
                if not (num - k, num) in ans:
                    ans.add((num, num - k))
            if (k + num) in hash:
                if not (k + num, num) in ans:
                    ans.add((num, k + num))
            if not num in hash:
                hash[num] = 1
        # print(f'{ans}')
        return len(ans)
sol = Solution()
assert sol.findPairs([3,1,4,1,5], k = 2) == 2
assert sol.findPairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1], k = 0) == 1
assert sol.findPairs([1,2,4,4,3,3,0,9,2,3], k = 3) == 2
assert sol.findPairs([6,3,5,7,2,3,3,8,2,4], k = 2) == 5
