class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        return head

    def __reverse(self, head: ListNone, tail = None) -> ListNode:
        cur = head.next
        head = 
        if cur is None:
            return tail
        else:


s = Solution()
inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
output = s.reverseList(inputList)
print(output)

