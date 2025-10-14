from __builtins__ import *

clear()
change_hat(Hats.Green_Hat)

worldSize = 6

def is_even(x):
  return x % 2 == 0

def goToPosition(x, y):
  moveX = x - get_pos_x()
  for _ in range(abs(moveX)):
    if moveX > 0:
      move(East)
    else:
      move(West)

  moveY = y - get_pos_y()
  for _ in range(abs(moveY)):
    if moveY > 0:
      move(North)
    else:
      move(South)

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
        if is_even(i):
          move(North)
        else:
          move(South)

    if i != worldSize - 1:
      move(East)
