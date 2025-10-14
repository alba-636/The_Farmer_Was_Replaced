from __builtins__ import *

clear()
change_hat(Hats.Green_Hat)

worldSize = get_world_size()
global tail_length
tail_length = 0

def is_even(x):
  return x % 2 == 0

def custom_move(direction):
  if get_entity_type() == Entities.Apple:
    global tail_length
    tail_length += 1
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
        if is_even(i):
          custom_move(North)
        else:
          custom_move(South)

    if i != worldSize - 1:
      custom_move(East)

  custom_move(South)
  for i in range(worldSize - 1):
    custom_move(West)
  custom_move(North)
