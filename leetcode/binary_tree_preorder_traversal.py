from typing import Optional
from typing import List
from util.Array import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
sol = Solution()
sol.preorderTraversal(deserialize('[1,null,2,3]')) == [1,2,3]
sol.preorderTraversal(deserialize('[1]')) == [1]
sol.preorderTraversal(deserialize('[]')) == []
sol.preorderTraversal(deserialize('[1,2]')) == [1,2]
sol.preorderTraversal(deserialize('[1,null,2]')) == [1,2]
