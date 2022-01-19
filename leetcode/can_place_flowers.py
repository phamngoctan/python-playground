from typing import List

class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    count = 0
    flowerbed = [0] + flowerbed + [0]
    for i in range(1, len(flowerbed) - 1):
      if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
        flowerbed[i] = 1
        count += 1
    return count >= n
  
  def canPlaceFlowers_myVersion(self, flowerbed: List[int], n: int) -> bool:
    consecutiveEmpty = 0
    prev = None
    startWithEmpty = 0
    for i in range(len(flowerbed)):
      if flowerbed[i] == 1:
        if prev == None:
          startWithEmpty = i
          n -= self.calculateSpot(startWithEmpty - 1)
        else:
          consecutiveEmpty = i - prev - 1
          n -= self.calculateSpot(consecutiveEmpty - 2)
        prev = i
    if prev == None:#and startWithEmpty
      totalAvailableBed = len(flowerbed)
      n -= self.calculateSpot(totalAvailableBed)
    else:
      endWithEmpty = len(flowerbed) - 1 - prev
      n -= self.calculateSpot(endWithEmpty - 1)
      
    return True if n <= 0 else False

  def calculateSpot(self, totalSpots):
    if totalSpots <= 0:
      return 0
    canBePlannedSpot = totalSpots // 2
    if 2 * (canBePlannedSpot + 1) - 1 == totalSpots:
      return canBePlannedSpot + 1
    return canBePlannedSpot
    
sol = Solution()
assert sol.canPlaceFlowers([1,0,0,0,1], 1) == True
assert sol.canPlaceFlowers([1,0,0,0,1], 0) == True
assert sol.canPlaceFlowers([1,0,0,0,1], 2) == False
assert sol.canPlaceFlowers([0,0,0,0,0,0,0], 4) == True
assert sol.canPlaceFlowers([1,0,1,0,1,0,1], 0) == True
assert sol.canPlaceFlowers([1,0,0,0,1,0,0], 2) == True
assert sol.canPlaceFlowers([1,0,0,0,1,0,0,1,0,0], 3) == False
assert sol.canPlaceFlowers([1], 1) == False
assert sol.canPlaceFlowers([1,1,1,1,1], 1) == False

# assert sol.calculateSpot(3) == 2