# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    # def helper(self, node: TreeNode) -> int:
    #     if node is None:
    #         return 0
    #     return max(self.helper(node.left), self.helper(node.right)) + 1

s = Solution()
print("None case (should print 0) ", s.maxDepth(None))
print("Only root node (should print 1) ", s.maxDepth(TreeNode(1)))
print("Root and left node (should print 2) ", s.maxDepth((TreeNode(1, TreeNode(2)))))
print("Root and left node and right node (should print 2) ", s.maxDepth((TreeNode(1, TreeNode(2), TreeNode(3)))))
print("Root (should print 3) ", s.maxDepth((TreeNode(1, TreeNode(2, TreeNode(3))))))
