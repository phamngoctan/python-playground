from typing import List
import heapq

class Solution:
  def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    ans = []
    queue = []
    def push(i, j):
      if i < len(nums1) and j < len(nums2): # prevent the multiple if else statement
        # the min heap in auto pick the first element as the comparison
        heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
    push(0, 0)
    while queue and len(ans) < k:
      sum, i, j = heapq.heappop(queue)
      ans.append([nums1[i], nums2[j]])
      push(i, j + 1)
      if j == 0:
        push(i + 1, 0)
    # print(f'{ans}')
    return ans
  
  def kSmallestPairs_betterIdea(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    ans = []
    count = 0
    queue = []
    row = 0
    for i in range(len(nums1)):
      if count < k:
        heapq.heappush(queue, [nums1[i] + nums2[0], nums1[i], row])
        count += 1
      else:
        break
    while len(ans) < k and queue:
      sum, valueAtNums1, row = heapq.heappop(queue)
      ans.append([valueAtNums1, sum - valueAtNums1])
      if row == len(nums2) - 1:
        continue
      heapq.heappush(queue, [valueAtNums1 + nums2[row + 1], valueAtNums1, row + 1])
    return ans
  
  def kSmallestPairs_bruceforce(self, nums1: List[int], nums2: List[int], k: int):
    '''
    Bruceforce
    '''
    product = []
    for i in range(len(nums1)):
      for j in range(len(nums2)):
        product.append((nums1[i], nums2[j]))
    newProduct = sorted(product, key= lambda x: x[0] + x[1])
    # print(f'{newProduct[:k]}')
    return newProduct[:k]
			
sol = Solution()
assert sol.kSmallestPairs(nums1 = [1,7,11], nums2 = [2,4,6], k = 3) == [[1,2],[1,4],[1,6]]
assert sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 2) == [[1,1],[1,1]]
assert sol.kSmallestPairs(nums1 = [1,1,2], nums2 = [1,2,3], k = 3) == [[1,1],[1,1],[1,2]]
assert sol.kSmallestPairs(nums1 = [1,2], nums2 = [3], k = 3) == [[1,3],[2,3]]
