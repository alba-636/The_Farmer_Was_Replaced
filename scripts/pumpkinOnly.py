from __builtins__ import *
from common import *

farmSize = 6

clear()

def farm():
  initialX = get_pos_x()
  initialY = get_pos_y()

  while True:
    goToPosition(initialX, initialY)

    gatherable_count = 0
    for i in range(farmSize):
      for y in range(farmSize):
        if get_ground_type() != Grounds.Soil:
          till()

        if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
          plant(Entities.Pumpkin)

        if can_harvest():
          gatherable_count += 1

        useWater(0.2)

        if y != farmSize - 1:
          if isEven(i):
            move(North)
          else:
            move(South)

      if i != farmSize - 1:
        move(East)

    if gatherable_count == farmSize ** 2:
      harvest()

staringPositions = buildStartingPositions(7, 7)

for i in range(len(staringPositions)):
  if i == 0:
    continue
  goToPosition(staringPositions[i][0], staringPositions[i][1])
  spawn_drone(farm)

goToPosition(0, 0)
farm()
