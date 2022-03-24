from typing import Optional
from util.TreeNode import TreeNode
from util.Array import deserialize
from util.Array import printInOrder

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val > key:
            # really a tricky part, without this, you have to manage the parent node, it is really painful
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else: # handle when node is found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # find the min node on the right branch
            minNode = self.findMin(root.right)
            root.val = minNode.val
            # print(f"Min val on the right of target: {minNode.val}")
            root.right = self.deleteNode(root.right, minNode.val)
        return root
    
    def findMin(self, root):
        while root.left:
            root = root.left
        return root

sol = Solution()
actual = sol.deleteNode(deserialize('[5,3,6,2,4,null,7]'), 3)
printInOrder(actual)
