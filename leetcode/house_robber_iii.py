from typing import Dict, Optional
from util.Array import deserialize
from util.TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def rob(self, root: Optional[TreeNode]) -> int:
    '''
    Best version for limiting the size of memorization
    '''
    def helper(node):
      if not node:
        return [0,0]
      left = helper(node.left)
      right = helper(node.right)
      maxNotRobValue = max(left[0], left[1]) + max(right[0], right[1])
      maxRobbedValue = left[0] + right[0] + node.val
      return [maxNotRobValue, maxRobbedValue]
    ans = helper(root)
    # print(f'{ans}')
    return max(ans[0], ans[1])
  
  def rob_dp_with_memorization(self, root: Optional[TreeNode]) -> int:
    def helper(node, dp: dict):
      if not node:
        return 0
      val = 0
      if not node in dp:
        if node.left:
          val += helper(node.left.left, dp) + helper(node.left.right, dp)
        if node.right:
          val += helper(node.right.left, dp) + helper(node.right.right, dp)
        dp[node] = max(val + node.val, helper(node.left, dp) + helper(node.right, dp))
      return dp[node]
    ans = helper(root, {})
    print(f'{ans}')
    return ans
  
  def rob_TLE(self, root: Optional[TreeNode]) -> int:
    '''
    Time Limit Exceed version
    '''
    if not root:
      return 0
    val = 0
    if root.left:
      val += self.rob(root.left.left) + self.rob(root.left.right)
    if root.right:
      val += self.rob(root.right.left) + self.rob(root.right.right)
    return max(val + root.val, self.rob(root.left) + self.rob(root.right))


  def rob_failed(self, root: Optional[TreeNode]) -> int:
    ''' Not consider case 4 -> 1 -> 2 -> 3
    this case, max is 7 (4 + 3), but we only consider 4+2 vs 1+3
    '''
    def BFS(node):
      queue = []
      queue.append(root)
      ans = [0,0]
      level = 0
      while len(queue) > 0:
        curLen = len(queue)
        for _ in range(curLen):
          curNode = queue.pop(0)
          ans[level%2] += curNode.val
          if curNode.left:
            queue.append(curNode.left)
          if curNode.right:
            queue.append(curNode.right)
        level += 1
      # print(f'{ans}')
      return ans[0] if ans[0] > ans[1] else ans[1]
    return BFS(root)
sol = Solution()
assert sol.rob(deserialize('[1,2,3]')) == 5
assert sol.rob(deserialize('[3,2,3,null,3,null,1]')) == 7
assert sol.rob(deserialize('[3,4,5,1,3,null,1]')) == 9
assert sol.rob(deserialize('[3,4,5]')) == 9
assert sol.rob(deserialize('[10,4,5]')) == 10
assert sol.rob(deserialize('[4,1,null,2,null,3]')) == 7
assert sol.rob(deserialize('[79,99,77,null,null,null,69,null,60,53,null,73,11,null,null,null,62,27,62,null,null,98,50,null,null,90,48,82,null,null,null,55,64,null,null,73,56,6,47,null,93,null,null,75,44,30,82,null,null,null,null,null,null,57,36,89,42,null,null,76,10,null,null,null,null,null,32,4,18,null,null,1,7,null,null,42,64,null,null,39,76,null,null,6,null,66,8,96,91,38,38,null,null,null,null,74,42,null,null,null,10,40,5,null,null,null,null,28,8,24,47,null,null,null,17,36,50,19,63,33,89,null,null,null,null,null,null,null,null,94,72,null,null,79,25,null,null,51,null,70,84,43,null,64,35,null,null,null,null,40,78,null,null,35,42,98,96,null,null,82,26,null,null,null,null,48,91,null,null,35,93,86,42,null,null,null,null,0,61,null,null,67,null,53,48,null,null,82,30,null,97,null,null,null,1,null,null]')) == 3038
