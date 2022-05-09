# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        result = ""
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        return str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = data.split(",")
        return self._buildTree(queue)
        
    def _buildTree(self, queue):
        val = queue.pop(0)
        if val == "#":
            return None
        else:
            newNode = TreeNode(int(val))
            newNode.left = self._buildTree(queue)
            newNode.right = self._buildTree(queue)
            return newNode
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

#      1
#     / \
#    3   4
#   / \   \
#  2   5   7
tree = TreeNode(1)
tree.left = TreeNode(3)
tree.right = TreeNode(4)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(5)
tree.right.right = TreeNode(7)
print(str(tree))
# string = serialize(tree)

ser = Codec()
deser = Codec()
print(ser.serialize(tree))
ans = deser.deserialize(ser.serialize(tree))
print(ans)