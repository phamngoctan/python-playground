class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class Solution:
  def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    next = head
    while next != None:
      cur = next
      next = next.next
      cur.next = prev
      prev = cur
    return prev

s = Solution()
inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output = s.reverseList(inputList)
print(output)

