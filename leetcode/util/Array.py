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
      This method does not match the expectation from Leetcode, please use the deserialize instead
  """  
  # Base case for recursion
  def insertLevelOrder(arr, root, i, n):
    # Base case for recursion
    if i < n and arr[i] != None:
      root = TreeNode(arr[i])
      # insert left child
      root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
      # insert right child
      root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root
  return insertLevelOrder(array_nums, None, 0, len(array_nums))

def deserialize(string):
  if string == '{}' or string == '[]':
    return None
  nodes = [None if val == 'null' else TreeNode(int(val))
            for val in string.strip('[]{}').split(',')]
  kids = nodes[::-1]
  root = kids.pop()
  for node in nodes:
    if node:
      if kids: node.left  = kids.pop()
      if kids: node.right = kids.pop()
  return root

def printInOrder(node:TreeNode):
  if not node:
    return
  printInOrder(node.left)
  print(f'{node.val}')
  printInOrder(node.right)

if __name__ == '__main__':
  
  bst = array_to_bst([1,4,2,3,5,6,8])
  # printInOrder(bst)
  # bst = deserialize('[2,null,3,null,4,null,5,null,6]')
  # printInOrder(bst)
  # bst = deserialize('[]')
  # printInOrder(bst)
  bst = deserialize('[3,9,20,null,null,15,7]')
  printInOrder(bst)
  