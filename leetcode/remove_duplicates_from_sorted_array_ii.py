from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Mix between my idea and LC solution"""
        for i in range(2, len(nums)):
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums[i - 2] = 10**5
        # input  [0,0,1,1,1,1,2,3,3]
        # middle [0, 0, 100000, 100000, 1, 1, 2, 3, 3]
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != 10**5:
                nums[i - count] = nums[i]
            else:
                count += 1
        # print(f'{nums}')
        # print(f'{len(nums) - count}')
        return len(nums) - count
sol = Solution()
input = [0,0,1,1,1,1,2,3,3]
no = sol.removeDuplicates(input)
assert input[0:no] == [0,0,1,1,2,3,3]

input = [1,1,1,2,2,3]
no = sol.removeDuplicates(input)
assert input[0:no] == [1,1,2,2,3]
