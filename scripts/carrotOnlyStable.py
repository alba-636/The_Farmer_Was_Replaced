from __builtins__ import *

clear()
change_hat(Hats.Green_Hat)

GRASS_TREE = 0
CARROT = 1
CARROT_TREE = 2

worldSize = get_world_size()
columsDisposition = [
  CARROT_TREE,
  GRASS_TREE,
  CARROT_TREE,
  GRASS_TREE,
  CARROT_TREE,
  GRASS_TREE,
  CARROT_TREE,
  GRASS_TREE,
  CARROT_TREE,
  GRASS_TREE,
  CARROT_TREE,
  GRASS_TREE,
]

def isEven(x):
  return x % 2 == 0


def gatherPlantGrass():
  if can_harvest():
    harvest()

def gatherPlantTree():
  if can_harvest():
    harvest()
    plant(Entities.Tree)
  
  # if get_water() < 0.5:
  #   use_item(Items.Water)

def gatherPlantCarrot():
  if can_harvest():
    harvest()
    plant(Entities.Carrot)


# Tile the farm
for i in range(worldSize):
  for y in range(worldSize):
    if columsDisposition[i] == CARROT or columsDisposition[i] == CARROT_TREE:
      till()
      plant(Entities.Carrot)
    if y != worldSize - 1:
      if isEven(i):
        move(North)
      else:
        move(South)

  if i != worldSize - 1:
    move(East)

move(East)
if not isEven(worldSize):
  move(North)


while True:
  for i in range(worldSize):
    for y in range(worldSize):
      if columsDisposition[i] == GRASS_TREE:
        if isEven(y):
          gatherPlantTree()
        else:
          gatherPlantGrass()

      if columsDisposition[i] == CARROT:
        gatherPlantCarrot()

      if columsDisposition[i] == CARROT_TREE:
        if isEven(y):
          gatherPlantTree()
        else:
          gatherPlantCarrot()


      if y != worldSize - 1:
        if isEven(i):
          move(North)
        else:
          move(South)

    if i != worldSize - 1:
      move(East)

  move(East)
  if not isEven(worldSize):
    move(North)
