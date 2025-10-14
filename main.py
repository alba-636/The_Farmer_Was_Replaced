from __builtins__ import *
from common import *

worldSize = 6

helloWorld()
clear()

while True:
  goToPosition(0, 0)

  gatherable_count = 0
  for i in range(worldSize):
    for y in range(worldSize):
      if get_ground_type() != Grounds.Soil:
        till()

      if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
        plant(Entities.Pumpkin)

      if can_harvest():
        gatherable_count += 1

      if get_water() < 0.2:
        use_item(Items.Water)

      if y != worldSize - 1:
        if isEven(i):
          move(North)
        else:
          move(South)

    if i != worldSize - 1:
      move(East)

  if gatherable_count == worldSize * worldSize:
    harvest()

  # Sunflowers
  positions = [[6, 0], [6, 1], [6, 2]]
  for i in range(len(positions)):
    goToPosition(positions[i][0], positions[i][1])
    if get_ground_type() != Grounds.Soil:
      till()
    if can_harvest():
      harvest()
    if get_entity_type() == None or get_entity_type() != Entities.Sunflower:
      plant(Entities.Sunflower)
    if get_water() < 0.9:
      use_item(Items.Water)

      



