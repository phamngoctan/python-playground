# Definition for singly-linked list.
class ListNode:
  def __init__(self, x, next = None):
    self.val = x
    self.next = next

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    '''
    Super cool idea
    '''
    curA, curB = headA, headB
    while curA != curB:
      curA = headB if curA is None else curA.next
      curB = headA if curB is None else curB.next
    return curA
    
  def getIntersectionNode_myIdea(self, headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
      return None
    stack1 = []
    cur1 = headA
    while cur1:
      stack1.append(cur1)
      cur1 = cur1.next
    stack2 = []
    cur2 = headB
    while cur2:
      stack2.append(cur2)
      cur2 = cur2.next
    ans = None
    while stack1 and stack2 and stack1[-1].val == stack2[-1].val:
      ans = stack1[-1]
      stack1.pop()
      stack2.pop()
    return ans if ans else None
    
sol = Solution()
intersection = ListNode(2, ListNode(4))
head1 = ListNode(1, ListNode(9, ListNode(1, intersection)))
head2 = ListNode(3, intersection)
assert sol.getIntersectionNode(head1, head2).val == 2
