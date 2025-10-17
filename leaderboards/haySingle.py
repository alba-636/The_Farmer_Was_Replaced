# From: Alba-636
# Leaderboard: Hay_Single
# Best time: 02:57.539
# Rank: #11
# At: 2025-10-17

from __builtins__ import *
from common import *

set_world_size(5)

def hasSuccess():
  return num_items(Items.Hay) >= 100000000 # 100_000_000

farmSize = 5
xMax = farmSize - 1
companionType = Entities.Bush
for x in range(farmSize):
  for y in range(farmSize):
    if isEven(x):
      goToPosition(x, y)
    else:
      goToPosition(x, xMax - y)
      
    if not (x == 0 and y == 4) and not (x == 4 and y == 4):
      plant(companionType)

isPosA = True

while True:
  if hasSuccess():
    break

  plantType, (_, _) = get_companion()
  if can_harvest() or plantType != companionType:
    harvest()
  elif not can_harvest() and plantType == companionType:
    useWater(0.8, 4)
    if isPosA:
      isPosA = False
      move(East)
    else:
      isPosA = True
      move(West)

