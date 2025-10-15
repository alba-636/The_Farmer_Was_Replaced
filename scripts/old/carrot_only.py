from __builtins__ import *

clear()

change_hat(Hats.Green_Hat)

# Tile the farm
for i in range(get_world_size()):
  for y in range(get_world_size()):
    if can_harvest():
      harvest()

    till()
    plant(Entities.Carrot)
    if y != get_world_size() - 1:
      if (i + 1) % 2 == 1:
        move(North)
      else:
        move(South)

  if i != get_world_size() - 1:
    move(East)

move(East)
if get_world_size() % 2 == 1:
  move(North)

while True:
  for i in range(get_world_size()):
    for y in range(get_world_size()):
      if can_harvest():
        harvest()
        plant(Entities.Carrot)
      if y != get_world_size() - 1:
        if (i + 1) % 2 == 1:
          move(North)
        else:
          move(South)

    if i != get_world_size() - 1:
      move(East)

  move(East)
  if get_world_size() % 2 == 1:
    move(North)

