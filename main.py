from __builtins__ import *
from common import *

helloWorld()
clear()

worldSize = get_world_size()

def custom_move(direction):
  if move(direction) == False:
    change_hat(Hats.Brown_Hat)
    change_hat(Hats.Dinosaur_Hat)

change_hat(Hats.Dinosaur_Hat)

custom_move(North)

square = worldSize - 1

while True:
  for i in range(worldSize):
    for y in range(square):
  
      if y != square - 1:
        if isEven(i):
          custom_move(North)
        else:
          custom_move(South)

    if i != worldSize - 1:
      custom_move(East)

  custom_move(South)
  for i in range(worldSize - 1):
    custom_move(West)
  custom_move(North)
