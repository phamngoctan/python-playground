
# Definition for a Node.
class Node:
  def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next

class Solution:
  def connect(self, root: 'Node') -> 'Node':
    if not root:
      return None
    queue = []
    queue.append(root)
    while queue:
      qsize = len(queue)
      for i in range(qsize):
        cur = queue.pop(0)
        cur.next = queue[0] if i < qsize - 1 else None
        if cur.left:
          queue.append(cur.left)
        if cur.right:
          queue.append(cur.right)
    return root

sol = Solution()
root = Node(1, 
            left=Node(2,
                      left=Node(4),
                      right=Node(5)), 
            right=Node(3,
                       left=Node(6),
                       right=Node(7)))
actual = sol.connect(root)
assert actual.next == None
assert actual.left.next.val == 3
assert actual.right.next == None
assert actual.left.left.val == 4
assert actual.left.left.next.val == 5