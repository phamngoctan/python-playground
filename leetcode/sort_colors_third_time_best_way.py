from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, left, right):
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
        
        zeroIdx, threeIdx = 0, len(nums) - 1
        idx = 0
        while idx <= threeIdx:
            if nums[idx] == 2:
                swap(nums, idx, threeIdx)
                threeIdx -= 1
            elif nums[idx] == 0:
                swap(nums, zeroIdx, idx)
                zeroIdx += 1
                idx += 1
            else:
                idx += 1