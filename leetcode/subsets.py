from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path, ans):
            ans.append(path)
            for i in range(len(nums)):
                backtrack(nums[i + 1:], path + [nums[i]], ans)
        ans = []
        backtrack(nums, [], ans)
        # print(f'{ans}')
        return ans

sol = Solution()
assert sol.subsets([1,2,3]) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
assert sol.subsets([1,2,3,4]) == [[], [1], [1, 2], [1, 2, 3], [1,2,3,4], [1,2,4], [1, 3], [1,3,4], [1,4], [2], [2, 3], [2,3,4], [2,4], [3], [3,4], [4]]
