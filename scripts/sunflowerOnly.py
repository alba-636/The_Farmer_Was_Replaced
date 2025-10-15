from __builtins__ import *
from common import *

farmSize = 5

clear()

def farm(worldSize):
  initialX = get_pos_x()
  initialY = get_pos_y()

  while True:
    # Go to starting position
    goToPosition(initialX, initialY)

    for i in range(worldSize):
      for y in range(worldSize):
        if get_ground_type() != Grounds.Soil:
          till()

        if can_harvest():
          harvest()

        if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
          plant(Entities.Sunflower)

        useWater(0.5)

        if y != worldSize - 1:
          if isEven(i):
            move(North)
          else:
            move(South)

      if i != worldSize - 1:
        move(East)

def drone():
  farm(farmSize)

staringPositions = buildStartingPositions(farmSize, farmSize)

for i in range(len(staringPositions)):
  if i == 0:
    continue
  goToPosition(staringPositions[i][0], staringPositions[i][1])
  spawn_drone(drone)

goToPosition(0, 0)
drone()
