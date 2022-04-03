from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums, i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        # Bubble sort, swap two adjacent elements, after first loop, max value is bubbled to top
        # for i in range(len(nums)):
        #     for j in range(len(nums) - i - 1):
        #         if nums[j] > nums[j + 1]:
        #             print(f"Swap {j} vs {j + 1}")
        #             swap(nums, j, j + 1)
        
        # Insertion sort, maintain the first sorted list
        # for i in range(len(nums)):
        #     val = nums[i]
        #     j = i - 1
        #     # find the correct position for putting current val to
        #     while j >= 0 and val < nums[j]:
        #         # 1, 3, 5, 2, 7
        #         # let say in position of 2
        #         # while 2 < 5, 3, swap 5 vs 2, swap 3 vs 2
        #         nums[j + 1] = nums[j]
        #         j = j - 1
        #     nums[j + 1] = val
        
        # selection sort, find the min value in the second list, mark it, swap
        # for i in range(len(nums)):
        #     minIdx = i
        #     for j in range(i, len(nums)):
        #         if nums[j] < nums[minIdx]:
        #             minIdx = j
        #     swap(nums, minIdx, i)
        
        # merge sort,
#         def mergeTwoSortedList(nums, left, mid, right):
#             """
#             [1,5,6, 2,3,4]
#             """
#             s1, s2 = left, mid + 1
#             # tmpArr = [0] * (right - left)
#             tmpArr = []
#             while s1 <= mid and s2 <= right:
#                 if nums[s1] <= nums[s2]:
#                     tmpArr.append(nums[s1])
#                     s1 += 1
#                 else:
#                     tmpArr.append(nums[s2])
#                     s2 += 1
#             while s1 <= mid:
#                 tmpArr.append(nums[s1])
#                 s1 += 1
#             while s2 <= right:
#                 tmpArr.append(nums[s2])
#                 s2 += 1
#             for i in range(left, right + 1):
#                 nums[i] = tmpArr[i - left]
#             # print(f"left to right {left}:{right} {nums[left:right+1]}")
                
#         def mergeSort(nums, left, right):
#             if left >= right:
#                 return
#             mid = (left + right) // 2
#             mergeSort(nums, left, mid)
#             mergeSort(nums, mid + 1, right)
#             mergeTwoSortedList(nums, left, mid, right)
#         mergeSort(nums, 0, len(nums) - 1)

        def quickSort(nums, left, right):
            if left < right:
                partitionIdx = partition(nums, left, right)
                quickSort(nums, left, partitionIdx - 1)
                quickSort(nums, partitionIdx + 1, right)
        def partition(nums, left, right):
            pivot = nums[right]
            partitionIdx = left
            for j in range(left, right):
                if nums[j] < pivot:
                    swap(nums, partitionIdx, j)
                    partitionIdx += 1
            swap(nums, partitionIdx, right)
            return partitionIdx
        quickSort(nums, 0, len(nums) - 1)