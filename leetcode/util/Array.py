try:
    # Trying to find module in the parent package
    from .TreeNode import TreeNode
except ImportError:
    # print('Relative import failed')
    pass

try:
    # Trying to find module on sys.path
    from TreeNode import TreeNode
except ModuleNotFoundError:
    # print('Absolute import failed')
    pass


def array_to_bst(array_nums):
  """ at node i, 2*i + 1 is left node, 2*i + 2 is right node
  """  
  # Base case for recursion
  def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n:
      root = TreeNode(arr[i])
      # insert left child
      root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
      # insert right child
      root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root
  return insertLevelOrder(array_nums, None, 0, len(array_nums))

def printInOrder(node:TreeNode):
  if not node:
    return
  printInOrder(node.left)
  print(f'{node.val}')
  printInOrder(node.right)

if __name__ == '__main__':
  
  bst = array_to_bst([1,4,2,3,5,6,8])
  printInOrder(bst)
  