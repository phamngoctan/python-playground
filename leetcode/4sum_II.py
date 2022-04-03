from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hash = {}
        for n1 in nums1:
            for n2 in nums2:
                if not (n1 + n2) in hash:
                    hash[n1+n2] = 0
                hash[n1 + n2] += 1
        # print(f'{hash}')
        ans = 0
        for n3 in nums3:
            for n4 in nums4:
                if -(n3 + n4) in hash:
                    ans += hash[-(n3 + n4)]
        return ans
sol = Solution()
assert sol.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]) == 2
assert sol.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]) == 1
