from util.Array import deserialize
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

class Solution:
  def diameterOfBinaryTree(self, root: TreeNode) -> int:
    if root is None:
      return 0
    def helper(node):
      if not node:
        return [0,0]
      left = helper(node.left)
      right = helper(node.right)
      currentHeight = max(left[0], right[0]) + 1
      cur = [currentHeight, max(left[0] + right[0] + 1, left[1], right[1])]
      return cur
    res = helper(root)
    # print(res)
    return max(res) - 1

  def curHeight(self, root: TreeNode):
    if root is None:
      return [0, 0]

    cur_height, cur_diameter = 0, 0
    res_left = self.curHeight(root.left)
    res_right = self.curHeight(root.right)
    cur_height = max(res_left[1], res_right[1])

    cur_diameter = max(res_left[1] + res_right[1] + 1, res_left[0], res_right[0])
    # print(root.val, " ", [cur_diameter, cur_height + 1])
    return [cur_diameter, cur_height + 1]


s = Solution()
print("t1 node: ", s.diameterOfBinaryTree(TreeNode(1)))
print("t2 node: ", s.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))))
print("t2:  ", s.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(9, TreeNode(10))), TreeNode(5)), TreeNode(3))))
treeNode2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(9, TreeNode(10))), TreeNode(5, TreeNode(6, TreeNode(7), TreeNode(8)))), TreeNode(3))
print("Second input: ", s.diameterOfBinaryTree(treeNode2))
treeNode3 = TreeNode(2)
print("Second input: ", s.diameterOfBinaryTree(treeNode3))
assert s.diameterOfBinaryTree(deserialize('[1,2,3,4,5]')) == 3