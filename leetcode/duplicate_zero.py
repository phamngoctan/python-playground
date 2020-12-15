from typing import List
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        index = [0] * len(arr)
        shift = 0
        for i in range(len(arr)):
            # print(arr[i])
            if arr[i] == 0:
                shift += 1
            index[i] += shift

        for i in range(len(arr) - 1, -1, -1):
            if i + index[i] < len(arr):
                arr[i + index[i]] = arr[i]
            if arr[i] == 0 and i + index[i] - 1 < len(arr):
                arr[i + index[i] - 1] = 0

        # print("shift:  ", index)
        return arr

s = Solution()
# input = [1,0,2,3,0,4,5,0]
# print("input:  ", input)
# print("actual: ", s.duplicateZeros(input))
# expect = [1,0,0,2,3,0,0,4]
# print("expect: ", expect)
#
# print("actual: ", s.duplicateZeros([1,2,3]))
# print("actual: ", s.duplicateZeros([1,2,0,3]))


input = [1,0,0,2,0,3]
print("input:  ", input)
print("actual: ", s.duplicateZeros(input))
expect = [1, 0, 0, 0, 0, 2]
print("expect: ", expect)