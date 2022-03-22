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

try:
    # Trying to find module in the parent package
    from .ListNode import ListNode
except ImportError:
    # print('Relative import failed')
    pass

try:
    # Trying to find module on sys.path
    from ListNode import ListNode
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

def inOrderTraversal(root:TreeNode):
  def dfs(root, res):
    if not root:
      return
    resLeft = dfs(root.left, res)
    if resLeft:
      res.extends(resLeft)
    res.append(root.val)
    resRight = dfs(root.right, res)
    if resRight:
      res.extends(resRight)
  res = []
  dfs(root, res)
  return res

def printInOrder(node:TreeNode):
  if not node:
    return
  printInOrder(node.left)
  print(f'{node.val}')
  printInOrder(node.right)

def fromArrayToListNode(arr):
  if not arr:
    return None
  head = ListNode(arr[0])
  cur = head
  for i in range(1, len(arr)):
    cur.next = ListNode(arr[i])
    cur = cur.next
  return head

def serialize_demo(root):
    if root is None:
        return []
    result = str(root.val) + ','
    last_level = [root]
    while last_level:
        new_level = []
        for node in last_level:
            result += str(node.left.val) + ',' if node.left is not None else '_,'
            if node.left is not None:
                new_level.append(node.left)
            result += str(node.right.val) + ',' if node.right is not None else '_,'
            if node.right is not None:
                new_level.append(node.right)
        last_level_count = len(last_level)
        last_level = new_level
    return result[:-(last_level_count*4 + 1)]

# def sortedArrayToBST(nums):
#     def convert(left, right):
#         if left > right:
#             return None
#         mid = (left + right) // 2
#         node = TreeNode(nums[mid])
#         node.left = convert(left, mid - 1)
#         node.right = convert(mid + 1, right)
#         return node
#     return convert(0, len(nums) - 1)


if __name__ == '__main__':
  
  bst = array_to_bst([1,4,2,3,5,6,8])
  # printInOrder(bst)
  bst = deserialize('[2,null,3,null,4,null,5,null,6]')
  printInOrder(bst)
  # bst = deserialize('[]')
  # printInOrder(bst)
  bst = deserialize('[3,9,20,null,null,15,7]')
  printInOrder(bst)
  inOrderTraversal(deserialize('[2,null,3,null,4,null,5,null,6]'))

  sorted_array = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12]
  print(f"sorted array: {str(sorted_array)}")
  tree = array_to_bst(sorted_array)
  print('serialized BST for testing in Leetcode: [' + str(serialize_demo(tree)).replace('_', 'null') + ']')
  