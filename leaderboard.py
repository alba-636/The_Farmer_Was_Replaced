
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
