from __builtins__ import *
from common import *

# 6074 / seconds
# Grow: 1000ms | 600 ticks
# Water Cost: 200 tick

# 4.79
# 1.81

# 27-28

# 2 Grass
# 34 - 35




def test(farmSize):
  quick_print("Farm size:", farmSize)
  set_world_size(farmSize)

  # startTime = get_time()
  # startTick = get_tick_count()

  xMax = farmSize - 1
  for x in range(farmSize):
    for y in range(farmSize):
      if isEven(x):
        goToPosition(x, y)
      else:
        goToPosition(x, xMax - y)
        
      plant(Entities.Bush)

  x = farmSize // 2
  goToPosition(x, x)

  # move(North)
  # plant(Entities.Bush)
  # move(North)
  # plant(Entities.Bush)
  # move(North)
  # plant(Entities.Bush)
  # move(North)
  # move(East)
  # plant(Entities.Bush)
  # move(East)
  # plant(Entities.Bush)
  # move(East)
  # plant(Entities.Bush)
  # move(East)
  # plant(Entities.Bush)
  # move(South)
  # plant(Entities.Bush)
  # move(South)
  # plant(Entities.Bush)
  # move(South)
  # plant(Entities.Bush)
  # move(South)
  # plant(Entities.Bush)
  # move(West)
  # plant(Entities.Bush)
  # move(West)
  # plant(Entities.Bush)
  # move(West)
  # plant(Entities.Bush)
  # move(North)
  # plant(Entities.Bush)
  # move(North)
  # plant(Entities.Bush)
  # move(North)
  # plant(Entities.Bush)
  # move(East)
  # plant(Entities.Bush)
  # move(East)
  # plant(Entities.Bush)
  # move(South)
  # move(South)
  # plant(Entities.Bush)
  # move(West)
  # plant(Entities.Bush)
  # move(North)

  # quick_print("Setup time:", get_time() - startTime) # 1.48
  # quick_print("Setup ticks:", get_tick_count() - startTick) # 9002

  loopTick = []

  hay = num_items(Items.Hay)

  # while True:
  for _ in range(10000):
    sTick = get_tick_count()
    plantType, (_, _) = get_companion()
    if can_harvest() or plantType != Entities.Bush:
      harvest()
    else:
      useWater(0.73, 4)
      if get_pos_x() == x:
        move(East)
      else:
        move(West)

    loopTick.append(get_tick_count() - sTick)

  quick_print("Tick:", sum(loopTick) / len(loopTick)) # 206.71
  quick_print("Tick min:", minOf(loopTick)) # 204
  quick_print("Tick max:", maxOf(loopTick)) # 411
  quick_print("Hay /t:", (num_items(Items.Hay) - hay) / sum(loopTick)) # 96.49


test(3)
test(4)
test(5)
test(6)
test(7)
test(8)
test(9)

# 3 = 89.87
# 4 = 91.24
# 5 = 95.09
# 6 = 96.61
# 7 = 94.41
# 8 = 94.24
# 9 = 94.8
