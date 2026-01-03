# From: Alba-636
# Leaderboard: Wood_Single
# Best time: 06:57.134
# At: 2026-01-03

# Avg: 6:2.1
# Min: 5:41.7
# Max: 6:14.41

set_world_size(12)

while True:
  plantType, (_, _) = get_companion()
  if can_harvest():
    harvest()
    plant(Entities.Tree)
    if num_items(Items.Wood) >= 500000000:
      break
  elif plantType != Entities.Grass:
    harvest()
    plant(Entities.Tree)
  else:
    if get_water() < 0.64:
      use_item(Items.Water, 4)
    move(North)
    move(East)


