from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(0, len(numbers), 1):
            if (numbers[i]) in dic:
                return [dic[numbers[i]] + 1, i + 1]
            else:
                dic[target - numbers[i]] = i
        return [None, None]

s = Solution()
print(s.twoSum([2,7,11,15], 9))