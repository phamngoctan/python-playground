from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    return str(self.val)

class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    count = 1
    curNode = head
    start = head # right before the left pointer
    while count < left:
      start = curNode
      curNode = curNode.next
      count += 1
    # print(f'{start}')
    # print('------')
    
    tail = curNode # pointer at left value
    # print(f'pointer at left value {tail}')
    listSoFar = None
    next = None
    while count >= left and count <= right:
      next = curNode.next
      curNode.next = listSoFar
      listSoFar = curNode
      curNode = next
      count += 1
    
    
    # print('-------')
    # print(f'right pointer value {curNode}')

    start.next = listSoFar # be careful when changing the order of this and below line, infinitive loop when printing out the head
    tail.next = curNode
    # self.printNode(listSoFar)
    # self.printNode(start)

    return listSoFar if left == 1 else head
  
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
assert result.val == 4
print('-------')

inputList = ListNode(1)
result = sol.reverseBetween(inputList, 1, 1)
sol.printNode(result)
print('-------')

inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = sol.reverseBetween(inputList, 1, 5)
sol.printNode(result)
assert result.val == 5
print('-------')

inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = sol.reverseBetween(inputList, 1, 1)
sol.printNode(result)

print('-------')

inputList = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = sol.reverseBetween(inputList, 2, 5)
sol.printNode(result)