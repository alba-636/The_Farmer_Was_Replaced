# From: Alba-636
# Leaderboard: Hay_Single
# Best time: 02:55.374
# At: 2026-01-03

# Avg: 2:56.69
# Min: 2:48.24
# Max: 3:5.5

set_world_size(5)

move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(South)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(South)
plant(Entities.Bush)
move(South)
plant(Entities.Bush)
move(South)
plant(Entities.Bush)
move(South)
plant(Entities.Bush)
move(West)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(West)
plant(Entities.Bush)
move(South)
plant(Entities.Bush)
move(West)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(East)

while True:
  compagion = get_companion()
  if compagion == None:
    break
  plantType, (_, _) = compagion
  if can_harvest():
    harvest()
    if num_items(Items.Hay) >= 100000000:
      break
  elif plantType != Entities.Bush:
    harvest()
  else:
    if get_water() < 0.67:
      use_item(Items.Water, 4)
    if get_pos_x() == 2:
      move(East)
    else:
      move(West)
