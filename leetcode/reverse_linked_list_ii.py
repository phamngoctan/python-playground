from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    return str(self.val)
class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    count = 0
    firstPointer = None
    secondPointer = head
    while secondPointer:
      count += 1
      if count == left:
        res = self.reverseTo(secondPointer, right - left + 1)
        # self.printNode(res)
        # print('-------')
        break
      firstPointer = secondPointer
      secondPointer = secondPointer.next if secondPointer else None
      
    if firstPointer:
      firstPointer.next = res
    else:
      head = res
      # print(f'current value after {firstPointer}')
    return head
  
  def reverseTo(self, head, to):
    next = head
    prev = None
    count = 1
    
    while next and count <= to:
      cur = next
      next = next.next
      cur.next = prev
      prev = cur
      count += 1
    head.next = next
    return prev 

  def printNode(self, head):
    next = head
    while next != None:
      print(f'{next}')
      next = next.next


sol = Solution()
inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
res = sol.reverseBetween(inputList, 2, 4)
sol.printNode(res)
assert res.next.val == 4
print('-------')

inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = sol.reverseBetween(inputList, 1, 4)
sol.printNode(result)
print('-------')

inputList = ListNode(1)
result = sol.reverseBetween(inputList, 1, 1)
sol.printNode(result)
print('-------')

inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = sol.reverseBetween(inputList, 1, 5)
sol.printNode(result)
print('-------')

inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = sol.reverseBetween(inputList, 1, 1)
sol.printNode(result)

print('-------')

inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = sol.reverseBetween(inputList, 2, 5)
sol.printNode(result)