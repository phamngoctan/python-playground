from typing import Optional
from util.TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time complexity for tree deserialize is O(n)
        Time complexity for checking a string is contained in another string is O(m * n)
        Actually, we can have it O(n) but it is not neccessary to check it in this easy problem
        """
        rootStr = self.treeDeserialize(root)
        subRootStr = self.treeDeserialize(subRoot)
        return subRootStr in rootStr
    
    def treeDeserialize(self, root):
        if not root:
            return "null"
        return str(root.val) + "," + self.treeDeserialize(root.left) + "," + self.treeDeserialize(root.right)
    
    """
    This approach will check very node in root with all node in subRoot
    So time complexity is: O(m*n)
    """
    def isSubtree_bruceforce(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.compareTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def compareTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        elif root and not subRoot:
            return False
        elif root.val != subRoot.val:
            return False
        else:
            return self.compareTree(root.left, subRoot.left) and self.compareTree(root.right, subRoot.right)