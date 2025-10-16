# From: Alba-636
# Leaderboard: Hay_Single
# Best time: 03:37.712
# Rank: #29
# At: 2025-10-16

from __builtins__ import *
from common import *

set_world_size(3)

companionType = Entities.Bush
farmSize = 3
for x in range(farmSize):
  for y in range(farmSize):
    goToPosition(x, y)
    plant(companionType)

def hasSuccess():
  return num_items(Items.Hay) >= 100000000 # 100_000_000

while True:
  if hasSuccess():
    break

  plantType, (_, _) = get_companion()
  if can_harvest() or plantType != companionType:
    harvest()
  else:
    use_item(Items.Water, 4)

