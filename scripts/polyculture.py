from __builtins__ import *

clear()

NONE = 0
GRASS = Entities.Grass
BUSH = Entities.Bush
TREE = Entities.Tree
CARROT = Entities.Carrot
PUMPKIN = Entities.Pumpkin
SUNFLOWER = Entities.Sunflower
CACTUS = Entities.Cactus

worldSize = get_world_size() - 6
positions = [
  [3, 3],
  [3, 7],
  # [3, 11],
  # [7, 11],
  [7, 7],
  [7, 3],
  # [11, 3],
  # [11, 7],
  # [11, 11],
]

def goToPosition(x, y):
  moveX = x - get_pos_x()
  for _ in range(abs(moveX)):
    if moveX > 0:
      move(East)
    else:
      move(West)

  moveY = y - get_pos_y()
  for _ in range(abs(moveY)):
    if moveY > 0:
      move(North)
    else:
      move(South)

def is_even(x):
  return x % 2 == 0

def gatherPlantNone():
  if get_ground_type() != Grounds.Soil:
    till()

def gatherPlantGrass():
  if get_ground_type() != Grounds.Grassland:
    till()
  if can_harvest():
    harvest()

def gatherPlantBush():
  if get_ground_type() != Grounds.Grassland:
    till()
  if can_harvest():
    harvest()
  if get_entity_type() != Entities.Bush:
    plant(Entities.Bush)

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

def gatherAndPlant(plantType):
  if plantType == GRASS:
    gatherPlantGrass()
  if plantType == BUSH:
    gatherPlantBush()
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

def useWater():
  if get_water() < 0.9:
    use_item(Items.Water)

while True:
  for i in range(len(positions)):
    x = positions[i][0]
    y = positions[i][1]
    plantType = CARROT

    goToPosition(x, y)
    gatherAndPlant(plantType)
    useWater()

    # Polyculture/compagnon
    companionPlantType, (companionX, companionY) = get_companion()
    goToPosition(companionX, companionY)
    if get_entity_type() != companionPlantType:
      gatherAndPlant(companionPlantType)
    useWater()
    goToPosition(x, y)
    

