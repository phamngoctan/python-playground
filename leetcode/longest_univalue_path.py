from typing import Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#     def __hash__(self):
#         return hash((id(), self.val))
class Solution:
  def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
    '''
    This is my solution, not good but I pround of it.
    '''
    if not root:
      return 0
    def longestUnivaluePathHelper(root):
      if not root:
        return 0
      def DFS(root, dp):
        if not root:
          return [0,0]
        left = [0,0]
        if root.left and root.left.val == root.val:
          left = DFS(root.left, dp)
        right = [0,0]
        if root.right and root.right.val == root.val:
          right = DFS(root.right, dp)
        
        current = max(left[0], right[0]) + 1
        return [current, max(left[1], right[1], left[0] + right[0] + 1)]
      dp = {}
      currentRootMax = max(DFS(root, dp))
      ans = max(currentRootMax,
                longestUnivaluePathHelper(root.left), 
                longestUnivaluePathHelper(root.right))
      return ans
    ans = longestUnivaluePathHelper(root) - 1
    # print(f'{ans}')
    return ans
  
  # def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
  #   if not root:
  #     return 0
  #   def DFS(root):
  #     if not root:
  #       return 0
  #     count = 0
  #     if root.left and root.left.val == root.val:
  #       count += DFS(root.left)
  #     if root.right and root.right.val == root.val:
  #       count += DFS(root.right)
  #     return count + 1
  #   ans = max(max(DFS(root), DFS(root.left)), DFS(root.right))
  #   # print(f'{ans}')
  #   return ans - 1
