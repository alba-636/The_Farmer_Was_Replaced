from __builtins__ import *
from common import *

# 6074 / seconds
# Grow: 1000ms | 600 ticks


companions = {
  Entities.Grass: 0,
  Entities.Bush: 0,
  Entities.Tree: 0,
  Entities.Carrot: 0,
}

def test(param = None):


  set_world_size(12)

  # while True:
  for _ in range(1000):
    harvest()
    plant(Entities.Bush)
    plantType, (_, _) = get_companion()

    companions[plantType] += 1


    # plantType, (_, _) = get_companion()
    # if can_harvest():
    #   harvest()
    #   plant(Entities.Tree)
    #   # if num_items(Items.Wood) >= 500000000:
    #   #   break
    # elif plantType != Entities.Grass:
    #   harvest()
    #   plant(Entities.Tree)
    # else:
    #   if get_water() < 0.9:
    #     use_item(Items.Water, 4)

global param
test()

quick_print(companions)

# Avg: 6:3.71
# Min: 5:49.14
# Max: 6:21.7




# Testing: 12 0.64
# Avg: 5:57.84
# Min: 5:43.4
# Max: 6:16.76

