from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(ans, nums, [])
        return ans
    def backtrack(self, ans, nums, path):
        # print(f"{path}")
        if len(path) == len(nums):
            ans.append(path[::])
            return
        
        for num in nums:
            if num in path: # without this check, the ans contain the duplicate elements.
                continue
            path.append(num)
            self.backtrack(ans, nums, path)
            path.pop()