sol = Solution()
assert sol.longestUnivaluePath(deserialize('[]')) == 0
assert sol.longestUnivaluePath(deserialize('[1,4,5,1,1,5]')) == 1
assert sol.longestUnivaluePath(deserialize('[5,4,5,1,1,5]')) == 2
assert sol.longestUnivaluePath(deserialize('[1,4,5,4,4,5]')) == 2
assert sol.longestUnivaluePath(deserialize('[1,4,5,4,4,5,4,4]')) == 3
assert sol.longestUnivaluePath(deserialize('[1,null,1,1,1,1,1,1]')) == 4
assert sol.longestUnivaluePath(deserialize('[79,99,77,null,null,null,69,null,60,53,null,73,11,null,null,null,62,27,62,null,null,98,50,null,null,90,48,82,null,null,null,55,64,null,null,73,56,6,47,null,93,null,null,75,44,30,82,null,null,null,null,null,null,57,36,89,42,null,null,76,10,null,null,null,null,null,32,4,18,null,null,1,7,null,null,42,64,null,null,39,76,null,null,6,null,66,8,96,91,38,38,null,null,null,null,74,42,null,null,null,10,40,5,null,null,null,null,28,8,24,47,null,null,null,17,36,50,19,63,33,89,null,null,null,null,null,null,null,null,94,72,null,null,79,25,null,null,51,null,70,84,43,null,64,35,null,null,null,null,40,78,null,null,35,42,98,96,null,null,82,26,null,null,null,null,48,91,null,null,35,93,86,42,null,null,null,null,0,61,null,null,67,null,53,48,null,null,82,30,null,97,null,null,null,1,null,null]')) == 1
assert sol.longestUnivaluePath(deserialize('[69,73,68,18,20,18,39,7,-3,13,-1,42,5,93,70,63,17,null,91,-4,30,null,-1,64,-4,16,49,48,78,51,43,92,45,null,53,9,36,80,-6,58,78,null,null,41,81,89,67,71,null,25,null,82,54,28,14,61,57,35,5,83,9,18,null,-9,-9,50,92,93,null,0,80,62,1,28,29,27,89,21,null,85,-9,null,56,56,-9,null,null,43,null,29,97,-7,null,35,25,90,67,53,18,61,7,23,81,37,19,26,2,0,19,null,null,77,37,-2,null,49,39,28,1,37,11,87,83,68,55,53,33,-2,22,7,52,null,14,null,18,50,97,-8,-7,null,21,59,72,27,null,64,null,null,47,null,null,38,46,null,null,99,null,null,48,13,85,78,7,64,43,59,71,11,37,12,37,50,2,null,null,89,87,null,78,97,null,31,86,37,96,34,38,6,36,null,null,99,63,null,12,null,82,null,81,70,19,null,81,32,null,null,null,null,79,10,null,91,48,-3,94,65,null,20,26,96,21,92,91,null,89,9,74,null,null,96,null,64,67,50,96,null,null,null,null,null,null,40,78,null,27,3,17,null,null,2,45,null,null,null,null,null,13,null,null,17,45,69,30,null,null,43,null,4,13,-6,66,6,null,16,48,55,98,69,57,null,5,9,65,-9,55,2,null,null,null,null,null,null,68,null,null,null,5,61,51,null,null,32,43,null,35,20,null,-7,38,30,1,80,null,null,42,86,42,null,null,null,null,47,null,null,null,62,29,-9,83,60,71,48,null,24,null,76,6,65,18,95,29,11,null,38,null,null,null,null,21,3,6,23,36,null,45,null,34,null,null,null,null,null,null,41,null,57,13,18,92,43,83,null,null,null,null,null,null,null,2,-4,97,null,93,null,62,null,null,48,18,71,92,53,89,null,null,null,95,null,16,null,null,null,83,87,5,null,null,3,-8,-4,65,null,null,null,22,null,31,null,null,null,63,null,null,62,null,57,12,85,45,23,55,null,null,null,81,83,23,null,3,null,83,null,-4,null,null,null,null,null,64,null,15,50,57,null,null,null,4,null,null,null,29,null,null,87,null,22,92,null,null,67,90,null,93,47,46,null,null,null,28,72,18,59,25,3,74,null,null,null,-5,28,-1,61,15,null,null,null,null,79,null,16,null,null,59,47,-7,98,31,50,null,null,null,null,19,null,93,null,22,null,null,-5,40,null,null,null,75,30,null,7,53,76,null,null,null,null,null,68,19,null,63,41,91,null,43,null,49,null,null,null,null,null,46,null,null,87,74,49,1,21,62,6,34,77,null,null,null,null,null,null,-9,61,null,null,null,7,null,45,null,null,63,null,null,7,null,null,16,86,null,null,63,null,61,72,null,13,null,24,91,null,null,59,null,null,48,14,77,null,null,null,null,92,null,null,null,null,null,null,84,null,null,76,82,63,84,84,94,null,null,null,null,null,47,40,null,null,null,null,75,20,null,null,null,-9,null,null,24,74,null,51,null,null,91,null,83,17,null,null,null,42,49,88,57,85,1,null,94,null,28,36,78,null,53,null,27,25,46,97,58,null,null,null,null,null,null,null,null,12,33,null,null,6,null,null,null,87,null,null,null,null,null,null,null,9,null,83,null,null,null,90,11,null,61,null,89,null,46,null,86,81,null,null,null,null,null,null,null,53,null,null,59,null,null,null,null,null,null,null,29,null,47,97,0,null,null,null,null,9,null,17,null,91,45,9,61,21,null,null,64,null,69,null,44,null,null,null,null,12,null,2,-8,88,null,null,null,null,null,-8,null,93,null,null,null,86,null,null,97,null,null,null,null,72,null,null,null,null,null,50,null,null,null,null,null,47,70,null,62,null,-3,-5,59,15,null,-3,37,null,null,null,null,20,-2,null,8,90,null,null,null,61,null,null,null,null,null,null,null,15,12,95,null,null,73,11,76,76,49,null,null,51,null,null,null,null,null,null,null,null,null,null,null,null,null,42,null,null,-9,null,null,null,null,null,null,null,null,80,null,null,70,31,78,98,null,null,null,null,null,null,null,null,null,null,null,null,7,null,null,null,null,57,null,null,null,null,-3,null,null,-7,null,31,42,null,null,null,null,62,17,7,null,null,63,null,null,null,null,83,51,null,76,77,null,null,40,null,null,95,null,27,55,61,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,95,null,93,19,null,37,null,73,null,null,null,null,null,75,null,null,null,null,null,22,null,null,null,null,null,-7,99,null,null,null,null,null,94,63,null,null,null,null,null,null,null,39,77,null,-2,15,null,69,33,9,null,null,null,null,null,null,null,null,null,42,null,null,null,69,35,null,36,null,11,null,null,null,52,null,null,null,null,null,null,null,51,50,null,null,null,null,null,null,30,null,null,null,null,null,63,null,null,null,null,null,null,56,28]')) == 1
