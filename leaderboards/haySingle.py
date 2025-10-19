# From: Alba-636
# Leaderboard: Hay_Single
# Best time: 02:54.114
# At: 2025-10-18

# Avg: 2:55.57
# Min: 2:48.96
# Max: 3:3.98

set_world_size(5)

move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
move(East)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(East)
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
move(West)
plant(Entities.Bush)
move(West)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(North)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(East)
plant(Entities.Bush)
move(South)
move(South)
plant(Entities.Bush)
move(West)
plant(Entities.Bush)
move(North)

while True:
  plantType, (_, _) = get_companion()
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
