from __builtins__ import *
from common import *

clear()

def farm(plantType, positions):
  initialX = get_pos_x()
  initialY = get_pos_y()

  while True:
    for i in range(len(positions)):
      x = positions[i][0] + initialX
      y = positions[i][1] + initialY

      goToPosition(x, y)
      gatherAndPlant(plantType)

      # useFertilizer()
      useWater(0.9)

      # Polyculture/compagnon
      companionPlantType, (companionX, companionY) = get_companion()
      goToPosition(companionX, companionY)
      if get_entity_type() != companionPlantType:
        gatherAndPlant(companionPlantType)
      goToPosition(x, y)

def drone():
  plantType = Entities.Carrot
  positions = [[3, 3], [3, 7], [7, 7], [7, 3]]
  farm(plantType, positions)

staringPositions = buildStartingPositions(8, 8)

for i in range(len(staringPositions)):
  if i == 0:
    continue
  goToPosition(staringPositions[i][0], staringPositions[i][1])
  spawn_drone(drone)

goToPosition(0, 0)
drone()
