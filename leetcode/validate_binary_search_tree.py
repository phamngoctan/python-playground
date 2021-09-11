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
  # def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
    # def dfs(root, preNode, fromLeft):
    #   if not root:
    #     return True
    #   if not isNodeValid(root) or (fromLeft and not isRightNodeValid(root, preNode)) or (not fromLeft and not isLeftNodeValid(root, preNode)):
    #     return False
    #   return dfs(root.left, root, True) and dfs(root.right, root, False)

    # def isNodeValid(root):
    #   leftNode = root.left
    #   rightNode = root.right
    #   if leftNode and leftNode.val >= root.val:
    #     return False
    #   if rightNode and rightNode.val <= root.val:
    #     return False
    #   return True
    
    # def isRightNodeValid(root, preNode):
    #   if preNode and root.right != None and root.right.val >= preNode.val:
    #     return False
    #   return True
    
    # def isLeftNodeValid(root, preNode):
    #   if preNode and root.left != None and root.left.val <= preNode.val:
    #     return False
    #   return True
  
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(root, mustGreaterThanValue, mustLessThanValue):
      if root == None:
        return True
      # print(f'{root}')
      rootVal = root.val
      if mustGreaterThanValue >= rootVal:
        return False
      if mustLessThanValue <= rootVal:
        return False      
      return dfs(root.left, mustGreaterThanValue, rootVal) and dfs(root.right, rootVal, mustLessThanValue)
    return dfs(root, -2**32, 2**32 - 1)

sol = Solution()
assert sol.isValidBST(deserialize('[2147483647]')) == True # 2**31 - 1
assert sol.isValidBST(deserialize('[-2147483648]')) == True # -2**31
assert sol.isValidBST(deserialize('[2,2,2]')) == False
assert sol.isValidBST(deserialize('[120,70,140,50,100,130,160,20,55,75,110,119,135,150,200]')) == False
assert sol.isValidBST(deserialize('[3,1,5,0,2,4,6]')) == True
assert sol.isValidBST(deserialize('[2,1,3]')) == True
assert sol.isValidBST(deserialize('[5,1,4,null,null,3,6]')) == False
assert sol.isValidBST(deserialize('[2]')) == True
assert sol.isValidBST(deserialize('[2,1,null]')) == True
assert sol.isValidBST(deserialize('[2,3,null]')) == False
assert sol.isValidBST(deserialize('[2,null,1]')) == False
assert sol.isValidBST(deserialize('[2,null,3]')) == True
assert sol.isValidBST(deserialize('[12,7,18,5,9,null,25,null,null,null,null,17]')) == False
