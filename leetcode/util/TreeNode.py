class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)
    def __eq__(self, obj):
        return isinstance(obj, TreeNode) and obj.val == self.val
    def __hash__(self):
        return hash((id(self), self.val))