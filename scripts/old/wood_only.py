from __builtins__ import *

clear()
change_hat(Hats.Green_Hat)

worldSize = get_world_size()

while True:
  for i in range(worldSize):
    for y in range(worldSize):
      if can_harvest():
        harvest()
        plant(Entities.Bush)

      if y != worldSize - 1:
        if (i + 1) % 2 == 1:
          move(North)
        else:
          move(South)

    if i != worldSize - 1:
      move(East)

  move(East)
  if worldSize % 2 == 1:
    move(North)

