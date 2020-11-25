# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur is not None and cur.val != val:
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return cur

s = Solution()
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
print(s.searchBST(root, 2))