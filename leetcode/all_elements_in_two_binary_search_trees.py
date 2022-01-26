from typing import List
from util.TreeNode import TreeNode
from util.Array import deserialize
from util.Array import array_to_bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    """know that it's → Timsort: in this case, time complexity is (O(n))
    which identifies the two already sorted runs as such and simply merges them
    """
    values = []
    def collect(root): # in-order traversal
      if root:
        collect(root.left)
        values.append(root.val)
        collect(root.right)
    collect(root1)
    collect(root2)
    return sorted(values)
  
  def getAllElements_myIdea(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    def getSortedArr(root):
      stack = []
      sortedArr = []
      self.appendTheLeftFace(root, stack)
      # print(stack)
      while stack:
        cur = stack.pop()
        sortedArr.append(cur.val)
        self.appendTheLeftFace(cur.right, stack)
      return sortedArr
    root1SortedArr = getSortedArr(root1)
    # print(f'{root1SortedArr}')
    root2SortedArr = getSortedArr(root2)
    # print(f'{root2SortedArr}')
    i, j = 0, 0
    ans = []
    while i < len(root1SortedArr) and j < len(root2SortedArr):
      if root1SortedArr[i] < root2SortedArr[j]:
        ans.append(root1SortedArr[i])
        i += 1
      else:
        ans.append(root2SortedArr[j])
        j += 1
    ans.extend(root1SortedArr[i:len(root1SortedArr)])
    ans.extend(root2SortedArr[j:len(root2SortedArr)])
    # print(f'{ans}')
    return ans
  
  def appendTheLeftFace(self, root, stack):
    tmp = root
    while tmp:
      stack.append(tmp)
      tmp = tmp.left
      
sol = Solution()
assert sol.getAllElements(deserialize('[190,100,194,1,150,null,null,null,null,140,null,130,null,120,null,110,125]'), deserialize('[1,0,3]')) == [0, 1, 1, 3, 100, 110, 120, 125, 130, 140, 150, 190, 194]
assert sol.getAllElements(deserialize('[2,1,4]'), deserialize('[1,0,3]')) == [0,1,1,2,3,4]
assert sol.getAllElements(deserialize('[2,1,4,null,null,3,9]'), deserialize('[1,0,3]')) == [0,1,1,2,3,3,4,9]
assert sol.getAllElements(deserialize('[]'), deserialize('[1,0,3]')) == [0,1,3]
assert sol.getAllElements(deserialize('[]'), deserialize('[]')) == []
