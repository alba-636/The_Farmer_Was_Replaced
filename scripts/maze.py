from __builtins__ import *
from common import *

clear()
change_hat(Hats.Purple_Hat)

def spawnMaze(worldSize):
  if get_ground_type() != Grounds.Grassland:
    till()
  plant(Entities.Bush)
  substanceCount = worldSize * 2**(num_unlocked(Unlocks.Mazes) - 1)
  use_item(Items.Weird_Substance, substanceCount)

def getCommingFrom(direction):
  if direction == North:
    return South
  elif direction == East:
    return West
  elif direction == South:
    return North
  elif direction == West:
    return East
  else:
    return None

def buildDeadPositions(worldSize):
  array = []
  for _ in range(worldSize):
    columns = []
    for _ in range(worldSize):
      columns.append(False)
    array.append(columns)
  return array

def isInDeadPositions(direction, deadPositions, offsetX, offsetY):
  x = get_pos_x() - offsetX
  y = get_pos_y() - offsetY
  if direction == North:
    y += 1
  elif direction == East:
    x += 1
  elif direction == South:
    y -= 1
  elif direction == West:
    x -= 1
  return deadPositions[x][y]

def solveMazeRandom(x, y, worldSize, offsetX, offsetY):
  commingFrom = None
  hasFoundTreasure = False
  deadPositions = buildDeadPositions(worldSize)

  while not hasFoundTreasure:
    if get_entity_type() == Entities.Treasure:
      harvest()
      hasFoundTreasure = True
      harvest()
      goToPosition(x, y)
      break
  
    canGoTo = []
    def canGoToDirection(direction):
      if direction != commingFrom and can_move(direction) and not isInDeadPositions(direction, deadPositions, offsetX, offsetY):
        canGoTo.append(direction)
    canGoToDirection(North)
    canGoToDirection(East)
    canGoToDirection(South)
    canGoToDirection(West)

    direction = None
    if len(canGoTo) > 0:
      index = rand(0, len(canGoTo))
      direction = canGoTo[index]
    else:
      direction = commingFrom
      commingFrom = None

    if len(canGoTo) <= 1 and (commingFrom == None or isInDeadPositions(commingFrom, deadPositions, offsetX, offsetY)):
      deadPositions[get_pos_x() - offsetX][get_pos_y() - offsetY] = True

    move(direction)
    commingFrom = getCommingFrom(direction)

def maze(x, y, worldSize, offsetX, offsetY):
  goToPosition(x, y)
  sleep(5)

  while True:
    spawnMaze(worldSize)
    solveMazeRandom(x, y, worldSize, offsetX, offsetY)


mazeSize = 5

def drone():
  x = get_pos_x()
  y = get_pos_y()
  offset = mazeSize // 2
  offsetX = offset 
  offsetY = offset 
  if x == 0:
    offsetX = 0
  if y == 0:
    offsetY = 0
  maze(x + offsetX, y + offsetY, mazeSize, x, y)

staringPositions = buildStartingPositions(mazeSize, mazeSize)

for i in range(len(staringPositions)):
  if i == 31:
    continue
  goToPosition(staringPositions[i][0], staringPositions[i][1])
  spawn_drone(drone)

# Manually put the main drone on the last available position.
maze(7, 27, mazeSize, 5, 25)
