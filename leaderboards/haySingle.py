# From: Alba-636
# Leaderboard: Hay_Single
# Best time: 03:03.987
# Rank: #15
# At: 2025-10-17

from __builtins__ import *
from common import *

set_world_size(8)

def hasSuccess():
  return num_items(Items.Hay) >= 100000000 # 100_000_000

farmSize = 8
xMax = 7
companionType = Entities.Bush
for x in range(farmSize):
  for y in range(farmSize):
    if isEven(x):
      goToPosition(x, y)
    else:
      goToPosition(x, xMax - y)
      
    plant(companionType)

goToPosition(3, 3)

isPosA = True

while True:
  if hasSuccess():
    break

  plantType, (_, _) = get_companion()
  if can_harvest() or plantType != companionType:
    harvest()
  elif not can_harvest() and plantType == companionType:
    if isPosA:
      isPosA = False
      move(East)
    else:
      isPosA = True
      move(West)
    useWater(0.95, 1)
