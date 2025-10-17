# From: Alba-636
# Leaderboard: Hay
# Best time: 01:58:727
# Rank: #8
# At: 2025-10-17

from __builtins__ import *
from common import *

set_world_size(24)

def hasSuccess():
  return num_items(Items.Hay) >= 2000000000

def farm(initialX, initialY, index):
  farmSize = 4
  xMax = 3
  companionType = Entities.Bush
  if index == 26 or index == 27 or index == 28 or index == 29:
    offsetX = initialX + 3
    offsetY = initialY + 4
    for x in range(farmSize):
      for y in range(farmSize):
        if isEven(x):
          goToPosition(offsetX - x, y + offsetY)
        else:
          goToPosition(offsetX - x, xMax - y + offsetY)
          
        plant(companionType)

  for x in range(farmSize):
    for y in range(farmSize):
      if isEven(x):
        goToPosition(x + initialX, y + initialY)
      else:
        goToPosition(x + initialX, xMax - y + initialY)
      
      if not (x == 0 and y == 0) and not (x == 3 and y == 3):
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

staringPositions = buildStartingPositions(4, 4)
for i in range(len(staringPositions)):
  def drone():
    farm(staringPositions[i][0], staringPositions[i][1], i)
  if i == 31:
    drone()
    break
  spawn_drone(drone)
