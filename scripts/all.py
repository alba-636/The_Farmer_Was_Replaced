from __builtins__ import *

clear()

NONE = 0
GRASS = 1
TREE = 2
CARROT = 3
PUMPKIN = 4
SUNFLOWER = 5
CACTUS = 6

worldSize = get_world_size()
columsDisposition = [
  [GRASS, TREE, CARROT, PUMPKIN, SUNFLOWER, CACTUS],
  [SUNFLOWER, CACTUS, GRASS, TREE, CARROT, PUMPKIN],
  [CARROT, PUMPKIN, SUNFLOWER, CACTUS, GRASS, TREE],
]

def is_even(x):
  return x % 2 == 0

def gatherPlantNone():
  if get_ground_type() != Grounds.Soil:
    till()

def gatherPlantGrass():
  if can_harvest():
    harvest()

def gatherPlantTree():
  if get_ground_type() != Grounds.Soil:
    till()
  if can_harvest():
    harvest()
  if get_entity_type() != Entities.Tree:
    plant(Entities.Tree)

def gatherPlantCarrot():
  if get_ground_type() != Grounds.Soil:
    till()
  if can_harvest():
    harvest()
  if get_entity_type() == None:
    plant(Entities.Carrot)

def gatherPlantPumpkin():
  if get_ground_type() != Grounds.Soil:
    till()
  if can_harvest():
    harvest()
  if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
    plant(Entities.Pumpkin)

def gatherPlantSunflower():
  if get_ground_type() != Grounds.Soil:
    till()
  if can_harvest():
    harvest()
  if get_entity_type() == None:
    plant(Entities.Sunflower)


def gatherPlantCactus():
  if get_ground_type() != Grounds.Soil:
    till()
  if can_harvest():
    harvest()
  if get_entity_type() == None:
    plant(Entities.Cactus)

while True:
  for i in range(worldSize):
    for y in range(worldSize):
      x = get_pos_x() % len(columsDisposition)
      z = get_pos_y() % len(columsDisposition[x])

      plantType = columsDisposition[x][z]

      if plantType == NONE:
        gatherPlantNone()

      if plantType == GRASS:
        gatherPlantGrass()

      if plantType == TREE:
        gatherPlantTree()

      if plantType == CARROT:
        gatherPlantCarrot()

      if plantType == PUMPKIN:
        gatherPlantPumpkin()

      if plantType == SUNFLOWER:
        gatherPlantSunflower()

      if plantType == CACTUS:
        gatherPlantCactus()


      if y != worldSize - 1:
        if is_even(i):
          move(North)
        else:
          move(South)

    if i != worldSize - 1:
      move(East)     

  move(East)
  if not is_even(worldSize):
    move(North)
