from typing import List, Optional
from util.TreeNode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.hash = {}
        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            self.hash.setdefault(root.val, 0)
            self.hash[root.val] += 1
        dfs(root)
        maxCount = 0
        ans = []
        for k, v in self.hash.items():
            if v > maxCount:
                ans = [k]
                maxCount = v
            elif v == maxCount:
                ans.append(k)
        return ans
        
    """
    [6,2,8,0,4,7,9,null,null,2,6]
    """
    def findMode_wrongForThisTest(self, root: Optional[TreeNode]) -> List[int]:
        self.maxCount = 0
        self.maxVals = []
        def dfs(root):
            if not root: return [None, 0]
            valLeft, countLeft = dfs(root.left)
            valRight, countRight = dfs(root.right)
            curCount = 1
            curCount += countLeft if root.val == valLeft else 0
            curCount += countRight if root.val == valRight else 0
            if curCount > self.maxCount:
                self.maxCount = curCount
                self.maxVals = [root.val]
            elif curCount == self.maxCount:
                self.maxVals.append(root.val)
            return [root.val, curCount]
        dfs(root)
        print(f"{self.maxVals}")
        return self.maxVals
