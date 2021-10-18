from typing import Optional
from util.Array import TreeNode
from util.Array import deserialize

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = [0,k]
        def helper(node):
            if res[1] < 0:
                return
            if node.left:
                helper(node.left)
            res[1] -= 1
            if res[1] == 0:
                res[0] = node.val
                # print(f'{node.val}')
                return
            if node.right:
                helper(node.right)
        helper(root)
        # print(f'{res}')
        return res[0]

sol = Solution()
assert sol.kthSmallest(deserialize('[3,1,4,null,2]'), k = 1) == 1
assert sol.kthSmallest(deserialize('[5,3,6,2,4,null,null,1]'), k = 3) == 3
assert sol.kthSmallest(deserialize('[3,1,4]'), k = 2) == 3
assert sol.kthSmallest(deserialize('[3]'), k = 1) == 3
