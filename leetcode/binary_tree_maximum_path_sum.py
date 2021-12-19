from typing import Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    def DFS(node):
      if not node:
        return [float('-inf'), float('-inf')]
      # leftMax = max(DFS(node.left), 0)  
      # rightMax = max(DFS(node.right), 0)
      # currentMax = max(0, node.val) + leftMax + rightMax
      # self.ans = max(self.ans, currentMax)
      leftMax,leftMaxSoFar = DFS(node.left)
      rightMax,rightMaxSoFar = DFS(node.right)
      
      currentMax = node.val + max(leftMax, rightMax, 0)
      currentMaxSoFar = node.val + max(leftMax, 0) + max(rightMax, 0)
      return [currentMax, max(currentMaxSoFar, leftMaxSoFar, rightMaxSoFar)]
    _, ans = DFS(root)
    # print(f'{ans}')
    return ans
  
  def maxPathSum_myselfThinking(self, root: Optional[TreeNode]) -> int:
    '''
    Using global variable to store the max so far
    '''
    self.ans = float('-inf')
    def DFS(node):
      if not node:
        return 0
      leftMax = DFS(node.left)
      rightMax = DFS(node.right)
      self.ans = max(self.ans, node.val + max(leftMax, 0) + max(rightMax, 0))
      return node.val + max(leftMax, rightMax, 0)
    DFS(root)
    # print(f'{self.ans}')
    return self.ans

sol = Solution()
assert sol.maxPathSum(deserialize('[53,73,11,null,null,null,62,27,62]')) == 261
assert sol.maxPathSum(deserialize('[-9,-10,-11]')) == -9
assert sol.maxPathSum(deserialize('[-9,-10]')) == -9
assert sol.maxPathSum(deserialize('[-9]')) == -9
assert sol.maxPathSum(deserialize('[-10,-9]')) == -9
assert sol.maxPathSum(deserialize('[9]')) == 9
assert sol.maxPathSum(deserialize('[-10,9]')) == 9
assert sol.maxPathSum(deserialize('[-10,-1,-1,null,null,-1,70]')) == 70
assert sol.maxPathSum(deserialize('[79,99,77,null,null,null,69,null,60,53,null,73,11,null,null,null,62,27,62,null,null,98,50,null,null,90,48,82,null,null,null,55,64,null,null,73,56,6,47,null,93,null,null,75,44,30,82,null,null,null,null,null,null,57,36,89,42,null,null,76,10,null,null,null,null,null,32,4,18,null,null,1,7,null,null,42,64,null,null,39,76,null,null,6,null,66,8,96,91,38,38,null,null,null,null,74,42,null,null,null,10,40,5,null,null,null,null,28,8,24,47,null,null,null,17,36,50,19,63,33,89,null,null,null,null,null,null,null,null,94,72,null,null,79,25,null,null,51,null,70,84,43,null,64,35,null,null,null,null,40,78,null,null,35,42,98,96,null,null,82,26,null,null,null,null,48,91,null,null,35,93,86,42,null,null,null,null,0,61,null,null,67,null,53,48,null,null,82,30,null,97,null,null,null,1,null,null]')) == 2769
