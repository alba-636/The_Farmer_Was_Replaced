from __builtins__ import *
from common import *

clear()

worldSize = get_world_size() - 6
positions = [
  [3, 3],
  # [3, 7],
  # [3, 11],
  # [7, 11],
  # [7, 7],
  # [7, 3],
  # [11, 3],
  # [11, 7],
  # [11, 11],
]

while True:
  for i in range(len(positions)):
    x = positions[i][0]
    y = positions[i][1]
    plantType = Entities.Tree

    goToPosition(x, y)
    gatherAndPlant(plantType)
    useFertilizer()
    # useWater(0.9)

    # Polyculture/compagnon
    companionPlantType, (companionX, companionY) = get_companion()
    goToPosition(companionX, companionY)
    if get_entity_type() != companionPlantType:
      gatherAndPlant(companionPlantType)
    # useWater(0.9)
    goToPosition(x, y)
    
