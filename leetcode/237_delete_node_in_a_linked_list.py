class Solution:
  def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    slow = None
    fast = node
    while fast and fast.next:
        fast.val = fast.next.val
        slow = fast
        fast = fast.next
    slow.next = None