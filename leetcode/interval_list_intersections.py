from typing import List

class Solution:
  def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i = j = 0
    ans = []
    while i < len(firstList) and j < len(secondList):
      if self.isOverlapped(firstList[i], secondList[j]):
        ans.append(self.getOverlapped(firstList[i], secondList[j]))
      if firstList[i][1] < secondList[j][1]:
        i += 1
      else:
        j += 1
    return ans
  def isOverlapped(self, segmentA, segmentB):
    return segmentA[0] <= segmentB[1] and segmentB[0] <= segmentA[1]
  def getOverlapped(self, segmentA, segmentB):
    return [max(segmentA[0], segmentB[0]), min(segmentA[1], segmentB[1])]
  
  def intervalIntersection_anotherIdea(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    i = j = 0
    ans = []
    while i < len(firstList) and j < len(secondList):
      overlappedSegment = self.getOverlapped(firstList[i], secondList[j])
      if self.isValidSegment(overlappedSegment):
        ans.append(overlappedSegment)
      if firstList[i][1] < secondList[j][1]:
        i += 1
      else:
        j += 1
    return ans
  def isValidSegment(self, segment):
    return segment[0] <= segment[1]
    
sol = Solution()
assert sol.intervalIntersection(
  firstList   = [[0,2],[5,10],[13,23],[24,25]], 
  secondList  = [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
assert sol.intervalIntersection(
  firstList = [[1,3],[5,9]], 
  secondList = []) == []
assert sol.intervalIntersection(
  firstList = [], 
  secondList = [[4,8],[10,12]]) == []
assert sol.intervalIntersection(
  firstList = [[1,7]], 
  secondList = [[3,10]]) == [[3,7]]
