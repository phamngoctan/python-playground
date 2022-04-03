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
    """Next time, can try with DFS approach bro."""
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = []
        queue.append([root, 0])
        ans = 0
        while len(queue) > 0:
            curLen = len(queue)
            curLevelMin = queue[0][1]
            curWidth = 1
            for i in range(curLen):
                curItem, pos = queue.pop(0)
                curWidth = pos - curLevelMin + 1
                ans = max(ans, curWidth)
                if curItem.left: 
                    queue.append([curItem.left, pos * 2 + 1])
                if curItem.right: 
                    queue.append([curItem.right, pos * 2 + 2])
        return ans
sol = Solution()
assert sol.widthOfBinaryTree(deserialize('[1,3,2,5,3,null,9]')) == 4
assert sol.widthOfBinaryTree(deserialize('[1,3,null,5,3]')) == 2
assert sol.widthOfBinaryTree(deserialize('[1,3,2,5]')) == 2
