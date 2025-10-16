# From: Alba-636
# Leaderboard: Hay
# Best time: 02:15:013
# Rank: #11
# At: 2025-10-16
from __builtins__ import *
from common import *

set_world_size(24)

def hasSuccess():
  return num_items(Items.Hay) >= 2000000000

def farm(initialX, initialY, index):
  farmSize = 4
  xMax = 3
  companionType = Entities.Bush
  for x in range(farmSize):
    for y in range(farmSize):
      if isEven(x):
        goToPosition(x + initialX, y + initialY)
      else:
        goToPosition(x + initialX, xMax - y + initialY)
        
      plant(companionType)

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

    goToPosition(3 + initialX, initialY)

  while True:
    if hasSuccess():
      break

    plantType, (_, _) = get_companion()
    if can_harvest() or plantType != companionType:
      harvest()
    elif index == 0 and plantType == companionType and num_items(Items.Fertilizer) > 0:
      use_item(Items.Fertilizer, 1)
      if num_items(Items.Weird_Substance) > 0:
        use_item(Items.Weird_Substance, 1)
      harvest()
    else:
      useWater(0.95, 1)

staringPositions = buildStartingPositions(4, 4)
for i in range(len(staringPositions)):
  def drone():
    farm(staringPositions[i][0], staringPositions[i][1], i)
  if i == 31:
    drone()
    break
  spawn_drone(drone)