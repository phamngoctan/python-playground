from typing import Optional
from util.TreeNode import TreeNode
from util.Array import deserialize

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        MIN_VAL = float("-INF")
        MAX_VAL = float("INF")
        """
        Do not return anything, modify root in-place instead.
        """
        self.firstWrong = None
        self.secondWrong = None 
        self.pre = TreeNode(MIN_VAL)
        
        def findWrongPos(root):
            if not root: return
            findWrongPos(root.left)
            if self.firstWrong == None and self.pre.val >= root.val:
                # print(f"Found first wrong {root.val} vs {self.pre.val}")
                self.firstWrong = self.pre # The first element is always larger than its next one 
            if self.firstWrong != None and self.pre.val >= root.val:
                self.secondWrong = root # the second element is always smaller than its previous one.
            self.pre = root
            findWrongPos(root.right)
        findWrongPos(root)
        # print(f"{self.firstWrong.val} and {self.secondWrong.val}")

        # Swap the two nodes
        tmp = self.firstWrong.val
        self.firstWrong.val = self.secondWrong.val
        self.secondWrong.val = tmp

    def recoverTree_myWrongRefactor(self, root: Optional[TreeNode]) -> None:
        MIN_VAL = float("-INF")
        self.firstWrong = None
        self.secondWrong = None
        
        def findWrongPos(root, parent):
            if not root: return
            findWrongPos(root.left, root)
            if self.firstWrong == None and parent.val >= root.val:
                print(f"Found first wrong {root.val} vs {parent.val}")
                self.firstWrong = parent
            if self.firstWrong != None and parent.val >= root.val:
                self.secondWrong = root
            findWrongPos(root.right, root)
        findWrongPos(root, TreeNode(MIN_VAL))
        print(f"{self.firstWrong.val} and {self.secondWrong.val}")
        tmp = self.firstWrong.val
        self.firstWrong.val = self.secondWrong.val
        self.secondWrong.val = tmp

sol = Solution()
inputBST = deserialize("[6, 3, 4, 5, 2]") 
# [3, 5, 17, 6, 7]
"""
Run by hand: inorder BST
- To the very left node: 
"""
sol.recoverTree(inputBST)
assert inputBST.val == 6

inputBST = deserialize("[1,3,null,null,2]")
sol.recoverTree(inputBST)
assert inputBST.val == 3

