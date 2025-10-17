# From: Alba-636
# Leaderboard: Cactus
# Best time: 00:36.396
# Rank: #44
# At: 2025-10-17

from __builtins__ import *
from common import *

clear()

def hasSuccess():
  return num_items(Items.Cactus) >= 33554432 # 33_554_432

def plantCactusOfSize(size):
  if get_ground_type() != Grounds.Soil:
    till()
  while measure() != size:
    harvest()
    plant(Entities.Cactus)

def cactus():
  size = 9
  for _ in range(32):
    plantCactusOfSize(size)
    move(North)
      
staringPositions = buildStartingPositions(1, 32)

while True:
  if hasSuccess():
    break

  drones = []
  for i in range(len(staringPositions)):
    if i == 31:
      continue
    goToPosition(staringPositions[i][0], staringPositions[i][1])
    drone = spawn_drone(cactus)
    drones.append(drone)

  goToPosition(31, 0)
  cactus()

  for i in range(len(drones)):
    wait_for(drones[i])

  sleep(5)
  harvest()
