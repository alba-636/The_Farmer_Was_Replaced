from __builtins__ import *
from common import *

worldSize = 6

clear()

while True:
  goToPosition(0, 0)

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
