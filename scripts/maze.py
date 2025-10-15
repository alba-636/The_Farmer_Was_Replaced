from __builtins__ import *
from common import *

clear()

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


mazeSize = 10

def drone2():
  maze(15, 0, mazeSize, 10, 0)
def drone3():
  maze(25, 0, mazeSize, 20, 0)
def drone4():
  maze(0, 15, mazeSize, 0, 10)
def drone5():
  maze(15, 15, mazeSize, 10, 10)
def drone6():
  maze(25, 15, mazeSize, 20, 10)
def drone7():
  maze(0, 25, mazeSize, 0, 20)
def drone8():
  maze(15, 25, mazeSize, 10, 20)

spawn_drone(drone2)
spawn_drone(drone3)
spawn_drone(drone4)
spawn_drone(drone5)
spawn_drone(drone6)
spawn_drone(drone7)
spawn_drone(drone8)

# set_execution_speed(1)

maze(0, 0, mazeSize, 0, 0)
