from __builtins__ import *
from common import *

farmSize = 6

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

        if get_water() < 0.2:
          use_item(Items.Water)

        if y != worldSize - 1:
          if isEven(i):
            move(North)
          else:
            move(South)

      if i != worldSize - 1:
        move(East)

def drone():
  farm(farmSize)

staringPositions = [
  [6, 0],
  [12, 0],
  [18, 0],
  [24, 0],

  [0, 6],
  [6, 6],
  [12, 6],
  [18, 6],
  [24, 6],

  [0, 12],
  [6, 12],
  [12, 12],
  [18, 12],
  [24, 12],

  [0, 18],
  [6, 18],
]

for i in range(len(staringPositions)):
  goToPosition(staringPositions[i][0], staringPositions[i][1])
  spawn_drone(drone)

goToPosition(0, 0)
drone()
