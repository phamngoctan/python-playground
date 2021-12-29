from typing import List, Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
    '''
    I know this problem use monotonic stack to solve.
    I can solve it by myself, so pround of me
    '''
    stack = []
    for i in range(len(nums)):
      previousNode = None
      while stack and stack[-1].val < nums[i]:
        tmp = stack.pop()
        tmp.right = previousNode
        previousNode = tmp
        # print(f'{tmp}')
      cur = TreeNode(nums[i])
      cur.left = previousNode
      # stack.append(nums[i])
      stack.append(cur)
    
    # print(f'{stack}')
    previousNode = None
    while stack:
      tmp = stack.pop()
      tmp.right = previousNode
      previousNode = tmp
    # print(f'{previousNode}')
    return previousNode
  
sol = Solution()
expectTree = deserialize('[6,3,5,null,2,0,null,null,1]')
root = sol.constructMaximumBinaryTree([3,2,1,4,6,0,5])
assert root.val == expectTree.val
root = sol.constructMaximumBinaryTree([3,2,1,6,0,5])
