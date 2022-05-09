from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.preComputeSums = []
        cur = 0
        for i, val in enumerate(nums):
            cur = cur + val
            self.preComputeSums.append(cur)
        print(f"{self.preComputeSums}")

    def sumRange(self, left: int, right: int) -> int:
        return self.preComputeSums[right] - (self.preComputeSums[left - 1] if left > 0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)