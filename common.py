
def helloWorld():
    print("Hello, World!")

def isEven(x):
  return x % 2 == 0

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
  if plantType == Entities.Grass:
    gatherPlantGrass()
  elif plantType == Entities.Bush:
    gatherPlantBush()
  elif plantType == Entities.Tree:
    gatherPlantTree()
  elif plantType == Entities.Carrot:
    gatherPlantCarrot()
  elif plantType == Entities.Pumpkin:
    gatherPlantPumpkin()
  elif plantType == Entities.Sunflower:
    gatherPlantSunflower()
  elif plantType == Entities.Cactus:
    gatherPlantCactus()

def useWater(min):
  if get_water() < min:
    use_item(Items.Water)

