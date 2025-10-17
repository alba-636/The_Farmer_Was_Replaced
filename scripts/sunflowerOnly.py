from __builtins__ import *
from common import *

farmSize = 5

clear()

def farm():
  while True:
    gatherPlantSunflower()
    useWater(0.5, 4)
    move(North)

for _ in range(31):
  spawn_drone(farm)
  move(East)

farm()
