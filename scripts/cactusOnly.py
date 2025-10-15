from __builtins__ import *
from common import *

helloWorld()
clear()

worldSize = 32

def plantCactusOfSize(size):
  if get_ground_type() != Grounds.Soil:
    till()
  while measure() != size:
    harvest()
    plant(Entities.Cactus)

areAllSameSize = False
while True:
  goToPosition(0, 0)
  if areAllSameSize and can_harvest():
    harvest()
    
  areAllSameSize = True

  for i in range(worldSize):
    for y in range(worldSize):
      size = 9
      plantCactusOfSize(size)
      if measure() != size:
        areAllSameSize = False
      if y != worldSize - 1:
        if isEven(i):
          move(North)
        else:
          move(South)

    if i != worldSize - 1:
      move(East)
    